#Opening a file in read mode
fileReader=open("example.txt", 'r')
content=fileReader.readlines()
print(content)
#Output: ['Line1\n', 'Line2\n', 'Line3\n', 'Line4']

#Filtering the \n character from the output.
content=[i.rstrip("\n") for i in content]
print(content)
#Output: ['Line1', 'Line2', 'Line3', 'Line4']

#Closing the file.
fileReader.close()