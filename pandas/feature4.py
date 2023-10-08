import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r".\penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 4 --------------------
   Analysing the cases caused by mobile phone usage, ... - ie: trend over time, offense code, and so on.
'''

'''' -------------- MOBILE PHONE USAGE ---------------------'''
mobile_phone_df = df[df['MOBILE_PHONE_IND'] == 'Y']
mobile_offence_year = [] 
mobile_offence_total = []
count = {}

# pie chart show the percentage of mobile phone offence out of the total offences
plt.pie([mobile_phone_df['TOTAL_NUMBER'].sum(), df['TOTAL_NUMBER'].sum()], labels=['Mobile phone usage','Total'], autopct='%1.1f%%', explode=(0, 0.2))
plt.savefig("mobile_phone_usage_percentage.png")
plt.show()

# ---- Information display as a table ----
'''
    This part only has less than 30 rows so do not need to create a new csv file
'''
info = mobile_phone_df.drop_duplicates(subset = 'OFFENCE_CODE')
info_df = info.loc[:,['OFFENCE_CODE', 'OFFENCE_DESC', 'OFFENCE_FINYEAR', 'OFFENCE_MONTH', 'FACE_VALUE']]
print(info_df)


# ---- Trend ----
# Use dictionary to count the total of mobile usage offence in each year
for index, row in mobile_phone_df.iterrows():
    year = row['OFFENCE_MONTH'][-4:] 
    count[year] = count.get(year, 0) + row['TOTAL_NUMBER']

# Separate the keys and values to correspoding list to draw the trend
for key in sorted(count.keys()):
    mobile_offence_year.append(key)
    mobile_offence_total.append(count[key])

plt.plot(mobile_offence_year, mobile_offence_total, 'r-') 
plt.title("Trend of mobile phone usage offence") 
plt.ylabel("Total of penalty notices issued") 
plt.xlabel("Year") 
plt.savefig("mobile_phone_usage_trend.png")
plt.show()