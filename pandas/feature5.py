import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r".\penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 5 --------------------
   Analysing the cases caused by exceed speed, ... - ie: trend over time, offense code, and so on.
'''

exceed_speed_df = df[df['SPEED_IND'] == 'Y']
offence_year = []
offence_total = []
count = {}

location_count = {}
location = []
location_total = []

# ---- PIE CHART ----
# pie chart show the percentage of exceed speed offence out of the total offences
plt.pie([exceed_speed_df['TOTAL_NUMBER'].sum(), df['TOTAL_NUMBER'].sum()], labels=['Exceed speed offences','Total offences'], autopct='%1.1f%%', explode=(0, 0.2))
plt.savefig("exceed_speed_percentage.png")
plt.show()

# # ---- Information display as a table ----
'''
    This part takes 100 first rows of the dataframe to save to a new csv file
'''
info = exceed_speed_df.drop_duplicates(subset = 'OFFENCE_CODE')
info_df = info.loc[:,['OFFENCE_CODE', 'OFFENCE_DESC', 'OFFENCE_FINYEAR', 'OFFENCE_MONTH', 'FACE_VALUE']].head(100)
info_df.to_csv('feature_5.csv', index=False)
print(info_df)

# # ---- TREND ----
# # Use dictionary to count the total of exceed speed offences in each year
# for index, row in exceed_speed_df.iterrows():
#     year = row['OFFENCE_MONTH'][-4:]
#     count[year] = count.get(year, 0) + row['TOTAL_NUMBER']

#     if str(row['LOCATION_DETAILS']).endswith('NORTHBOUND'):
#         location_count['NORTHBOUND'] = location_count.get('NORTHBOUND', 0) + 1
#     elif str(row['LOCATION_DETAILS']).endswith('SOUTHBOUND'):
#         location_count['SOUTHBOUND'] = location_count.get('SOUTHBOUND', 0) + 1
#     elif str(row['LOCATION_DETAILS']).endswith('EASTBOUND'):
#         location_count['EASTBOUND'] = location_count.get('EASTBOUND', 0) + 1
#     elif str(row['LOCATION_DETAILS']).endswith('WESTBOUND'):
#         location_count['WESTBOUND'] = location_count.get('WESTBOUND', 0) + 1

# # Separate the keys and values to correspoding list to draw the trend
# for key in sorted(count.keys()):
#     offence_year.append(key)
#     offence_total.append(count[key])

# # ---- Trend chart ----
# fig = plt.figure(figsize=(7, 5))
# plt.plot(offence_year, offence_total, 'b-')
# plt.title("Trend of exceed speed offences")
# plt.ylabel("Total of penalty notices issued")
# plt.xlabel("Year")
# plt.savefig("exceed_speed_trend.png")
# plt.show()

# # ---- Location chart ----
# for key in location_count.keys():
#     location.append(key)
#     location_total.append(location_count[key])

# plt.pie(location_total, autopct='%1.1f%%', startangle=90)
# plt.legend(location, loc='upper right')
# plt.savefig("exceed_speed_location.png")
# plt.show()
