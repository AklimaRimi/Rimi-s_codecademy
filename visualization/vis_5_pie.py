import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here

#1
plt.figure(figsize = (10,8))

#2
# plt.pie(num_hardest_reported )

#3
plt.axis('equal')

#4
plt.pie(num_hardest_reported,labels = unit_topics,autopct='%d%%' )

#5
plt.title('Hardest Topics')

#6
plt.savefig('my_pie_chart.png')


plt.show()
