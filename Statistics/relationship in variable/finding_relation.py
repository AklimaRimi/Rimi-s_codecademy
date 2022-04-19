import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#1
knicks_pts = nba_2010[nba_2010['fran_id']=='Knicks']['pts']
nets_pts =nba_2010[nba_2010['fran_id']=='Nets']['pts']

#2
print(np.mean(knicks_pts) - np.mean(nets_pts))

#3
plt.hist(knicks_pts,alpha=.5,label='knick')
plt.hist(nets_pts,alpha=.5,label =' nets')
plt.legend()
plt.show()

#4
knicks_pts = nba_2014[nba_2014['fran_id']=='Knicks']['pts']
nets_pts =nba_2014[nba_2014['fran_id']=='Nets']['pts']


print(np.mean(knicks_pts) - np.mean(nets_pts))

plt.clf()
plt.hist(knicks_pts,alpha=.5,label='knick')
plt.hist(nets_pts,alpha=.5,label =' nets')
plt.legend()
plt.show()

#5
plt.clf()
sns.boxplot(data = nba_2010,x = 'pts',y = 'fran_id')
plt.show()


#6
location_result_freq = pd.crosstab(nba_2010.game_result,nba_2010.game_location)
print(location_result_freq)

#7
print(location_result_freq/len(nba_2010))

#8
chi,pval,dof,ex = chi2_contingency(location_result_freq)

print(chi)

#9
point_div = np.cov(nba_2010.forecast,nba_2010.point_diff)
print(point_div)

#10
corrrelationss = pearsonr(nba_2010.forecast,nba_2010.point_diff)
print(corrrelationss)



#11
plt.clf()
plt.scatter(nba_2010.forecast,nba_2010.point_diff)
plt.show()

#they have positive corelation

