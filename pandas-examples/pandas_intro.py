import pandas
df = pandas.DataFrame([[2,4,6],[10,20,30]], 
    columns=["Price","Age","Value"], 
    index=["Row1", "Row2"])

print(df)
print("Max of price is : " + str(df.Price.max()))
print("Min of price is : " + str(df.Price.min()))
print("Avg of price is : " + str(df.Price.mean()))