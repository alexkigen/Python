#we can use the sympy module to express symbolic functions
#can also use it to integrate

import sympy as sp

x = sp.Symbol('x')

print (sp.integrate(3.0*(x**2) + 1, x))

print (x)
              

#use SCIPY

from scipy.integrate import quad

def f(x):
    
    return 3.0*(x**2) + 1


print (f(2))

soln, error = quad(f, 0, 2)

print ("Solution is: ", soln)
print ("Error is: ", error)

import numpy as np

def function(x):
    
    return np.exp(-x) * np.sin(3.0*x)

print (function(2))

soln2, error2 = quad(function, 0, 2*np.pi)

print ("Solution 2 is: ", soln2)
print ("Error 2 is: ", error2)
