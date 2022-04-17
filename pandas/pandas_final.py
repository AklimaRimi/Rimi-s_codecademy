import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import pandas as pd
import glob

census = pd.read_csv('states0.csv')
print(census.head())

dfs = glob.glob('states*.csv')
print(dfs)
#4
list_ =[]
for file in dfs:
  x = pd.read_csv(file)
  list_.append(x)
us_census = pd.concat(list_)

print(us_census.columns)
print(us_census.dtypes)

#5

us_census.Income = us_census.Income.str[1:]

#6

split_= us_census.GenderPop.str.split('_')
us_census['Men'] = split_.str[0]
us_census['Women'] = split_.str[1]

print(us_census.head())

#7
us_census['Men'] = us_census['Men'].str[0:-1]
us_census['Women'] = us_census['Women'].str[0:-1]
print(us_census.head())


#8

plt.scatter(pd.to_numeric(us_census['Women']), pd.to_numeric(us_census['Income']))
plt.show() 

#9
print(us_census.isnull().sum())

us_census['Women'] = us_census['Women'].fillna(pd.to_numeric(us_census['TotalPop']) - pd.to_numeric(us_census['Men']))


#10
census = us_census.drop_duplicates(subset = us_census.columns[1:])

#11
plt.scatter(pd.to_numeric(us_census['Women']), pd.to_numeric(us_census['Income']))
plt.show() 


#12
print(census.columns)

census = census.dropna()
for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
  x = census[race].str[:-1]
  census[race] = pd.to_numeric(x)
print(census)
for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.hist(census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()
