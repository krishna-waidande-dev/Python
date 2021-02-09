import random

def checkCondition(player1, player2):
    if (player1 == 'Rock' and player2 == 'Scissors'):
        return 1
    elif (player1 == 'Paper' and player2 == 'Rock'):
        return 1
    elif (player1 == 'Scissors' and player2 == 'Paper'):
        return 1
    else:
        return 0

def main():
    flag=''
    player1=''
    player2=''
    name=''
    
    print ('Welcome to Rock, Paper, Scissors Game!!')
    print ('Enter your name:')
    name=input()

    while flag != 'no':  
        print ('Enter your choice (Rock/Paper/Scissors)')
        player1=input()
        
        print ('Your Choice is: ' + player1)

        player2=random.choice(['Rock','Paper','Scissors'])
        print ('Computer Choice is: ' + player2)

        if (player1 == player2):
            print ('Its a tie..No one wins')
            continue
            
        result1=checkCondition(player1, player2)
        result2=checkCondition(player2, player1)

        print ('Result 1: ' + str(result1))
        print ('Result 2: ' + str(result2))

        if result1 == 1:
            print (name +' Wins!! Hurray')
        else:
            print ('Computer wins!!')
        
        print ('Do you want to play again? (yes/no)')
        flag=input()
main()
