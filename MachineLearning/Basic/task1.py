import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())
#2

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

#3

x = prod_per_year['year'].values.reshape(-1,1)

#4
y = prod_per_year['totalprod'].values
#5

plt.scatter(x,y)
#6
from sklearn.linear_model import LinearRegression
regr = LinearRegression()


#7
regr.fit(x,y)

#8
print(regr.coef_ , regr.intercept_)

#9
y_predict = regr.predict(x)

#10

plt.plot(x,y_predict,color='red')


#11
nums = np.array(range(1, 11))
X_future = nums.reshape(-1, 1)


future_predict = regr.predict(X_future)

# plt.plot(X_future,future_predict)
plt.show()



