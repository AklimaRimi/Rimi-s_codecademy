def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

#2
df = pd.read_csv('income.csv',header = 0,delimiter =', ')
# print(df.head())

#3

print(df.iloc[0])

#5
label = df[['income']]

#6
features = df[['age','capital-gain','capital-loss','hours-per-week','sex']]
#12
features['sex'] = features['sex'].map({'Male':1,'Female':2})
print(features.head())

#7
train_data,test_data,train_labels,test_labels = train_test_split(features,label,random_state = 1)

#8
forest = RandomForestClassifier(random_state = 1)

#9
forest.fit(train_data,train_labels)



#11
print(forest.score(test_data,test_labels))

#14
print(df['native-country'].value_counts())

#15
df['native-country'] = df['native-country'].apply(lambda x: 0 if x =='United-States' else (2 if x=='Germany' else 3))
print(df['native-country'].value_counts())

#16
features['country-int'] = df['native-country'] 
print(features.head())

#17

forest = RandomForestClassifier()
forest.fit(features,label)

print(forest.feature_importances_)
print(forest.score(features,label))


