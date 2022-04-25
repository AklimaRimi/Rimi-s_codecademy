import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#2
df = pd.read_csv('WorldCupMatches.csv')
#3 4
print(df.head())

#5

df['Total Goal'] = df['Home Team Goals'] + df['Away Team Goals']

#6 7

sns.set_style('whitegrid')
sns.set_context('poster' , font_scale=.8)

sns.barplot(data=df, x ='Year',y = 'Total Goal')
plt.show()
plt.clf()

# 8
f, ax = plt.subplots(figsize = (12,7))
#9
sns.barplot(data = df,x = 'Year', y ='Total Goal')



#10 11
ax.set_title('Year vs Goal')

plt.show()
plt.clf()


#12

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

#13
sns.set_context('notebook', font_scale = 1.25)

#14

f, ax2  = plt.subplots(figsize = (12,7))

sns.boxplot(data = df_goals,x = 'year',y = 'goals')
#15
ax2.set_title('Year vs Goal')

plt.show()







