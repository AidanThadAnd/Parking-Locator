from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Perform tasks with CSV data here
    onsDF = read_data_from_csv('backend/datasets/On-Street_Parking_Zones_20240217.csv')
    resDF = read_data_from_csv('backend/datasets/On-Street_Residential_Parking_Zones_20240217.csv')
    filter_parking_restrictions(resDF, "Payment Required")
    userCoords = get_address_coords('1400 12 Ave SW, Calgary')
    return userCoords

def read_data_from_csv(filename):
    # Logic to read data from CSV
    dataFrame = pd.read_csv(filename)
    return dataFrame

# converts lat and long into km
def convert_coord_km(lat, long):
    return abs(lat*111.2) + abs(long*111.3)

# Filters the dataFrame by a desired parking restriction in the csv
def filter_parking_restrictions(dataFrame, desiredRestriction):
    for x in dataFrame.index:
        if dataFrame.loc[x,"PARKING_RESTRICTION"] != desiredRestriction:
            dataFrame.drop(x, inplace = True)
    return dataFrame

# This method uses the canadian governments free geolocation service to extract matching coordinates based on 
# provided address
def get_address_coords(address):
    # 1400 12 Ave SW, Calgary, AB T3C 0P7, 51.043345859995114, -114.0940433180538
    addressDF = requests.get('https://geogratis.gc.ca/services/geolocation/en/locate?q=' + address)
    userAddressList = addressDF.json()

    for x in userAddressList[1].values():
        if type(x) is dict:
            return x.get('coordinates')

# Parses the dataframe for coords and returns a list of lists containing floats for further analysis
def get_float_coords(dataFrame):
    coordsList = []
    for string in resDF.loc[:, "line"]:
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

if __name__ == '__main__':
    app.run()

print(get_address_coords('1400 12 Ave SW, Calgary'))