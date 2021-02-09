import pandas

#Reads Json file using panda. All data is stored in df variable 
# which is also alled as data frame.
df = pandas.read_json("supermarkets.json")
print(df)

#Reads CSV file.
#df1 = pandas.read_csv("supermarkets.csv")
#print(df1)

# Slicing the particular row and column. (Label based indexing)
print(df.loc["0":"2","City":"Name"])

#Store all country values in list
print(list(df.loc[:,"Country"]))

#Slicing the particular row and column. (Position based Indexing)
#Upper value of index is excluded from result.
print(df.iloc[1:3,1:3])

#To print all rows
print(df.iloc[:,1:4])

#To Delete the column, specify 1 and for row 0. It is not inplace.
print(df.drop("City", 1))


