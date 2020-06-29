import random
import re
import sys

movieNames = ['HarryPotter', 'Friends', 'HowIMetYourMother','GameOfThrones','ShadowHunters','BigBankTheory']
choice = random.choice(movieNames)
choice.lower()
guess=[]
print ('It is ' + str(len(choice) + 1) + ' letters word')

def initializeBlankValues():
    i=0
    while (i < len(choice)):
        guess.append('_')
        i=i+1

    print (guess)

def checkLetter(letter):
    pos = [m.start() for m in re.finditer(letter,choice)]
        
    j=0
    while (j < len(pos)):
        guess[pos[j]]=letter
        j=j+1

def checkGuess(letter):
    if (letter == choice):
        print ('You guessed the movie/series correct')
        sys.exit()
        
    if ( not '_' in guess):
        print ('You guessed the movie correct:' + choice)
        sys.exit()

def guessMovie():
    i=0
    while (i < len(choice)):
        letter = input('Enter the letter:')
        letter.lower()
        checkLetter(letter)
        checkGuess(letter)
        i=i+1
        print (guess)
    
def main():
    initializeBlankValues()
    guessMovie()

    if ( '_' in guess):
        print ('Opps!!..Could not guess movie name. Better luck next time')


main()
