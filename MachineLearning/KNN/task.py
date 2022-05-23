import codecademylib3_seaborn

#1
from sklearn.datasets import load_breast_cancer

breast_cancer_data = load_breast_cancer()


#2
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

#3
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

#4
from sklearn.model_selection import train_test_split

#5-6-7
training_data,validation_data,training_labels,validation_labels = train_test_split(breast_cancer_data.data,breast_cancer_data.target,test_size = .2,random_state = 42)

#8-9

from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(3)

#10
classifier.fit(training_data,training_labels)

#11
print(classifier.score(validation_data,validation_labels))

bestk = 0
acc = 0
x_axis =[]
y_axis =[]
#12-14
import matplotlib.pyplot as plt
for k in range(1,101):
  classifier = KNeighborsClassifier(k)
  classifier.fit(training_data,training_labels)

  score =classifier.score(validation_data,validation_labels)
  x_axis.append(k)
  y_axis.append(score)
  if acc<score:
    acc = score
    bestk = k

print('best K :'+str(bestk)+' accuracy : '+str(acc))

#16
plt.plot(x_axis,y_axis)
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.title('Breast Cancer Classifier Accuracy"')
plt.grid()
plt.show()


