import random
print ('This game is guess the number')
print ('Try to guess the number in 5 attempts')
print ('I am thinking number between 1 to 20')

secretNum = random.randint(1,21)

for guessNum in range (1,6):
       print ('Your guess is')
       userNum = int(input())

       if userNum < secretNum:
         print ('Your guess is low. Take a guess')
       elif userNum > secretNum:
           print ('Your guess is high. Take a guess')
       else:
           break
        
if secretNum == userNum:
    print ('Nice! You guessed the right number in ' + str(guessNum) + 'guesses')
else:
    print ('Nope. The number was:' + str(secretNum))
