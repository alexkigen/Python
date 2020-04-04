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
