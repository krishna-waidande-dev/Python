# Table Printer
# Write a function named printTable() that takes a list of lists of strings and
# displays it in a well-organized table with Each column right-justified. Assume
# that all the inner lists will contain the same number of strings

# Expected output:
#   apples  Alice    dogs
#  oranges    Bob    cats
# cherries  Carol   moose
#   banana  David   goose


tableData = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

columnWidth=[]
columnSize=len(tableData)
rowSize=len(tableData[0])

"""
This funciton is used to find the longest string in each of the inner lists so that
the whole column can be wide enough to fit all the strings. Store the maximum width
of each column as a list of integers. 
"""
def getColumnWidth():
    for listData in tableData:
        max=0
        for item in listData:
            if max < len(item):
                max=len(item)
        columnWidth.append(max)

"""
This function prints the list content in well-organized table.
"""
def printTable():
    for idx in range(rowSize):
        for idy in range(columnSize):
            print(tableData[idy][idx].rjust(columnWidth[idy], ' '), end=' ')
        print()

def main():
    getColumnWidth() 
    printTable()

main()
