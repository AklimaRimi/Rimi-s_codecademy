import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
high = np.max(flight['coach_price'])
low = np.min(flight['coach_price'])
average = np.mean(flight['coach_price'])

print(high,low,average)


sns.boxplot(flight['coach_price'])
plt.show()
plt.clf()

# $500 is a good price for coach ticket

## Task 2

take8 = flight[flight['hours']>=8]['coach_price']
sns.boxplot(take8)
plt.show()
plt.clf()


## Task 3
plt.hist(flight['delay'],color='red',alpha =1)
plt.show()
plt.clf()


## Task 4
plt.figure(figsize=(12,7))
plt.scatter(flight['coach_price'],flight['firstclass_price'])
plt.show()
plt.clf()

# retionship between two classes have positive association
## Task 5

# x  = flight['inflight_meal'].apply(lambda x :1 if x== 'Yes' else 0)
# plt.bar(x,flight['coach_price'])
# plt.show()


## Task 6
ps_vs_hours = flight.groupby(['hours']).passengers.sum().reset_index()
print(ps_vs_hours)
x = ps_vs_hours['hours'].values
y = ps_vs_hours['passengers'].values
sns.barplot(x,y)
plt.show()
plt.clf()

sns.scatterplot(x,y)
plt.show()
plt.clf()

## Task 7
weekend = flight[flight['weekend']=='Yes']
sns.scatterplot(weekend['coach_price'],weekend['firstclass_price'])
plt.show()
plt.clf()



## Task 8
sns.barplot(weekend['redeye'],weekend['coach_price'])
plt.show()
plt.clf()



