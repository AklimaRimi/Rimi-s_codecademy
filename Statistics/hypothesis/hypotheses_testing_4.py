# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')


#1
print(abdata.head())

#2
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

#3
from scipy.stats import chi2_contingency
chi,pval,dof,exp = chi2_contingency(Xtab)
print(pval)


#4
num_visits = len(abdata)
print(num_visits)

#5

num_sales_needed_099 =1000/.99


#6
p_sales_needed_099 =num_sales_needed_099/num_visits
print(p_sales_needed_099)

#7
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 =num_sales_needed_199/num_visits
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 =num_sales_needed_499/num_visits


print(num_sales_needed_199)

#8
from scipy.stats import binom_test
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

#9
samp_size_199 =  np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499 =  np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

#10
pvalA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print('P value for A: {}'.format(pvalA))

#11
pvalB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print('P value for B: {}'.format(pvalB))

#12
pvalC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print('P value for C: {}'.format(pvalC))

# P value for A: 0.9028081076188985
# P value for B: 0.11184562623739903
# P value for C: 0.027944826659907135
#so C group puchase rate is higher than any other group



