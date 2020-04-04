import math

#execute option pricing code to get optionPrice input (reads from another file)

exec(open("optionPricing.py").read())

#print (callPrice)

def putCallparity(optionPrice, currentVal, strike, riskFree, optionType):
    
    if optionType == "Call":
        
        callPrice = optionPrice
        putPrice = callPrice - currentVal + strike * math.exp(-riskFree * T)
        putPrice = max(putPrice, 0)
        
        return putPrice
    
    else:
        
        putPrice = optionPrice
        callPrice = putPrice + currentVal - strike * math.exp(-riskFree * T)
        callPrice = max(callPrice, 0)


print(putCallparity(callPrice,currentVal, strike, riskFree, "Call"))
