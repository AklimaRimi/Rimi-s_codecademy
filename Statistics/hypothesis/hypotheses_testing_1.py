import noshmishmosh

#2
import numpy as np

#3
baseline =.5
lift = .3
significance =.10

#4
all_visitors = noshmishmosh.customer_visits
print(all_visitors)

#5
paying_visitors = noshmishmosh.purchasing_customers
print(paying_visitors)

#6
total = len(all_visitors)
pay = len(paying_visitors)

#7
baseline_percent = (total/pay)*100
print('baseline: {}'.format(baseline_percent))

#8
payment_history = noshmishmosh.money_spent
print(payment_history)

#10

average_payment = np.mean(payment_history)
print(average_payment)

#11
new_customers_needed = np.ceil(1240/average_payment)

#12
percentage_point_increase = (new_customers_needed/total)*100

print(percentage_point_increase)
#13

mde = (percentage_point_increase /baseline_percent)*100

print(mde)
