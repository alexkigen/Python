import math

#execute option pricing code to get optionPrice input

exec(open("optionPricing.py").read())

#print (callPrice)

def putCallparity(optionPrice, currentVal, strike, riskFree, optionType):
    
    if optionType == "Call":
        
        callPrice = optionPrice
        putPrice = callPrice - currentVal + strike * math.exp(-riskFree * T)
        putPrice = round(max(putPrice, 0),4)
        optionReturn = "Put"
        
        return optionReturn, putPrice
    
    else:
        
        putPrice = optionPrice
        callPrice = putPrice + currentVal - strike * math.exp(-riskFree * T)
        callPrice = round(max(callPrice, 0),4)
        optionReturn = "Call"

        return optionReturn, callPrice


parityPrice = putCallparity(callPrice,currentVal, strike, riskFree, "Call")

print (callPrice)
print (parityPrice) #displays the option type (if call supplied then put displayed) and price

