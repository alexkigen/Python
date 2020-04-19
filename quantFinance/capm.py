#capm function
def capm (riskFreeRet, marketRet, beta):
    
    stockRet = riskFreeRet + beta * (marketRet - riskFreeRet)

    return stockRet

print (capm(0.02,0.08, 1)) #same return as market due to same systematic risk
print (capm(0.02,0.08, 2.5)) #higher systematic risk means higher expected return

#compute beta
def beta (cor, marketVol, stockVol):

    cov = cor * marketVol * stockVol #covariance

    betaStock = cov/(marketVol**2)

    return betaStock

print (beta(0.5, 0.15, 0.75))
print (capm(0.02, 0.08, beta(0.5, 0.15, 0.75)))
