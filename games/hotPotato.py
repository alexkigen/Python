#implement hot potato game

numberOfPlayers = int(input("Enter the number of Players: "))

playerNames = list(range(numberOfPlayers))

for i in range(numberOfPlayers):
    print ("Player ", i+1 ,", enter your name")
    playerNames[i] = input("Player name: ")

print ("Player names and orders are as follows: ", playerNames)

#hot potato engine:

#method A - base Python
time = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

import random
import math
countRemain = len(playerNames)
playersLeft = playerNames

print ("Starting players: ", playersLeft)

while countRemain > 1:
    chosen = random.choice(time)
    #print (chosen)
    group = math.ceil(chosen/len(playersLeft))
    #print (group)
    losingPlayerIndex = chosen - ((group-1)*len(playersLeft)) - 1
    #print (losingPlayerIndex)
    losingPlayer = playersLeft[losingPlayerIndex]
    playersLeft.remove(losingPlayer)
    print ("Player out: ", losingPlayer)
    print ("Players left: ", playersLeft)
    countRemain -= 1
