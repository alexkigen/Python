#demonstrates number types: integers, floats and complex
#demonstrates randomization and random number generation

x = 24    # int
y = 24.5  # float
z = 24.5j   # complex

#store in a tuple
dataTuple = (x, y, z) #a tuple is imply an immutable list
dataList = (x, y, z)
dataSet = frozenset(dataTuple)

print "The data tuple is: ", dataTuple
print "The data list is: ", dataList
print "The data is: ", dataSet

#increases length of a tuple or list by a constant
print dataTuple * 2 
print dataList * 2
#wouldn't work for sets or frozen sets

#we can convert from one type to another

xx = float(x) #adds a decimal point
yy = int(y)  #basically truncates
zz = complex(y)

print (xx, yy, zz)

#we can also work with random numbers
#to do this, we need to import the random module

import random
import math #for exp function

mu = 0.05
sigma = 0.15

muLog = math.exp(mu + 0.5*(sigma**2))
sigmaLog = math.exp(2*mu + (sigma**2))*(math.exp(sigma**2)-1)

print muLog, sigmaLog

randUnifInteger = random.randint(0,10)
randUnifFloat = random.uniform(0,1)

#random number from a sequence, say the data list created above
randSeq = random.choice(dataList)

#random number from a normal distribution
randStdNorm = random.gauss(0,1) #standard normal
randNorm = random.gauss(mu,sigma)
randLogNorm = random.lognormvariate(muLog, sigmaLog)

print "Uniform Random Integer: ", randUnifInteger
print "Uniform Random Number: ", randUnifFloat
print "Randomize from dataList: ", randSeq
print "Standard normal random number: ",randStdNorm
print "Normal random number: ", randNorm
print "Lognormal random number: ", randLogNorm
