# script.py
import sys
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# You can set some options to better print pandas df
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', 20)

df = pd.read_csv(r"api/penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 1 --------------------
   Report the information of all penalty cases
'''
# Make index start from 1:
# df.index = range(1, len(df)+1)
input_data = sys.argv[1]

from_date = input("From (dd/mm/yyyy) : ") # take value from html tag
to_date = input("to (dd/mm/yyyy): ") # take value from html tag

'''
 IF FROM AND TO INPUT IS EMPTY -> USE DF DATAFRAME
 IF FROM AND TO INPUT IS ENTERED -> USE FILTERED DATAFRAME
'''
if from_date == '' and to_date == '':
    data = df
    print(data)
else:
    data = df.loc[(df['OFFENCE_MONTH'] >= from_date) & (df['OFFENCE_MONTH'] <= to_date)]

# # Search offences by offence_code
# code = int(input("Search by offence code: "))
# offences = data[data['OFFENCE_CODE'] == code]
# print(offences)

# Search offences by offence type
    search = input("Search by offence type: ")
    match search:
        case 'mobile':
            result = data[data['MOBILE_PHONE_IND'] == 'Y']
        case 'seatbelt':
            result = data[data['SEATBELT_IND'] == 'Y']
        case 'speed': 
            result = data[data['SPEED_IND'] == 'Y'] 
        case 'food': 
            result = data[data['FOOD_IND'] == 'Y'] 
        case 'parking': 
            result = data[data['PARKING_IND'] == 'Y'] 
            
    print(result)
    