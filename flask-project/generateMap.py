import folium
import pandas
from platform import system
from subprocess import call, DEVNULL
from datetime import datetime


# DEVNULL is used to supress output of ping command.
def ping_to_server(host):
    if system().lower() == 'windows':
        print("Check for " + host)
        command = ['ping', '-n', '2', host]
    else:
        command = ['ping', '-c', '2', host]
    return call(command, stdout=DEVNULL) == 0


# tnsping command is used to check if database is available or not.
def ping_to_db_server(db_service_name):
    print("Check for " + db_service_name)
    command = ['tnsping', db_service_name]
    return call(command, stdout=DEVNULL) == 0


def pinpoint(color, latitude, longitude, app, srv_name):
    if color == 'red':
        pop_up_msg = r"<i>" + srv_name + "</i><br> <i> Down At:" + str(datetime.now()) + "</i>"
    else:
        pop_up_msg = r"<i>" + srv_name + "</i>"

    return folium.Marker([latitude, longitude], popup=pop_up_msg, tooltip=app,
                         icon=folium.Icon(color=color))


def add_markers(feature_grp, lat, lon, app_name, server, entity):
    if entity == "server":
        result = ping_to_server(server)

    if entity == "db":
        result = ping_to_db_server(server)

    if (result):
        feature_grp.add_child(pinpoint('green', lat, lon, app_name, server))
    else:
        feature_grp.add_child(pinpoint('red', lat, lon, app_name, server))


# def draw_map(lat, lon, app_name, server, entity):
#     # Creating Map.
#     worldmap = folium.Map(tiles="OpenStreetMap", width=1100, height=600,
#                           zoom_start=7, zoom_control=True)
#     # Add feature group.
#     fg = folium.FeatureGroup(name="locations")
#
#     for lt, ln, app, srv in zip(lat, lon, app_name, server):
#         add_markers(fg, lt, ln, app, srv, entity)
#
#     worldmap.add_child(fg)
#     worldmap.save("C:/Users/acjxqkk/PycharmProjects/Automation-Project/Flask-Demo/templates/latitude-longitute.html")


def load_server_data():
    # Read file and retrieve latitude, longitude, location, server name.
    data = pandas.read_csv("server-locations.txt")
    app_name_f = list(data["app_name"])
    lat_f = list(data["latitude"])
    lon_f = list(data["longitude"])
    server_f = list(data["server_name"])

    return lat_f, lon_f, app_name_f, server_f


def load_db_data():
    data = pandas.read_csv("db-locations.txt")
    app_name = list(data["app_name"])
    db_name = list(data["db_name"])
    lat_f = list(data["latitude"])
    lon_f = list(data["longitude"])

    return lat_f, lon_f, app_name, db_name


def render_map():
    # Creating Map.
    worldmap = folium.Map(tiles="OpenStreetMap", width=1100, height=600,
                          zoom_start=7, zoom_control=True)

    # Add feature group.
    fg = folium.FeatureGroup(name="server-locations")

    lat, lon, app_name, server = load_server_data()

    for lt, ln, app, srv in zip(lat, lon, app_name, server):
        add_markers(fg, lt, ln, app, srv, "server")

    lat, lon, app_name, server = load_db_data()

    for lt, ln, app, srv in zip(lat, lon, app_name, server):
        add_markers(fg, lt, ln, app, srv, "db")

    worldmap.add_child(fg)
    worldmap.save("C:/Users/acjxqkk/PycharmProjects/Automation-Project/Flask-Demo/templates/latitude-longitute.html")


render_map()
