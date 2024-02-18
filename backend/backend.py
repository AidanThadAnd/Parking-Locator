from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Perform tasks with CSV data here
    onsDF = read_data_from_csv('backend/datasets/On-Street_Parking_Zones_20240217.csv')
    resDF = read_data_from_csv('backend/datasets/On-Street_Residential_Parking_Zones_20240217.csv')
    userCoords = get_address_coords('1400 12 Ave SW, Calgary')
    res_filter_useless_restrictions(resDF)
    return resDF

def read_data_from_csv(filename):
    # Logic to read data from CSV
    dataFrame = pd.read_csv(filename)
    return dataFrame

# Hopefully brings everything together once front end data is passed.
def important_method(desiredTime, desiredDistance, payment, ovnight, userAddress):
    onsDF = read_data_from_csv('backend/datasets/On-Street_Parking_Zones_20240217.csv')
    resDF = read_data_from_csv('backend/datasets/On-Street_Residential_Parking_Zones_20240217.csv')
    userCoords = get_address_coords(userAddress)

    resFloatCoords = get_float_coords(resDF)
    onsFloatCoords = get_float_coords(onsDF)
    resTuples = avg_lat_long(resFloatCoords)
    onsTuples = avg_lat_long(onsFloatCoords)
    resDistList = compare_distances(userCoords=userCoords, tuplesList=resTuples)
    onsDistList = compare_distances(userCoords=userCoords, tuplesList=onsTuples)
    filter_df_distance(resDF, resDistList, desiredDistance)
    filter_df_distance(onsDF, onsDistList, desiredDistance)

    res_filter_useless_restrictions(resDF)
    ons_filter_non_parking_zones(onsDF)
    res_filter_parking_restrictions(resDF, desiredTime)
    ons_filter_parking_times(onsDF, desiredTime)
    if payment == True:
        filter_payment_required(resDF, onsDF)
    if ovnight == True:
        filter_overnight_parking(resDF)

    return onsDF, resDF

def filter_overnight_parking(dataFrame):
    for x in dataFrame.index:
            if dataFrame.loc[x,"PARKING_RESTRICTION"] != 'NONE':
                dataFrame.drop(x, inplace = True)
    return dataFrame

# filter useless restrictions
def res_filter_useless_restrictions(dataFrame):
    res_filter_parking_restrictions(dataFrame, 'Special Permit')
    res_filter_parking_restrictions(dataFrame, 'Handicap Permit Required')
    res_filter_parking_restrictions(dataFrame, 'EOC Permit')
    return dataFrame

# filters for users desired parking length
def ons_filter_parking_times(dataFrame, desiredRestriction):
    for x in dataFrame.index:
        if dataFrame.loc[x, "MAX_TIME"] < desiredRestriction:
            dataFrame.drop(x, inplace = True)
    return dataFrame

def filter_payment_required(resDataFrame, onsDataFrame):
    res_filter_parking_restrictions(resDataFrame, 'Payment Required')
    for x in onsDataFrame.index:
        if onsDataFrame.loc[x, "PRICE_ZONE"] != '':
            onsDataFrame.drop(x, inplace = True)
    return resDataFrame, onsDataFrame

# converts lat and long into km
def convert_coord_km(lat, long):
    return abs(lat*111.2) + abs(long*111.3)

# Filters the dataFrame by a desired parking restriction in the csv
def res_filter_parking_restrictions(dataFrame, desiredRestriction):
    if isinstance(desiredRestriction, int):
        for x in dataFrame.index:
            if dataFrame.loc[x,"PARKING_RESTRICTION"] != 'NONE' and dataFrame.loc[x,"PARKING_RESTRICTION"] != "Payment Required" and int(dataFrame.loc[x,"PARKING_RESTRICTION"]) < desiredRestriction:
                dataFrame.drop(x, inplace = True)
    else:
        for x in dataFrame.index:
            if dataFrame.loc[x,"PARKING_RESTRICTION"] == desiredRestriction:
                dataFrame.drop(x, inplace = True)
    return dataFrame

#filters non-parking zones
def ons_filter_non_parking_zones(dataFrame):
    for x in dataFrame.index:
        if dataFrame.loc[x, "ZONE_TYPE"] != 'Parking Zone':
            dataFrame.drop(x, inplace = True)
    return dataFrame

# This method uses the canadian governments free geolocation service to extract matching coordinates based on 
# provided address returns list of floats
def get_address_coords(address):
    # 1400 12 Ave SW, Calgary, AB T3C 0P7, 51.043345859995114, -114.0940433180538
    addressDF = requests.get('https://geogratis.gc.ca/services/geolocation/en/locate?q=' + address)
    userAddressList = addressDF.json()

    for x in userAddressList[1].values():
        if type(x) is dict:
            return x.get('coordinates')

# Parses the dataframe for coords and returns a list of lists containing floats for further analysis
# Returns list of list of floats
def get_float_coords(dataFrame):
    coordsList = []
    for string in dataFrame.loc[:, "line"]:
        getvals = []
        for val in string:
            if val.isdigit() or val.isspace() or val == '.':
                getvals.append(val)
        result = "".join(getvals)
        result = result.strip()
        list2 = result.split(" ")
        listnum = []
        for s in list2:
            z = float(s)
            listnum.append(z)
        coordsList.append(listnum)
    return coordsList

# Parses a list of lists of floats to produce the avg lat and long of lines
def avg_lat_long(coordsList):
    tuplesList = []
    for li in coordsList:
        l2 = []
        li.sort()
        sumFirstHalf = 0
        sumSecondHalf = 0
        for i in range(len(li)):
            if i < len(li)/2:
                sumFirstHalf += li[i]
                # print(sumFirstHalf)
            else:
                sumSecondHalf += li[i]
        l2.append(sumFirstHalf/(len(li)/2))
        l2.append(sumSecondHalf/(len(li)/2))
        tuplesList.append(l2)
    return tuplesList

# takes in userCoords and tuplesList to generate a list of distances from the user coords
def compare_distances(userCoords, tuplesList):
    distanceFromUserList = []
    for li in tuplesList:
        lat = abs(userCoords[1] - li[0])
        long = abs(li[1] + userCoords[0])
        distanceFromUserList.append(convert_coord_km(lat=lat, long=long))
    return distanceFromUserList

# filters dataframe based on distanceList got from compare_distances method and a desired distance filter
def filter_df_distance(df, distanceList, desiredDistance):
    for i in range(len(distanceList)):
        if distanceList[i] > desiredDistance:
            df.drop(index=i, inplace=True)
    return df

if __name__ == '__main__':
    app.run()




# print(important_method(180, .5, True, False, '1400 12 Ave SW, Calgary'))