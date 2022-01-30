from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river

def run():
    
    # build a list of stations
    stations = build_station_list()

    # build list of rivers
    rivers = rivers_with_station(stations)

    # print no. of rivers
    print(str(len(rivers)) + " rivers have at least one monitoring station")

    # sort rivers alphabetically, print the first 10
    sorted_rivers = sorted(rivers)
    print("The first 10 of these rivers in alphabetical order are:",
sorted_rivers[0:10])
    # Sort stations for 3 rivers alphabetically, print them
    print("The stations on the River Aire are: ",
(sorted((stations_by_river(stations))["River Aire"])))
    print("The stations on the River Cam are: ",
(sorted((stations_by_river(stations))["River Cam"])))
    print("The stations on the River Thames are: ",
(sorted((stations_by_river(stations))["River Thames"])))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
run()