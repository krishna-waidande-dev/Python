import pandas

df = pandas.read_json("supermarkets.json")

#Get the number of rows for column just replace 0 with 1.
print(df.shape[0])

#Add new column to data frame.
df["Continent"]=df.shape[0]*["Asia"]

#Prints the updated data frame.
print(df)

#Update the data for newly created column with Country name.
df["Continent"]=df["Country"] + "," + "North America"
print(df)

#Data transpose: Means columns becomes rows and rows becomes columns.
df_temp=df.T
print(df_temp)

