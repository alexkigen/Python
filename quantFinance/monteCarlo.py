import random
import math


#function to generate a random z
def z_score(mu, sigma):
    a = random.gauss(mu, sigma)
    return a

def payOff (currentVal, strike, T, vol, riskFree):
    
    z = z_score(0, 1)
    
    futureVal = currentVal * math.exp(riskFree * T - 0.5 * vol * vol * T * z)
    
    payoff = futureVal - strike
    
    return payoff

def OptionPrice (currentVal, strike, T, vol, riskFree, noRuns):
    
    rollingPayoffSum = 0
    for i in range(noRuns):
        payoff = payOff(currentVal, strike, T, vol, riskFree)
        rollingPayoffSum += payoff
    
    optionPrice = rollingPayoffSum/noRuns
    
    return optionPrice, rollingPayoffSum

#define inputs
currentVal = 100
riskyReturn = 0.07
riskFree = 0.04
strike = 100
vol = 0.15
T = 0.5

callPrice = OptionPrice(currentVal, strike, T, vol, riskFree, 10000)[0]
putPrice = callPrice + strike * math.exp(-riskFree * T) - currentVal

print ("Call ption price is " + str(callPrice))
print ("Put option price is " + str(putPrice))


#suppose we anticipate this stock to grow at an annual rate of 5% (risk world)
#if we went long a call option:
expectedVal = currentVal * math.exp(riskyReturn * T)

profit = expectedVal - strike - callPrice
leverage = profit/callPrice

print ("profit is " + str(profit))
print ("'leverage' is " + str(leverage))
