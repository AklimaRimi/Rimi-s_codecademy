import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

#1
print(census.head())

#2
print(census.describe())

#3
print(census.dtypes)

#4
print(census.birth_year.unique())

#5 
census['birth_year'] = census['birth_year'].replace('missing','1967')
print(census.birth_year.unique())

#6
census['birth_year'] =census['birth_year'].astype(int)

#7
print(census['birth_year'].mean())

#8
census['higher_tax'] = pd.Categorical(census['higher_tax'],['strongly disagree','disagree','neutral','agree','strongly agree'],ordered = True)
print(census['higher_tax'].unique())

#9
#print(census['higher_tax'].median())

#10
census = pd.get_dummies(data = census,columns=['marital_status'])

print(census.head())

