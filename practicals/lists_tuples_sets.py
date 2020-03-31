#demonstrate use of lists, tuples and sets in python

#lists: ordered and changeable
#tuples: ordered and immutable
#sets: unordered and unindexed
#in addition to creation methods shown below, tuple(), list() and set() constructors can be used to create tuples, lists and sets


a = "Rwanda"
b = "Burundi"
c = "Tanzania"
d = "Uganda"
e = "Kenya"
f = "Nigeria"

countryList = [a, b, c, d, e, f]
cpiList = [500, 650, 250, 300, 100, 1000]

print countryList

#as with c++, lists are indexed from 0 and items can be obtained using object[index]

print countryList[4]

#we can also use negative indexing, which starts from the last item in the list

print countryList[-1] #same as
print countryList[4]

#we can also extract ranges of lists

print countryList[1:3] #returns another list with the second and third items; 4th item not included

#if we leave out the start value, the list will pull starting with the first item i.e. start value = 0

print countryList[:3] #same as
print countryList[0:3]

#similarly, we can go to the end of the list by not specifying an ending value

print countryList[2:] #same as
print countryList[2:5]

#we can also use negative ranges to extract starting from the last item

print countryList[-4:-2] #same as
print countryList[1:3]

#we can change items in lists by using indexing

countryList[5] = "Somalia" #remove Nigeria

print countryList

#Loop through a list

for i in cpiList:
    print i*2

#length of a list
print len(cpiList), len(countryList)

#can add an item to a list using the list.append() method
countryList.append("Ethiopia")
cpiList.append(350)

print countryList
print cpiList

#can remove item using the list.remove() or list.pop() method
#remove() requires item being called
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#can remove item using the list.remove() or list.pop() method
#pop() removes using indices. If no index is supplied, removes last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#we can also use the del keyword to remove item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#list.clear() method empties the list

#ways to copy a list:
#1. use list.copy() method
#2. use list2 = list(list1): list() keyword function

#ways to join lists
#1. simply add list1 + list2
#2. append item by item of list2 into list1 using a loop

countryListCopied = list(countryList)

for item in cpiList:
    countryListCopied.append(item)

print countryListCopied

#3. use the list.extend() method
countryListCopied = list(countryList)
countryListCopied.extend(cpiList)
print countryListCopied

#other methods
#NOTE - sort() and reverse() methods do not return an object and work on the original object

countryList.sort() #sort ascending:
print countryList

countryList.sort(reverse = True) #sort descending
print countryList

countryList.reverse() #reverse order - first to last, last to first, etc.
print countryList

#count number of times an item appears in the list
print countryList.count("Kenya")


#TUPLES
#written in round brackets
#immutable - cannot be altered
#most other things work for TUPLES as they do for LISTS e.g. access methods
#alteration methods don't work

countryTuple = (a, b, c, d, e, f)

print countryTuple

#countryTuple[2] = "Nigeria" #error
#countryTuple.sort()         #error

#SETS
#unordered and unindexed
#we cannot access them by indexing
#once a set is created, you cannot modify its items except to add or remove new items
#other operations work on it though, as illustrated below

countrySet = {a, b, c, d, e, f}
countrySet.add("Somalia")
countrySet.remove("Nigeria")

print countrySet

#del function can be used to delete entire sets, lists and/or tuples
del countrySet
del countryTuple
del countryList
