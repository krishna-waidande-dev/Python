import folium
import pandas
import random

def giveRandomColour():
    return random.choice(('green','orange','red'))

#Read file and retrive latitude and longitude and place.
data = pandas.read_csv("lat-lon-delhi.txt")
lat = list(data["latitude"])
lon = list(data["longitude"])
place = list(data["place_name"])

#Location for Pimple Saudagar.
#mapDemo = folium.Map(location=[18.59,73.79], tiles="OpenStreetMap")

#Location for New Delhi
mapDemo = folium.Map(location=[28.6139, 77.2090], tiles="OpenStreetMap")

#Add feature group.
fgL = folium.FeatureGroup(name="Lon-Lat")

for lt, lon, plc in zip(lat, lon, place):
    #Adding Circle Marker on Map.
    fgL.add_child(folium.CircleMarker(location=[lt, lon], radius=7, popup=plc, 
    fill_color=giveRandomColour(), color='grey', fill_opacity=0.7))

    #Adding Markers on Map. This is optional for above line.
    #fg.add_child(folium.Marker(location=[lt, lon], popup=plc, icon=folium.Icon(color=giveRandomColour())))


fgP = folium.FeatureGroup(name="Population")

#To add polygon on Map from world.json file.
fgP.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000000
                else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#Style_function is added to provide multiple colour as per population count.

mapDemo.add_child(fgL)
mapDemo.add_child(fgP)
#To control the layers of the map.
mapDemo.add_child(folium.LayerControl())

#Saving Map into HTML file.
mapDemo.save("C:/Users/91976/Documents/Python/Application3/latitude-longitute.html")