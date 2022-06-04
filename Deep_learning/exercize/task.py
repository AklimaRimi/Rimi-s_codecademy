import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [[0,0],[0,1],[1,0],[1,1]]
label = [0,0,0,1]

plt.clf()
plt.scatter(x = [point[0] for point in data],y = [point[1] for point in data],c = label)

plt.show()

#4
classifier = Perceptron(max_iter = 40)

#5
classifier.fit(data,label)

#6
print(classifier.score(data,label))

#7
data = [[0,0],[0,1],[1,0],[1,1]]
label = [0,1,1,1]
classifier.fit(data,label)
print(classifier.score(data,label))

#9
print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]])
)
#10
x_values = np.linspace(0,1,100)
y_values = np.linspace(0,1,100)

#11
point_grid = list(product(x_values,y_values))

#12
distance = (classifier.decision_function(point_grid))

#13
abs_distance = abs(distance)

#14
distances_matrix = np.reshape(abs_distance,(2,2),-1)


#15 
plt.clf()
heatmap =plt.pcolormesh(x_values,y_values,abs_distance)
plt.colorbar(heatmap)
plt.show()

