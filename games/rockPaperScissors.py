#Rock Paper Scissors Game
import random

def playGame ():
    options = ["Rock", "Paper", "Scissors"]
    
    goAgain = True
    outcome = "Not Played"
    
    compPlay = "Dummy"
    
    #engine
    while goAgain == True:
        
        #inputs
        compPlay = random.choice(options)
        userInput = input("Enter your choice: Rock, Paper or Scissors?")
        
        if userInput not in options:
            Error = str(userInput) + " is not a valid entry. Go again!"
            outcome = Error
            print (outcome)
            goAgain = True
        
        elif userInput == compPlay:
            outcome = "That's a draw. Go Again!"
            print (outcome)
            goAgain = True
        
        
        elif userInput == "Rock":
            if compPlay == "Paper":
                outcome = "Computer Wins!"
            if compPlay == "Scissors":
                outcome = "You Win!"
            goAgain = False
    
        elif userInput == "Paper":
            if compPlay == "Rock":
                outcome = "You Win!"
            if compPlay == "Scissors":
                outcome = "Computer Wins!"
            goAgain = False
            
        elif userInput == "Scissors":
            if compPlay == "Rock":
                outcome = "Computer Wins!"
            if compPlay == "Paper":
                outcome = "You Win!"
            goAgain = False
        
        #output
    print ("Computer chose: ", compPlay)
    print (outcome)


playGame()
