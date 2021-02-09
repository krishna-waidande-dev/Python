import pandas
from geopy.geocoders import Nominatim

nom = Nominatim(user_agent="testing-app", scheme='http')

#Reads the place name from user and shows it's latitute and longitute.
place=input("Enter the place name : ") 
print("Latitute of "  + place + " is : " + str(nom.geocode(place).latitude))
print("Longitute of " + place + " is : " + str(nom.geocode(place).longitude))

#Reads the CSV file columns of address and adds new 2 columns as latitude and longitude.
df = pandas.read_csv("supermarkets.csv")

df["Address"]=df["Address"] + "," + df["City"] + "," + df["State"] + "," + df["Country"]
df["Coordinates"]= df["Address"].apply(nom.geocode)
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)

#Printing the final result.
print(df)