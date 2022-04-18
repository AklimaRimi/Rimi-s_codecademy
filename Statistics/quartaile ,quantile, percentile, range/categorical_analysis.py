import pandas as pd

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

#2
manufacturer_country = car_eval['manufacturer_country'].value_counts(normalize=True)

print('Country: {}'.format(manufacturer_country.index[0]))

#3
buyingCost = car_eval['buying_cost'].value_counts()
print('Buying cost: \n{}'.format(buyingCost))

#4-5
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'],['low','med','high','vhigh'],ordered =True)

#6
import numpy as np
buying_cost_mean = np.mean(car_eval['buying_cost'].cat.codes)

print("buying_cost_mean: {}".format(buying_cost_mean))

#7
print(car_eval.columns)
car_luggage =  car_eval['luggage'].value_counts(normalize=True)
print("car_luggage : {}".format(car_luggage))

#8
after_using_nan = (car_eval['luggage'].value_counts(dropna=False,normalize=True))
print("after_using_nan: {}".format(after_using_nan))

#9 
car_luggage =  car_eval['luggage'].value_counts()/len(car_eval['luggage'])
print("car_luggage : {}".format(car_luggage))







