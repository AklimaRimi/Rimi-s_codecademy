import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data  = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

#3
print('there are {} columns availabe.'.format(len(diabetes_data.columns)))

#4
print(diabetes_data.shape)

#5
print(diabetes_data.isnull().sum())

#6
print(diabetes_data.describe())

#7 - 8
#Analysing abnormalities in BMI, Pregnencies, Insulin

#9
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

#10
print(diabetes_data.isnull().sum())

#11 

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#13
print(diabetes_data.dtypes)

#14
print(diabetes_data.Outcome.unique())

#15
diabetes_data.Outcome = diabetes_data.Outcome.replace('O','0')
diabetes_data.Outcome = pd.to_numeric(diabetes_data.Outcome)

print(diabetes_data.Outcome.unique())

#extra

for x in ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']:
  diabetes_data[x] = diabetes_data[x].fillna(diabetes_data[x].mean())


print(diabetes_data.isnull().sum())

print(diabetes_data.describe())

# much cleaner and acceptable data has been created 
