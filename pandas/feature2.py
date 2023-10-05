import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

offence_code = []
offence_code_total = []

df = pd.read_csv(r".\penalty_data_set_2.csv", low_memory=False)

'''
   ------------ Feature 2 --------------------
   Produce a chart to show the distribution of cases in each offense code
'''
offence_code = df['OFFENCE_CODE'].unique().tolist()
for i in offence_code:
    offence_code_total.append(len(df[df['OFFENCE_CODE'] == i]))
# Draw the bar graph
fig = plt.figure(figsize=(10, 7))  # figure size

plt.bar(np.arange(0, len(offence_code), step=1), offence_code_total)
plt.margins(x=0, y=0)
plt.title("Penalty case distribution")
plt.ylabel("Distribution")
plt.xlabel("Offence code")
plt.xticks(np.arange(0, len(offence_code), step=1), labels=offence_code)
plt.show()
