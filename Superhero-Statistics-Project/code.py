# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data['Gender'].replace('-', 'Agender', inplace =True)

gender_count = data['Gender'].value_counts()

gender_count.hist()
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment)
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()

sc_covariance = sc_df.cov().iloc[0,1]
print(sc_covariance)

sc_strength = sc_df['Strength'].std()

sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_strength * sc_combat)

print(sc_pearson)

ic_df = data[['Intelligence', 'Combat']]

ic_covariance = ic_df.cov().iloc[0,1]

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence * ic_combat)


print(ic_pearson)


# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)

super_best = data.loc[data['Total'] > 554.05]


super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1)


ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])
plt.title('Intelligence')
plt.title('Speed')
plt.title('Power')
plt.show()



