import codecademylib3
import pandas as pd

inventory = pd.read_csv('inventory.csv')

#2

print(inventory.head(10))

#3

staten_island = inventory.head(10)

#4
product_request = staten_island ['product_description']

#5
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

#6
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
print(inventory.head())

#7
inventory['total_value'] = inventory['price'] * inventory['quantity']

#8
combine_lambda = lambda row:'{} - {}'.format(row.product_type,row.product_description)

#9

inventory['full_description'] =row.product_type.apply(combine_lambda())


