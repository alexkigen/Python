#demonstrate math operations in python
#initialize some variables

x = 2
xx = 2.5
y = 4
yy = 4.5
yyy = 5.1

print yy/xx #quotient
print yy//xx #floored quotient - lower integer bound; type takes on the types of input


#take x to the power of y

powY = pow(y,x)
powY_ = y**x
print powY, powY_

#remainder of yy/x
print yy%x

dataList = (x, xx, y, yy)
#recall that slicing or subsetting is not inclusive:
print dataList[1:3] #does not include the value of yy and returns 2 items

import math

#exponent and logs
print math.exp(xx)
print math.log(xx)

#as in C++, we can do some operations on a variable without calling it
#this will perform the operation on the incoming value of the variable and return
#a final value in the same variable
val1 = 5
val2 = 3
val1 += 2
print val1

#and, or, not logical operations

print (val1 > val2)
print (val1 > 10 and val1 < 12)
print (val1 == 7 or val2 == 2)
print not(val1 == 7 or val2 == 2) #not reverses result of operation

#in and not in are used to query presence in sequence
print (2.57 in dataList)
print (2.5 in dataList)

#is and is not are used to compare objects (not contents)
dataList2 = dataList
dataList3 = (x, xx, y, yy)

print dataList2 is dataList #same objects - returns True
print dataList3 is dataList #same contents - returns False

