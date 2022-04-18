import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

#1 
print(healthcare.head())

#2
print(healthcare["DRG Definition"].unique())

#3
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

#4
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
print(alabama_chest_pain)

co_chest_pain = chest_pain[chest_pain['Provider State'] == "CO"]

ny_chest_pain = chest_pain[chest_pain['Provider State'] == "NY"]

#5
costs = alabama_chest_pain[' Average Covered Charges '].values

#6
plt.boxplot(costs,labels=['alabama'])
plt.show()
states=chest_pain['Provider State'].unique()

#7

ny_chest_pain = chest_pain[chest_pain['Provider State'] == "NY"][' Average Covered Charges '].values
plt.boxplot(ny_chest_pain)
plt.show()

datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

plt.figure(figsize=(20,6))

plt.boxplot(datasets,labels=states)
plt.show()

