import json
import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim


def geocode_all():
    geolocator = Nominatim(user_agent="polling-mapping")
    with open("locations.txt") as locations_file, open("geocode_results.jsonl", "a") as geocode_results_file:
        while address := locations_file.readline().rstrip():
            print(address)
            result = geolocator.geocode(address).raw
            geocode_results_file.write(str(result) + '\n')


def load_to_map():
    m = folium.Map(location=[35.0844, -106.6504], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(m)
    with open("geocode_results.jsonl") as geocode_results_file, open("raw_gps_additions.jsonl") as additions:
        [m.add_to(marker_cluster) for m in parse_locations(geocode_results_file)]
        [m.add_to(marker_cluster) for m in parse_locations(additions)]

    m.save("index.html")


def parse_locations(locations_file):
    markers = []
    while geocode_result := locations_file.readline().rstrip():
        location_json = json.loads(str(geocode_result))
        location = (location_json["lat"], location_json["lon"])
        name = location_json["display_name"]
        markers.append(folium.Marker(location=location, popup=name, tooltip=name))
    return markers


if __name__ == '__main__':
    # geocode_all()
    load_to_map()

