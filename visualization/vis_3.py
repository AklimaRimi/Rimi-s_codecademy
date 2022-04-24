import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom,Cs)
f_bottom = np.add(d_bottom,Ds)

#create your plot here
#2
plt.figure(figsize = (10,8))

#3
plt.bar(x,As)
plt.bar(x,Bs,bottom=As)
plt.bar(x,Cs,bottom = Bs)
plt.bar(x,Ds,bottom = Cs)
plt.bar(x,Fs,bottom = Ds)

#4
ax = plt.subplot()
#5
ax.set_xticks(range(len(unit_topics)))

#6
ax.set_xticklabels(unit_topics)

#7
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')



#8
plt.savefig('my_stacked_bar.png')



plt.show()
