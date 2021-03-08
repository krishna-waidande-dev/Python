#Write a program which will accept a number which will be provided to the power of 2.
#Once 2's power is calculated do the addition of those digits and continue process
#Until the sum of digit comes to single digit value.
#
#Enter the number power number:
#6
#6 to the power 2 is : 64
#The Sum is 1
#
# Here 6 + 4 is 10 and again 1 + 0  is 1 so answer is 1.

import math

user_input=input("Enter the number power number:\n")
power = pow(2, int(user_input))
sum=0

print(str(user_input) + " to the power 2 is : " + str(power))

while True:
    if int(user_input) == 1:
        sum = 2
        break

    sum = (int(power) % 10) + sum
    power = int(power / 10)
    
    if len(str(power)) == 1:
       sum = sum + power
       if len(str(sum)) > 1:
           power = sum
           sum = 0
           continue
       break
   
print("The Sum is " + str(sum))