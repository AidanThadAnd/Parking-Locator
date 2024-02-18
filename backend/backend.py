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
    for x in dataFrame.index:
        j = dataFrame.loc[x,"PARKING_RESTRICTION"]
        if j == 'Permit Required' or j == 'Payment Required':
            dataFrame.drop(x, inplace = True)
    return dataFrame

def important_method(desiredLength, desiredDistance):
    onsDF = read_data_from_csv('backend/datasets/On-Street_Parking_Zones_20240217.csv')
    resDF = read_data_from_csv('backend/datasets/On-Street_Residential_Parking_Zones_20240217.csv')

    res_filter_useless_restrictions(resDF)
    ons_filter_non_parking_zones(onsDF)

    res_filter_parking_restrictions(resDF, desiredLength)
    return

# filter useless restrictions
def res_filter_useless_restrictions(dataFrame):
    res_filter_parking_restrictions(dataFrame, 'Payment Required')
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

# converts lat and long into km
def convert_coord_km(lat, long):
    return abs(lat*111.2) + abs(long*111.3)

# Filters the dataFrame by a desired parking restriction in the csv
def res_filter_parking_restrictions(dataFrame, desiredRestriction):
    if isinstance(desiredRestriction, int):
        for x in dataFrame.index:
            if dataFrame.loc[x,"PARKING_RESTRICTION"] != 'NONE' and int(dataFrame.loc[x,"PARKING_RESTRICTION"]) < desiredRestriction:
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

if __name__ == '__main__':
    app.run()

print(home())