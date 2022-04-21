# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

#2
sns.boxplot(heart['thalach'],heart['heart_disease'])
plt.show()
print(heart['heart_disease'].unique())

#3
thalach_hd = heart.thalach[(heart['heart_disease']=='presence')]
thalach_no_hd = heart.thalach[heart['heart_disease']=='absence']
print(thalach_no_hd)


#4
x = np.mean(thalach_hd)
y = np.mean(thalach_no_hd)
print(abs(x-y))

#5
from scipy.stats import ttest_ind

test,pval = ttest_ind(thalach_no_hd,thalach_hd) #two quantity variable
print(pval)

#6
#two values are significantly difference
# reject the null hypothesis


#7
plt.clf()
sns.boxplot(heart.age,heart.heart_disease)
plt.show()


#8
plt.clf()
sns.boxplot(x = heart.thalach,y=heart.cp)
plt.show()

print(heart.cp.unique())

#9
thalach_typical = heart[heart['cp'] =='typical angina'].thalach
thalach_asymptom = heart[heart['cp'] =='asymptomatic'].thalach
thalach_nonangin = heart[heart['cp'] =='non-anginal pain'].thalach
thalach_atypical = heart[heart['cp'] =='atypical angina'].thalach

#10
from scipy.stats import f_oneway#anova
t, p = f_oneway(thalach_typical,thalach_asymptom,thalach_nonangin,thalach_atypical)## non binary categories
print(p)
# null hypothesis is rejected

#11

from statsmodels.stats.multicomp import pairwise_tukeyhsd
report = pairwise_tukeyhsd(heart.thalach, heart.cp )## quantitative and non binary categorical
print(report)

#asymptomatic   typical angina is not different

#12
Xtab = pd.crosstab(heart.cp, heart.heart_disease)## non binary categorical and binary categorical
print(Xtab)

#13
from scipy.stats import chi2_contingency
chi2,pval,dof,exp = chi2_contingency(Xtab)
print(pval)

##
# there have association between chest pain type and heart disease
##

