import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#1
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase)

#2 
visit_and_cart = visits.merge(cart,how='left')

print(visit_and_cart.head())
print(len(visit_and_cart))

#4
import numpy as np
print('nan values are: ')
print(len(visit_and_cart[visit_and_cart['cart_time'].isnull()]))

#4
print('nan values are: ')
print(len(visit_and_cart[visit_and_cart['cart_time'].isnull()])/int(len(visit_and_cart)))

#6

cart_and_check = cart.merge(checkout,how='left')
print(cart_and_check)

print('nan values are: ')
print(len(cart_and_check[cart_and_check['checkout_time'].isnull()]))

print('nan values are: ')
print(len(cart_and_check[cart_and_check['checkout_time'].isnull()])/int(len(cart_and_check)))


#7
all_data = cart.merge(visits).merge(checkout)
print(all_data)

all_data['purchase_time'] = all_data['cart_time'] - all_data['visit_time']


print(all_data)

print('average time: {}'.format(all_data['purchase_time'].mean()))



