from sklearn.svm import SVC
from graph import points, labels

classifier = SVC(kernel = 'linear')

classifier.fit(points,labels)

predict = classifier.predict([[3,4],[6,7]])
print(predict)
