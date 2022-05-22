import codecademylib3_seaborn
import pandas as pd

# import train_test_split
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df.drop('rent',axis=1)
y = df['rent']

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=6)
print(y_train)
