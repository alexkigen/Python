
#simple algorithm to integrate Y = a + b*X^c

def integrate (a, b, c, lowerX, upperX, divisions):

    interval = ((upperX - lowerX)/divisions)
    x = lowerX - interval/2
    area = 0

    for div in range(divisions):
        x += interval

        height = a + b*((x)**c)
        area += interval * height
    
    return area


print ("Partition Method Ans: ", integrate(0, 1, 2, 2, 4, 10000)) #test
print ("Closed Form Ans: " , 56/3)
print ("Partition Method Ans: ", integrate(2, 2, 2, 2, 4, 10000)) #test with intercepts
print ("Closed Form Ans: ", (8+(128/3))-(4+(16/3)))
print ("Partition Method Ans: ", integrate(0, 1, 2, -2, 2, 10000)) #test negative bounds
print ("Closed Form Ans: " , 16/3)
print ("Partition Method Ans: ", integrate(0, 1, 3, 2, 4, 10)) #test higher power
print ("Closed Form Ans: " , 60)
