import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
#1
print(financial_data.head())

#2
month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

#3
plt.plot(month,revenue)


#4

plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
#5
plt.plot(month,expenses)


plt.xlabel('Month')
plt.ylabel('Expenses ($)')
plt.title('expence')

#plt.clf()
plt.show()

#6
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))


#7
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

#8
plt.pie(proportions,labels =expense_categories)
plt.show()

#10

value = expense_overview[expense_overview['Proportion']<.05]['Proportion']
print(value)
sum= 0
for i in value:
  sum += i
print(sum)
proportion_update = expense_overview[expense_overview['Proportion']>.05]
proportion_update.loc[len(proportion_update.index)] = ['other',sum]
print(proportion_update)

#11
labels = list(proportion_update['Expense'].unique())

plt.pie(proportion_update['Proportion'],labels=labels)
plt.show()

#12
expense_cut = 'Salaries'
employees = pd.read_csv('employees.csv')
print(employees.head())

#13
sorted_data = employees.sort_values(by=['Productivity'])
print(sorted_data)

#14
employees_cut =sorted_data[:100]

#15
transformation = 'standardization'

#16
commute_times =employees['Commute Time']

#17
print(commute_times.describe())

plt.clf()
plt.hist(commute_times)
plt.show()
#19
commute_times_log = np.log(commute_times)
plt.clf()
plt.hist(commute_times_log)
plt.show()

#20
from sklearn.preprocessing import StandardScaler
st =StandardScaler()
value = st.fit_transform(employees[['Commute Time']])

plt.clf()
plt.hist(value)
plt.show()
