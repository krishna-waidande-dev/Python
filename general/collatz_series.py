import sys

# If num is even then devide it by 2 and return the value.
# If num is odd then print and return 3 * number + 1
# Accept the number from user and then keep calling the collatz function
# until the function returns 1.

def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    else:
        return (number * 3 + 1)
    
def main():
    print ('Enter the number')
    try:
        number = int(input())
    except ValueError:
        print ('Must enter the integer value')
        sys.exit()
            
    while(number > 1):
        number=collatz(number)
        print (number)
main()
