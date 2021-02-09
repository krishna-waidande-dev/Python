import random

inputStr=''
while inputStr != 'no':
    print('Your dice number is:')
    num=random.randrange(1,7)
    print (num)
    if num == 6:
        print ('Wohh!! you got 6')
        continue
    print('Do you wanted to roll dice again? (yes/no)')
    inputStr=input()
