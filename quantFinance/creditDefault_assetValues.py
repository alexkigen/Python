#Bernoulli Type default - occurs when assets are lower than a critical threshold, say debt
import math
import random

debtValue = 80000
assetValueStart = 75000
leverage = (debtValue + assetValueStart)/assetValueStart

#assetValue ~ N(0, 1)

#function to generate z score
def z_score(mu, sigma):
    a = random.gauss(mu, sigma)
    return a

#function to project assets
def projection (avStart, riskFree, vol, T):
    
    z = z_score(0,1) #generate NRV
    avEnd = avStart * math.exp(riskFree * T - 0.5*z*vol*vol*T)
    return avEnd

#project asset value

assetValueEnd = projection(assetValueStart, 0.04, 0.2, 1)

print (assetValueEnd)

default = (1 if assetValueEnd < debtValue else 0)

print ("The default event is ", default)

