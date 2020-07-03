# Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
# Extras:
# 1. Randomly generate two lists to test this.
# 2. Write this in one line of Python. (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

sizeFirst=random.randrange(1,20)
sizeSecond=random.randrange(1,20)

firstList=random.sample(range(10, 50), sizeFirst)
secondList=random.sample(range(10, 50), sizeSecond)                       
common=[]

print ('First random list is:')
print(firstList)
print ('Second random list is:')
print(secondList)
                         
def getCommon(list1, list2, listSize):
    for i in (range(listSize)):
        if list1[i] in list2:
            if list1[i] not in common:
                common.append(list1[i])           
    print ('List overlap:')
    print(common)

def main():
    if sizeFirst < sizeSecond:
        getCommon(firstList, secondList, sizeFirst)
    else:
        getCommon(secondList, firstList, sizeSecond)

main()
