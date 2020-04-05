import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv("/Users/Kigen/Documents/r/GSPC.csv")

sp500['LogReturn'] = np.log(sp500['Close']).shift(-1) - np.log(sp500['Close'])

print (sp500['LogReturn'])

#sp500['LogReturn'].plot()

print (sp500.describe())

#sp500['LogReturn'].hist(bins = 50)


#we can use the SCIPY package to get the CDF and PDFs of the distribution of sp500 daily stock returns

from scipy.stats import norm

densityFunc = pd.DataFrame()
densityFunc['x'] = np.arange(-5,5,0.0001)

densityFunc['PDF'] = norm.pdf(densityFunc['x'], 0, 1)
densityFunc['CDF'] = norm.cdf(densityFunc['x'], 0, 1)

#densityFunc[['PDF', 'CDF']].plot()

#plt.plot(densityFunc['x'], densityFunc[['PDF', 'CDF']])


#what is the probability that sp 500 drops more than 40% in a year?

mu = 252 * sp500['LogReturn'].mean()
sigma = (252**0.5) * sp500['LogReturn'].std()

print ("Mean is ", mu, " and std dev is ", sigma)

zScore_40pcDrop = (-0.4 - mu)/sigma #use to read z table

prob_40pcDrop = norm.cdf(-0.4, mu, sigma)

print ("The probability of a 40% drop is ", prob_40pcDrop)

#we can compute value at risk:
#at the 95% CI

VaR95 = norm.ppf(0.05, mu, sigma)

print ("VaR(95) is ", VaR95)
#with probability 5%, the daily return is less than 13%

