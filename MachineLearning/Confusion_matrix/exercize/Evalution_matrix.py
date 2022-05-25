
from sklearn.metrics import confusion_matrix

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
true_positives = 0
true_negatives = 0
false_positives =0
false_negatives =0

for i in range(len(actual)):
  if actual[i] == predicted[i] and actual[i]==1:
    true_positives+=1
  elif actual[i] == predicted[i] and actual[i]==0:
    true_negatives+=1
  elif actual[i] != predicted[i] and actual[i]==1:
    false_negatives +=1
  else:
    false_positives+=1
print(true_positives,true_negatives,false_positives,false_negatives)

conf_matrix =(confusion_matrix(actual,predicted))
print(conf_matrix)
