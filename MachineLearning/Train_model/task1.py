import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())

outcomes = df[['Wins','Losses','Winnings','Ranking']]





# perform exploratory analysis here:
print(df.shape)


# plt.scatter(df['FirstServe'],df['Wins'])
# plt.show()

plt.clf()
plt.scatter(df['FirstServePointsWon'],df['Wins'])
plt.show()


## perform single feature linear regressions here:
li = ['Aces','DoubleFaults','FirstServe','FirstServePointsWon','SecondServePointsWon',
'BreakPointsFaced','BreakPointsSaved','ServiceGamesPlayed','ServiceGamesWon','TotalServicePointsWon']

best = 'x'
max_score = 0
for i in li:
  feature = df[[i]]
  outcome = df['Wins']

  x_train,x_test,y_train,y_test  = train_test_split(feature,outcome)

  lr = LinearRegression()
  lr.fit(x_train,y_train)
  x = lr.score(x_test,y_test)
  if x>max_score:
    max_score = x
    best = i

print('best Feature: '+str(best)+ ' For win\nbest Score : '+str(max_score))


best = 'x'
max_score = 0
for i in li:
  feature = df[[i]]
  outcome = df['Losses']

  x_train,x_test,y_train,y_test  = train_test_split(feature,outcome)

  lr = LinearRegression()
  lr.fit(x_train,y_train)
  x = lr.score(x_test,y_test)
  if x>max_score:
    max_score = x
    best = i

print('best Feature: '+str(best)+ ' For Losses\nbest Score : '+str(max_score))


best = 'x'
max_score = 0
for i in li:
  feature = df[[i]]
  outcome = df['Winnings']

  x_train,x_test,y_train,y_test  = train_test_split(feature,outcome)

  lr = LinearRegression()
  lr.fit(x_train,y_train)
  x = lr.score(x_test,y_test)
  if x>max_score:
    max_score = x
    best = i

print('best Feature: '+str(best)+ ' For Winnings\nbest Score : '+str(max_score))


best = 'x'
max_score = 0
for i in li:
  feature = df[[i]]
  outcome = df['Ranking']

  x_train,x_test,y_train,y_test  = train_test_split(feature,outcome)

  lr = LinearRegression()
  lr.fit(x_train,y_train)
  x = lr.score(x_test,y_test)
  if x>max_score:
    max_score = x
    best = i

print('best Feature: '+str(best)+ ' For: Rankings\nbest Score : '+str(max_score))


## perform two feature linear regressions here:

features = df[[
'ServiceGamesPlayed','ServiceGamesWon']]
outcome = df[['Winnings']]

x_train,y_train,x_test,y_test = train_test_split(features,outcome)

lr = LinearRegression()
lr.fit(x_train,x_test)

print(lr.score(y_train,y_test))



## perform multiple feature linear regressions here:

features = df[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon',
'SecondServePointsWon','SecondServeReturnPointsWon','Aces',
'BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities',
'BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon',
'ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon',
'TotalServicePointsWon']]
outcome = df[['Winnings']]


x_train,y_train,x_test,y_test = train_test_split(features,outcome)

lr = LinearRegression()
lr.fit(x_train,x_test)

print(lr.score(y_train,y_test))

