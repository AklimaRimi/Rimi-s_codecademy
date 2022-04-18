import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#1
print(data.head())

#2
life = data['Life Expectancy']

#3
life_expectancy_quartiles = np.quantile(life,[.25,.5,.75])

plt.hist(life)
plt.show()

#4
print(life_expectancy_quartiles)

#7
gdp = data['GDP']
print(np.median(gdp))
print(np.quantile(gdp,.5))

#8
low_gdp = data[data['GDP'] <= np.quantile(gdp,.5)]

#9

low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [.25, .5,.75])

#10

high_gdp = data[data['GDP'] > np.quantile(gdp,.5)]


#11
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()








