#exception handling in python

#return a user defined run time error in anticipation of error
options = ["Rock", "Paper", "Scissors"]

userInput = input("Enter your choice: Rock, Paper or Scissors ")

if userInput not in options:
    raise RuntimeError("Invalid choice. Please choose Rock, Paper or Scissors")

print (userInput)

#assign system error to a specific error type following operation
import math

try:
    choiceInput = float(input("Enter the number"))
    solution = math.sqrt(choiceInput)
    print (solution)
except:
    print ("Negative number entered")

