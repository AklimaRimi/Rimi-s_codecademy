import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#1
print(london_data.head())
print(london_data.iloc[100:200])

#2
print('There are {} datapoints.'.format(len(london_data)))

#3
temp = london_data['TemperatureC']

#4
average_temp = np.average(temp)
print('Average Temparature is: {}.'.format(average_temp))
#5
temperature_var = np.var(temp)
print('Variance of temperature is: {}'.format(temperature_var))

#6
temperature_standard_deviation = temperature_var**.5
print('Standard deviation of temperature is: {}'.format(temperature_standard_deviation))

#7
print(london_data.head())

#8
june = london_data[london_data['month']==6]['TemperatureC']

#9
july = london_data[london_data['month']==7]['TemperatureC']

#10
print('Mean of June Temparature is: {}.'.format(np.mean(june)))
print('Mean of July Temparature is: {}.'.format(np.mean(july)))

#11

print('Std of June Temparature is: {}.'.format(np.std(june)))
print('Std of July Temparature is: {}.'.format(np.std(july)))



#12
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")




