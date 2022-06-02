import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()
#1
print(aaron_judge.columns)
print(aaron_judge.head())


#2
print(aaron_judge.description)

#3
df = aaron_judge
#4
df['type'] = df['type'].map({'S':1, 'B':0})

#6
print(df['plate_x'])

#7
df = df.dropna(subset = ['plate_x','plate_z','type'])
cleand_df = df[['plate_x','plate_z','type']]
print(cleand_df.head())


#8
plt.scatter(x = 'plate_x',y = 'plate_z',c = 'type',data = cleand_df, cmap = plt.cm.coolwarm, alpha = 0.5)
plt.show()
plt.clf()

#9
x_train,x_test = train_test_split(df,random_state=1)

y_train,y_test = train_test_split(df,random_state=1)

#10
classifier = SVC(kernel = 'rbf')

#11
classifier.fit(x_train[['plate_x','plate_z']],x_train['type'])
#12
draw_boundary(ax,classifier)

#13
print(classifier.score(x_train[['plate_x','plate_z']],x_train['type']))

#14

classifier = SVC(kernel = 'rbf',gamma = 100,C =100)
classifier.fit(x_train[['plate_x','plate_z']],x_train['type'])
print(classifier.score(x_train[['plate_x','plate_z']],x_train['type']))





