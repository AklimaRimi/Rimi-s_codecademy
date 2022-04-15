import codecademylib3
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')

#1
print(ad_clicks.head())

#2
x = ad_clicks.groupby('utm_source').user_id.count()
print(x)

#3
ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].apply(lambda x: False if x is np.nan else True)
print(ad_clicks)

#4
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

#5
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id',
).reset_index()
print(clicks_pivot)

#6
clicks_pivot['percent_clicked'] = clicks_pivot[True]*100/(clicks_pivot[True]+clicks_pivot[False])



#7
x = ad_clicks.groupby(['is_click','experimental_group']).user_id.count()
print('A or B')
print(x)


#8

a_clicks = ad_clicks[ad_clicks.experimental_group =='A']
b_clicks = ad_clicks[ad_clicks.experimental_group =='B']


#9
a_day_click = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()

print(a_day_click)
a_pivot = a_day_click.pivot(
  columns ='is_click',
  index = 'day',
  values = 'user_id',
).reset_index()
print(a_pivot)

