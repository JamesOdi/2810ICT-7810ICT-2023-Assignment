import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 20)

offence_year = []
offence_code_total = []
offence_count = {}

df = pd.read_csv(r".\penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 2 --------------------
   Produce a chart to show the distribution of cases in each offense code
'''
offence_code = int(input("Enter offence code: ")) # take value from html tag

data = df[df['OFFENCE_CODE'] == offence_code]

# Use dictionary to count the total of mobile usage offence in each year

for index, row in data.iterrows():
   year = row['OFFENCE_FINYEAR']
   offence_count[year] = offence_count.get(year, 0) + row['TOTAL_NUMBER']

for key in sorted(offence_count.keys()):
   offence_year.append(key)
   offence_code_total.append(offence_count[key])

# # Draw the bar graph
fig = plt.figure(figsize=(10, 7))  # figure size

plt.bar(offence_year, offence_code_total)
plt.title("Penalty case distribution")
plt.ylabel("Total of penalty notices issued")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.savefig("offence_code_distribution.png")
plt.show()
