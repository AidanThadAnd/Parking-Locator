from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Perform tasks with CSV data here
    onsDF = read_data_from_csv('backend/datasets/On-Street_Parking_Zones_20240217.csv')
    resDF = read_data_from_csv('backend/datasets/On-Street_Residential_Parking_Zones_20240217.csv')
    return str(resDF)

def read_data_from_csv(filename):
    # Logic to read data from CSV
    dataFrame = pd.read_csv(filename)
    return dataFrame

# converts lat and long into km
def convert_coord_km(lat, long):
    return abs(lat*111.2) + abs(long*111.3)




if __name__ == '__main__':
    app.run()