def get_gradient_at_b(x,y,m,b):
  diff =0 
  for i in range(len(x)):
    diff += (y[i] - (m*x[i]+b))

  b_gradient = -2/(len(x))*(diff)
  return b_gradient

x = [2, 4 , 6 ,9]

y = [20,10,30,15]

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()

print(get_gradient_at_b(x,y,4,1))
