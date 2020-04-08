#sampling and inference
import pandas as pd
import numpy as np

population = pd.DataFrame()

population['pop'] = [12, 1, 67, 20, 34, 32, 8, 55, 53, 0, 44, 12, 3, 4]

#sort values

population = population.sort_values(by = 'pop')

print (population)
 

#use the sample function to sample from the dataframe
segment_woReplace = population['pop'].sample(5, replace = False)
segment_wReplace = population['pop'].sample(5, replace = True)


print (segment_woReplace)
print (segment_wReplace)

#use the iloc function to get specific item
for i in range(5):
    print (segment_wReplace.iloc[i])
    


segment = population['pop'].sample(1000, replace = True)

print (segment.head(), segment.tail())

print(population.describe())

#sample 5 items from population 10 times

segment_1000 = [population['pop'].sample(5, replace = True) for i in range(10)]

#can access the different samples using [x]: for example
print (segment_1000[9])
print ("mean is ", segment_1000[9].mean(), "var is ", segment_1000[9].var())

#sampling from a normal distribution

normSamples = pd.DataFrame(np.random.normal(0,1,10))

print (normSamples)

meanList = []
varList = []

for i in range(1000):
    sample = pd.DataFrame(np.random.normal(0,1,50))
    meanList.append(sample[0].mean())
    varList.append(sample[0].var(ddof = 1))

collection = pd.DataFrame()

collection['meanList'] = meanList

collection['meanList'].hist(bins = 500)

#confidence interval at 90th percentile level

z_left = norm.ppf(0.05)
z_right = norm.ppf(0.95)

print (z_left, z_right)

mean = np.mean(meanList)
std_dev = np.std(meanList)

upperCI = mean + z_right*std_dev
lowerCI = mean + z_left*std_dev

print ("Confidence Interval is ", lowerCI, " to ", upperCI)
