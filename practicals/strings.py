#demonstrate strings in python
#can use with double or single quotes
#additional reference https://www.w3schools.com/python/python_ref_string.asp

s = "the dark knight returns"

print s

#a more likely string
multS = """   This is a
multiline string. Comes in handy
for string analysis e.g. twitter feed  """

print multS

#strings are arrays, so we can subset letters as we typically do arrays and lists
print s[0], s[1], s[2], s[3]
print s[3:6]


#length of string
print len(s)
print len(multS)

#remove white space from the beginning or end of strings
print (multS.strip())

#change case
#lower function returns string in all lower case
#upper function returns string in all upper case
s_upper = s.upper()
s_lower = s_upper.lower()

print s_upper
print s_lower

#split function can be used to separate strings by a delimiter such as "," or "."
print multS.split()

#check if a cerain word or letter sequence is in a string
print "string" in multS #check whether "string" is in multS
print "string" not in multS #check whether string is not in multS

#concatenate strings by adding them
newS = s*2 + multS
print newS

#combine strings with integers and numerical data types
#we use curly brackets to specify where we insert the numerics
price = 5.00
quantity = 10
txt = "For only {} dollars each, these coconuts can be yours if you buy {} or more of them"
print(txt.format(price, quantity))
#or
txt = "For only {0} dollars each, these coconuts can be yours if you buy {1} or more of them"
print(txt.format(price, quantity))
