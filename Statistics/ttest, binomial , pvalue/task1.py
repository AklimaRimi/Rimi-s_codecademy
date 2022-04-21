# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

#1
print(heart.head())
chol_hd = yes_hd.chol
print(chol_hd)

#2
print(np.mean(chol_hd)) # heigher than 240

#3
from scipy.stats  import ttest_1samp

tstat,p_val = ttest_1samp(chol_hd,240)

print('p_val: {}'.format(p_val/2))# p_val is .0035 so null value will bw rejected

#5
chol_hd = no_hd.chol
print(chol_hd)

print(np.mean(chol_hd)) # heigher than 240

tstat,p_val = ttest_1samp(chol_hd,240)

print('p_val: {}'.format(p_val/2))# p_val is .26 so null value will be taken

#6
num_patient = len(heart)

#7
print(heart.columns)
num_highfbs_patients = heart['fbs']
print(num_highfbs_patients)


#8
sum_diabetic= np.sum(num_highfbs_patients == '1')
print(sum_diabetic)

#if we take 8% of diabetic patient
sample_size = .08*303
print(sample_size)

#9
from scipy.stats import binom_test
p_value = binom_test(25,303,.08,alternative = 'geater')
print(p_value)#output = 0.55 > 0.05




