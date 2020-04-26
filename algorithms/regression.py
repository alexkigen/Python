#regression using scipy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("http://apmonitor.com/che263/uploads/Main/stats_data.txt")

print (data.head())

print ("Variance of x: ", data['x'].var())
print ("Variance of y: ", data['y'].var()) #unbiased

np.var(data['y']) #is biased



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("http://apmonitor.com/che263/uploads/Main/stats_data.txt")

print (data.head())

print ("Variance of x: ", data['x'].var())
print ("Variance of y: ", data['y'].var()) #unbiased

np.var(data['y']) #is biased


from scipy.optimize import curve_fit

#fit a linear model
def f(x, a, b):
    return (a * x + b)

model = curve_fit(f, data['x'], data['y'])

parameters, covarianceMat = model
parameters = list((parameters[1], parameters[0]))

print ("The parameters are: ", parameters)
print ("The covariance matrix is: ", covarianceMat)

#analyze model fit
y = data['y']
x = data['x']
n = len(x)
a = parameters[1]
b = parameters[0]

R2 = 1.0-sum((y - f(x, a, b))**2)/((n-1)*y.var()) #1-unexplained variance

print ("R-Squared is: ", R2)


#plot data
plt.scatter(x, y, s = 10, label = 'Data')




#fit a linear model
def f(x, a, b):
    return (a * x + b)

model = curve_fit(f, data['x'], data['y'])

parameters, covarianceMat = model
parameters = list((parameters[1], parameters[0]))

print ("The parameters are: ", parameters)
print ("The covariance matrix is: ", covarianceMat)

#analyze model fit
y = data['y']
x = data['x']
n = len(x)
a = parameters[1]
b = parameters[0]

R2 = 1.0-sum((y - f(x, a, b))**2)/((n-1)*y.var()) #1-unexplained variance

print ("R-Squared is: ", R2)


#plot data
plt.scatter(x, y, s = 10, label = 'Data')



