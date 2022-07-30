import folium
import pandas
from platform import system
from subprocess import call, DEVNULL
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(5)


def getServerPingCommand(server):
    if system().lower() == 'windows':
        return ['ping', '-n', '2', server]
    else:
        return ['ping', '-c', '2', server]


def pinpoint(color, latitude, longitude, app, srv_name):
    print(f"For {srv_name} colour is {color}")
    if color == 'red':
        pop_up_msg = r"<i>" + srv_name + "</i><br> <i> Down At:" + str(datetime.now()) + "</i>"
    else:
        pop_up_msg = r"<i>" + srv_name + "</i>"

    return folium.Marker([latitude, longitude], popup=pop_up_msg, tooltip=app,
                         icon=folium.Icon(color=color))


def makeCommand(entity, server):
    if entity == "server_name":
        return getServerPingCommand(server)

    if entity == "db_name":
        return ['tnsping', server]

def actualCall(cmd, feature_grp, lat, lon, app_name, server):
    isServerUp = True if call(cmd, stdout=DEVNULL) == 0 else False

    if (isServerUp):
        feature_grp.add_child(pinpoint('green', lat, lon, app_name, server))
    else:
        feature_grp.add_child(pinpoint('red', lat, lon, app_name, server))

    return feature_grp

def add_markers(feature_grp, lat, lon, app_name, server, entity):
    cmd = makeCommand(entity, server)
    future = executor.submit(actualCall, cmd, feature_grp, lat, lon, app_name, server)
    return future.result()


def load_file_data(filename, entity):
    data = pandas.read_csv(filename)
    entities = list(data[entity])   # Entities could either be Servers or DBs
    appNames = list(data["app_name"])
    lats = list(data["latitude"])
    longs = list(data["longitude"])

    return lats, longs, appNames, entities


def render_map():
    worldmap = folium.Map(tiles="OpenStreetMap", width=1100, height=600,
                          zoom_start=7, zoom_control=True)

    fg = folium.FeatureGroup(name="server-locations")

    lats, longs, appNames, entities = load_file_data("server-locations.txt", "server_name")

    for latitude, longitude, appName, entity in zip(lats, longs, appNames, entities):
        fg2 = add_markers(fg, latitude, longitude, appName, entity, "server_name")

    worldmap.add_child(fg2)
    worldmap.save("C:/Users/91976/PycharmProjects/FlaskPractice/templates/latitude-longitute.html")

render_map()
