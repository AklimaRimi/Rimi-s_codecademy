x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

y_predicted1 = [m1*xi+b1 for xi in x]

#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2*xi+b2 for xi in x]

total_loss1 =0 
for i in range(len(y)):
  total_loss1 += (y[i]-y_predicted1[i])**2


total_loss2 =0 
for i in range(len(y)):
  total_loss2 += (y[i]-y_predicted2[i])**2


print(total_loss1,total_loss2)

better_fit = 2
