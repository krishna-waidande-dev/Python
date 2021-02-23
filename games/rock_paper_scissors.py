import random

#All Required Variables.
rock='rock'
scissors='scissors'
paper='paper'
player1=''
player2=''
name=''
totalScore=0

def printGameBanner():
    print("<==========================================>")
    print ('Welcome to Rock, Paper, Scissors Game!!')
    print("<==========================================>")

def takeInputs():
    print ('Enter your choice (Rock/Paper/Scissors)')
    player1=input().lower()
    print ('Your Choice is: ' + player1)

    player2=random.choice([rock, paper, scissors])
    print ('Computer Choice is: ' + player2)
    
    return player1, player2

def isValidInput(player1):
    if (player1 not in (rock, paper, scissors)):
        print('Invalid input or spelling mistake..Please specify correct choice')
        return False
    return True
      
def processInputs(player1, player2, name):
    global totalScore

    if (player1 == player2):
        print ('It\'s a tie..Nobody wins.. Try again..')
        return
 
    result1=checkCondition(player1, player2)
    if (result1 == 1):
        print (name + ' Wins!! Hurray')
        totalScore += 1
    else:
        print ('Computer wins!! Better luck next time :) ')

def checkCondition(player1, player2):
    if (player1 == rock and player2 == scissors):
        return 1
    elif (player1 == paper and player2 == rock):
        return 1
    elif (player1 == scissors and player2 == paper):
        return 1
    else:
        return 0

def main():
    continueGame=''
    printGameBanner()
    print ('Enter your name:')
    name=input()
    while continueGame != 'no':
        player1, player2 = takeInputs()
        if(not(isValidInput(player1))):
            continue
        processInputs(player1, player2, name)
        print ('Do you want to play again? (yes/no)')
        continueGame=input()

    print("Your Total Score is: " + str(totalScore))

main()
