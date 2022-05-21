import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data

reviews = pd.read_csv('reviews.csv')

 
#print column names
print(reviews.columns)
 
#print .info
print(reviews.info())


#look at the counts of recommended
print(reviews['recommended'].value_counts())
 
#create binary dictionary
from sklearn.preprocessing import LabelEncoder

 
#transform column

reviews['recommended'] = LabelEncoder().fit_transform(reviews['recommended'])
#print your transformed column
print(reviews['recommended'].value_counts())

#look at the counts of rating
print(reviews['rating'].value_counts())
 
#create dictionary
reviews['rating'] = LabelEncoder().fit_transform(reviews['rating'])
 
#transform rating column

 
#print your transformed column values
print(reviews['rating'].value_counts())

#get the number of categories in a feature

 
#perform get_dummies
print(print(reviews['department_name'].value_counts()))
 
#join the new columns back onto the original
one_hot = pd.get_dummies(reviews['department_name'])

#print column names
print(one_hot)

#transform review_date to date-time data

date = pd.to_datetime(reviews['review_date'])
print(date.value_counts())
#print review_date data type 


#get numerical columns
new_reviews = reviews[['clothing_id', 'age', 'recommended', 'rating']]
 
#reset index
new_reviews = new_reviews.set_index('clothing_id')

#instantiate standard scaler
scale = StandardScaler().fit_transform(new_reviews)
 
#fit transform data




