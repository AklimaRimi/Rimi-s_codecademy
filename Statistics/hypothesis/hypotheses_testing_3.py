# Import libraries
import numpy as np
import pandas as pd
import codecademylib3

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

#1
print(dogs.head())

#2
whippet_rescue = dogs.is_rescue[dogs['breed']=='whippet']
print(whippet_rescue.head())

#3
num_whippet_rescues = np.sum(whippet_rescue== 1)
print("rescued:  {}".format(num_whippet_rescues))

#4
num_whippets = len(whippet_rescue)

#5
from scipy.stats import binom_test
p_val = binom_test(len(whippet_rescue),num_whippets,.08)
print(p_val)


#6
wt_whippets = dogs.weight[dogs['breed'] =='whippet']
wt_terriers = dogs.weight[dogs['breed'] == 'terrier']
wt_pitbulls = dogs.weight[dogs['breed'] == 'pitbull']


#7
from scipy.stats import f_oneway

f_stat , pval = f_oneway(wt_whippets,wt_terriers,wt_pitbulls)
print(pval)

## Alternative: whippets, terriers, and pitbulls do not all weigh the same amount on average (at least one pair of breeds has differing average weights) is true


print(dogs_wtp)

#9

print(dogs_ps)

Xtab = pd.crosstab(dogs_ps.breed,dogs_ps.color)
print(Xtab)

#10

from scipy.stats import chi2_contingency
chi,pval,dof,exp = chi2_contingency(Xtab)
print(pval)

#so as pvalue is 0.005302408293244597 so we can reject null value and 
#Alternatively There is not an association between breed (poodle vs. shihtzu) and color.




