import pandas as pd
import matplotlib.pyplot as plt

# You can set some options to better print pandas df
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', 20)

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
plt.bar(offence_code, offence_code_total)
plt.margins(x=0, y=0)
# plt.xticks(np.arange(0, len(offence_code), step = 1), labels = offence_code)
plt.title("Penalty case distribution") 
plt.ylabel("Distribution") 
plt.xlabel("Offence code") 
plt.show()