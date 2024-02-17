from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Perform tasks with CSV data here
    return "lol"

def read_data_from_csv(filename):
    # Logic to read data from CSV

    pass

def convert_coord_km(lat, long):
    return lat*111.2 + long*111.3

if __name__ == '__main__':
    app.run()