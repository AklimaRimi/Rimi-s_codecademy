# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qJuYCdq-h10INBhVTvwa1g0WkRgrOZpW
"""

import csv 
import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/New folder/insurance.csv')

data

data.age.mean()

data.age.hist()

data.smoker.hist()

children = data[data['children']>1]
children['age'].mean()