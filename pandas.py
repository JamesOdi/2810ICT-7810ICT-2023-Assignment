import pandas as pd

# You can set some options to better print pandas df
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', 20)

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
filtered_df = df.loc[(df['OFFENCE_MONTH'] >= from_date)
                      & (df['OFFENCE_MONTH'] <= to_date)]
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
