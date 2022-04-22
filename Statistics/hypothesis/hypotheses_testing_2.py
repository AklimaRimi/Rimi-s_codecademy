# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
#1

print(lifespans.head())

#2
vein_pack_lifespans = lifespans.lifespan[lifespans.pack=='vein']
print(vein_pack_lifespans.head())

#3
print("mean: {}".format(np.mean(vein_pack_lifespans)))
## mean value(76.1) is greater than 73

#4
from scipy.stats import ttest_1samp
tstat, p_val = ttest_1samp(vein_pack_lifespans,73)
print('vain p_val: {}'.format(p_val))

## null value is false because p_value(5.972157921433082e-07) is much lower than threshold value(.05) again average life is not 73


#6
artery_pack_lifespans = lifespans.lifespan[lifespans.pack=='artery']
print(artery_pack_lifespans.head())

#7
print("artery mean: {}".format(np.mean(artery_pack_lifespans)))

#8

from scipy.stats import ttest_ind

tstat, pval = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)

print('2 category\'s pval: {}'.format(pval))

# The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber. as two pval is same


#10
print(iron.head()) 

#11
Xtab = pd.crosstab(iron.pack,iron.iron)
print(Xtab)

#12

from scipy.stats import chi2_contingency

chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)

# as pval is very lower than 0.05 so alternative hypotheses is true (There is an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.)

