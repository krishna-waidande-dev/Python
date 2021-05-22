rows=int(input("How many rows you wanted to print??? "))
i=0
rowList=[]

while( i < rows ):
    innerList=[]

    #Inserts first 1 into row.
    if (len(innerList) == 0):
        innerList.append(1)

    #Inserts middle calculated numbers into row.
    if (len(rowList) != 0 and i >= 2):
        temp=rowList[i-1]
        j=1
        while( j < i):
            innerList.append(temp[j-1] + temp[j])
            j+=1

    #Inserts last 1 into row.
    if(len(innerList) != 0 and i != 0 ):
        innerList.append(1)

    rowList.append(innerList)
    
    #Printing the output in formatted manner.
    outputString=""
    for element in innerList:
        outputString+=str(element)+' '
    print(' ' * (rows-i) + str(outputString) + ' ' * (rows-i))
    
    i+=1
    
#Output:
    
# How many rows you wanted to print???5
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
