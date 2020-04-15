#program to check if a string is a palindrome

def palindrome(x):
    reversedString = x[::-1] ##define own reversal
    reversedString = ''.join(reversed(x)) ##user predefined function

    isPalindrome = False
    if x == reversedString:
        isPalindrome = True
    else:
        isPalindrome = False
    
    return isPalindrome

print (palindrome('pull'))
print (palindrome('racecar'))
print (palindrome('madam'))
print (palindrome('amanaplanacanalpanama'))


#test on a phrase. First, we can clear out whitespace, set case uniformly
phrase = 'A man a plan a canal Panama'
phraseClean = phrase.replace(" ", "").lower() #clear out whitespace and lower caps for comparison basis
print (palindrome(phraseClean)) #then apply palindrome function
