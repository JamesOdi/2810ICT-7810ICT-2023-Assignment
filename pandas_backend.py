import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# You can set some options to better print pandas df
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', 20)

# Variables for feature 2
offence_code = []
offence_code_total = []

df = pd.read_csv(r".\penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 1 --------------------
   Report the information of all penalty cases
'''
# Make index start from 1:
# df.index = range(1, len(df)+1)

'''
 IF FROM AND TO INPUT IS EMPTY -> USE DF DATAFRAME
 IF FROM AND TO INPUT IS ENTERED -> USE FILTERED_DF DATAFRAME
'''

# This prints all penalty cases from dates entered without specific requirements
from_date = input("From (dd/mm/yyyy) : ")
to_date = input("to (dd/mm/yyyy): ")
filtered_df = df.loc[(df['OFFENCE_MONTH'] >= from_date) & (df['OFFENCE_MONTH'] <= to_date)]
print(filtered_df) 

# Search offences by offence_code
code = int(input("Search by offence code: "))
offences = filtered_df[filtered_df['OFFENCE_CODE'] == code]
print(offences)

# Search offences by offence type
search = input("Search by offence type: ")
match search:
    case 'mobile':
        result = filtered_df[filtered_df['MOBILE_PHONE_IND'] == 'Y']
        print(result)
    case 'seatbelt':
        result = filtered_df[filtered_df['SEATBELT_IND'] == 'Y']
        print(result)
    case 'speed': 
        result = filtered_df[filtered_df['SPEED_IND'] == 'Y'] 
        print(result)
    case 'food': 
        result = filtered_df[filtered_df['FOOD_IND'] == 'Y'] 
        print(result)
    case 'parking': 
        result = filtered_df[filtered_df['PARKING_IND'] == 'Y'] 
        print(result)

'''
   ------------ Feature 3 --------------------
   Retrieve all cases captured by radar or camera based on offense description
'''
radar = True # Check the checkbox value
if(radar):
   captured_cases = filtered_df[filtered_df['OFFENCE_DESC'].str.contains("Radar")]
   print(captured_cases)

camera = True # Check the checkbox value
if(camera):
   captured_cases = filtered_df[filtered_df['OFFENCE_DESC'].str.contains("Camera")]
   print(captured_cases)

lidar = True # Check the checkbox value
if(lidar):
   captured_cases = filtered_df[filtered_df['OFFENCE_DESC'].str.contains("Lidar")]
   print(captured_cases)

'''
   ------------ Feature 2 --------------------
   Produce a chart to show the distribution of cases in each offense code
'''
offence_code = df['OFFENCE_CODE'].unique().tolist()
for i in offence_code:
    offence_code_total.append(len(df[df['OFFENCE_CODE']==i]))
# Draw the bar graph
fig = plt.figure(figsize=(10, 7))  # figure size

plt.bar(np.arange(0, len(offence_code), step = 1), offence_code_total)
plt.margins(x=0, y=0)
plt.title("Penalty case distribution")
plt.ylabel("Distribution")
plt.xlabel("Offence code")
plt.xticks(np.arange(0, len(offence_code), step = 1), labels=offence_code)
plt.show()

'''
   ------------ Feature 4 and 5 --------------------
   Analysing the cases caused by mobile phone usage, seatbelt, ... - ie: trend over time, offense code, and so on.
'''

'''' -------------- MOBILE PHONE USAGE ---------------------'''
mobile_phone_df = df[df['MOBILE_PHONE_IND'] == 'Y']
mobile_offence_year = [] 
mobile_offence_total = []
count = {}

# pie chart show the percentage of mobile phone offence out of the total offences
plt.pie([len(mobile_phone_df), len(df)], labels=['Mobile phone usage','Total'], autopct='%1.1f%%', explode=(0, 0.5))
plt.show()

# ---- Information ----
info = mobile_phone_df.drop_duplicates(subset = 'OFFENCE_CODE')
print(info.loc[:,['OFFENCE_CODE', 'OFFENCE_DESC', 'OFFENCE_FINYEAR', 'OFFENCE_MONTH', 'FACE_VALUE']])


# ---- Trend ----
# Use dictionary to count the total of mobile usage offence in each year
for index, row in mobile_phone_df.iterrows():
    year = row['OFFENCE_MONTH'][-4:] 
    count[year] = count.get(year, 0) + 1

# Separate the keys and values to correspoding list to draw the trend
for key in sorted(count.keys()):
    mobile_offence_year.append(key)
    mobile_offence_total.append(count[key])

plt.plot(mobile_offence_year, mobile_offence_total, 'r-') 
plt.title("Trend of mobile phone usage offence") 
plt.ylabel("Total of offence") 
plt.xlabel("Year") 
plt.ylim(30, 60)
plt.show()

