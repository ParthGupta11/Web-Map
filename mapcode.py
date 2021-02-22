import folium
import pandas
import itertools

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def icon_color(el):
    if el <= 1000 :
        return "blue"
    elif el <1500 :
        return "green"
    elif el <= 2000 :
        return "orange"
    else:
        return "red"


maps = folium.Map(location=[28.632901,77.219761], zoom_start=14, tiles="OpenStreetMap")
feature_group = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
        feature_group.add_child(folium.Marker(location=[lt,ln], popup="elevation: {} meters".format(el), icon = folium.Icon(color = icon_color(el))))

maps.add_child(feature_group)

maps.save("map1.html")
