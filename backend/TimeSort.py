

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
    current_day = datetime.datetime.now().strftime("%a").upper()

    # List to store indices of rows to be removed
    rows_to_remove = []

    day_indices = {
    'MON': 0,
    'TUE': 1,
    'WED': 2,
    'THU': 3,
    'FRI': 4,
    'SAT': 5,
    'SUN': 6,
    'FR': 4
    }

    for index, row in dataframe.iterrows():
        time_restriction = row["TIME_RESTRICTION"]
 
        if time_restriction == "None":
            continue
        
        # Skip if the value is None or NaN
        if pd.isna(time_restriction):
            continue
        
        # Extract time and day range
        match = re.match(r'(\d{4}-\d{4})?\s*(\w+(?:-\w+)?(?:\s*-\s*\w+)?)', time_restriction)
        if match:
            time_range, day_range = match.groups()
                     
            # If time range exists, check if current time falls within it
            if time_range:
                    start_time, end_time = time_range.split('-')
                    
                    if not start_time <= current_time <= end_time:
                        rows_to_remove.append(index)
                                  
            # If day range exists, check if current day falls within it
            if day_range:                  
                    
                    # Check if it's a single day or a range
                    if '-' in day_range:
                        # It's a range, split and check if the current day is within it
                        start_day, end_day = day_range.split('-')
                        # Convert day names to their corresponding indices
                        start_day_index = day_indices[start_day]
                        end_day_index = day_indices[end_day]
                        current_day_index = day_indices[current_day]

                        if start_day_index <= current_day_index <= end_day_index:
                            continue
                        else:
                            rows_to_remove.append(index)
            
                    if day_range == current_day:
                        continue
        if not match:
            continue
        
        # If execution reaches this point, remove the row
        rows_to_remove.append(index)

    # Remove rows marked for removal
    dataframe.drop(index=rows_to_remove, inplace=True)
    return dataframe
print("before: ")
print(dataframe)
enforceable_time_check(dataframe)
print("after: ")
print(dataframe)







