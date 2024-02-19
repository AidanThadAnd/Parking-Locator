

import pandas as pd
import datetime
import re
dataframe = pd.read_csv("/users/andresisturiz/PARKING/datasets/On-Street_Residential_Parking_Zones_20240217 copy 2.csv")
#Check if Parking spot is open according to the local time and then 
#Takes in address to see if it is open


# Create a DataFrame for testing
#df = pd.read_csv("/users/andresisturiz/PARKING/datasets/On-Street_Residential_Parking_Zones_20240217 copy 2.csv")
#df = pd.DataFrame({'TIME_RESTRICTION': ['0800-1700 MON-FRI', '0900-1800 MON-SAT', 'Special Permit','0800-2359 MON-SUN',]})

def enforceable_time_check(dataframe):
    # Get current user time and day
    current_time = datetime.datetime.now().strftime("%H%M")
    current_day = datetime.datetime.now().strftime("%A").upper()
    print(current_day)
    print(current_time)
    # List to store indices of rows to be removed
    rows_to_remove = []

    for x in dataframe.index:
        # Check if the cell in the "TIME_RESTRICTION" column is not empty or None
        if pd.notna(dataframe.loc[x, "TIME_RESTRICTION"]): #and dataframe.loc[x, "TIME_RESTRICTION"] != "None":
            # Extracting more information from the cell's content using regular expressions
            match = re.match(r'(\d{4}-\d{4})?\s*(\w+(?:-\w+)?(?:\s*-\s*\w+)?|\w+)', dataframe.loc[x, "TIME_RESTRICTION"])
            if match:
                time_range, day_range = match.groups()
                if time_range:
                    start_time, end_time = time_range.split('-')
                    if '-' in day_range:
                        start_day, end_day = map(str.strip, day_range.split('-'))
                    else:
                        start_day = end_day = day_range.strip()

                    # Check if the current time is within the time range and day range
                    if start_day <= current_day <= end_day and start_time <= current_time <= end_time:
                        continue  # User's time is within the range, so continue to the next row
                else:
                    # If the cell only contains a day like "SUN"
                    if current_day != day_range:
                        continue  # User's day is different, so continue to the next row
            elif dataframe.loc[x,"TIME_RESTRICTION"] == "None":
                continue

            
        

        dataframe.drop(x, inplace = True)
        #rows_to_remove.append(x)

    # Remove rows marked for removal
        #dataframe.drop(rows_to_remove[x], inplace=True)







