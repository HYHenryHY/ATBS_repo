#Coin Flip Streaks
#'H' = heads = 0
#'T' = tails = 1

import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    #Code that creates a list of 100 'heads' or 'tails' values
    listOf100=[]
    for flips in range(100):
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            listOf100.append('H')
        else:
            listOf100.append('T')
    

    #Code that checks if there is a streak of 6 heads or tails in a row
    startI=0 #start index
    endI=6 #end index
    for check in range(100):
        checkList=listOf100[startI:endI]
        if checkList == ['H','H','H','H','H','H'] or checkList == ['T','T','T','T','T','T']:
            numberOfStreaks += 1
        else:
            continue
        startI += 1
        endI +=1
    
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks/100))
