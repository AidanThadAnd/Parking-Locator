# Park Freezy
The free and easy parking solution

## Inspiration
We wanted it to be easy to find free and easy parking given a location in Calgary, Alberta, Canada
## What it does
The web app takes in an address as a search parameter and a few filters for the user's desired walking distance, pay preference, and other filters, and then shows a map with a pin of the nearest parking location based on the users parameters.
## How we built it
We built it by connecting a frontend designed in Figma and implemented with HTML, CSS, JS, Node.js, with a Flask python server backend. We also used a library called Leaflet for the map. We took our data from https://data.calgary.ca/Transportation-Transit/On-Street-Residential-Parking-Zones/2rmy-g65b/about_data, https://data.calgary.ca/Transportation-Transit/On-Street-Parking-Zones/g33j-xi2h
## Accomplishments that we're proud of
We were able to effectively take the data from the CSV data files provided from the Calgary page and be able to filter through them for desired specifications. We were also able to make a pleasing frontend that was smooth and easy for users to use.

## Installing
<details>
  <summary>Installation Details</summary>
  To avoid the pain of dependency hell if you want to install and/or test this you will use the following steps to ensure proper repeatability and organization.

1. Activate the python virtual environment
  ```bash
  cd backend
  source/bin/activate  # Activate the virtual environment on Unix/macOS
  # OR
  myenv\Scripts\activate  # Activate the virtual environment on Windows
  ```
2. Install packages from 'requirements.txt'
   ```bash
    pip install -r requirements.txt
    ```
3. If you decide to add additional packages
   ```bash
   pip freeze > requirements.txt
   ```
    
   **By following these steps this should ensure that using this project is as painless as can be**
</details>

## Home Page & Filters Designed with Figma
<img width="316" height="700" alt="Screenshot 2024-02-28 at 11 03 46 AM" src="https://github.com/AidanThadAnd/Parking-Locator/assets/78242226/8ce3c680-2bc9-4ef6-aef5-e9759ccebc75">
<img width="316" height="700" alt="Screenshot 2024-02-28 at 11 04 12 AM" src="https://github.com/AidanThadAnd/Parking-Locator/assets/78242226/984f1105-5e9b-4fe3-aceb-36f07b60a9d3">

## Home Page & Filters Implementation
<img width="316" height="700" alt="Screenshot 2024-02-28 at 11 13 03 AM" src="https://github.com/AidanThadAnd/Parking-Locator/assets/78242226/c0655b3b-bd9e-46d0-92b6-cb71df62bb8f">
<img width="316" height="700" alt="Screenshot 2024-02-28 at 11 13 17 AM" src="https://github.com/AidanThadAnd/Parking-Locator/assets/78242226/07dbee15-b7f7-4098-bd34-65d3af5d96f1">


