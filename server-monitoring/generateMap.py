import folium
import pandas
from platform import system
from subprocess import call, DEVNULL
from datetime import datetime


# DEVNULL is used to supress output of ping command.
def ping_to_server(host):
    if system().lower() == 'windows':
        command = ['ping', '-n', '2', host]
    else:
        command = ['ping', '-c', '2', host]
    return call(command, stdout=DEVNULL) == 0


def pinpoint(color, latitude, longitude, plc, srv_name):
    if color == 'red':
        pop_up_msg = r"<i>"+srv_name+"</i><br> <i> Down At:"+str(datetime.now())+"</i>"
    else:
        pop_up_msg = r"<i>"+srv_name+"</i>"

    return folium.Marker([latitude, longitude], popup=pop_up_msg, tooltip=plc,
                         icon=folium.Icon(color=color))


def add_markers(feature_grp, lat, lon, place, server):
    for lt, ln, plc, srv in zip(lat, lon, place, server):
        # Pinging to servers and adding Circle Marker on Map.
        if ping_to_server(srv):
            feature_grp.add_child(pinpoint('green', lt, ln, plc, srv))
        else:
            feature_grp.add_child(pinpoint('red', lt, ln, plc, srv))


def draw_map(lat, lon, place, server):
    # Creating Map.
    worldmap = folium.Map(tiles="OpenStreetMap", width=1100, height=600,
                          zoom_start=7, zoom_control=True)
    # Add feature group.
    fg = folium.FeatureGroup(name="locations")
    add_markers(fg, lat, lon, place, server)
    worldmap.add_child(fg)
    worldmap.save("C:/Users/91976/PycharmProjects/FlaskPractice/templates/latitude-longitute.html")


def load_data():
    # Read file and retrieve latitude, longitude, location, server name.
    data = pandas.read_csv("server-locations.txt")
    lat_f = list(data["latitude"])
    lon_f = list(data["longitude"])
    place_f = list(data["place_name"])
    server_f = list(data["server_name"])
    return (lat_f, lon_f, place_f, server_f)


def render_map():
    lat, lon, place, server = load_data()
    draw_map(lat, lon, place, server)

