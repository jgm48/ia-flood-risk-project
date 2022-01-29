from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():

    # Build list of stations
    stations = build_station_list()

    # Cambridge town centre
    centre = (52.2053, 0.1218)

    # Radius = 10km
    r = 10.0

    cambridge_stations = stations_within_radius(stations, centre, r)

    print("Stations within 10km of Cambridge town centre: ")   
    print(sorted(cambridge_stations))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
run()