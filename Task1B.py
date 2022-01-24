from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key # noqa

def run():
    
    # define p as reference point (Cambridge city centre)
    p = (52.2053, 0.1218)

    # build the list of stations
    stations = build_station_list()

    # build the list of (stations, distance) tuples
    station_distance_tuple_list = stations_by_distance(stations, p)

    # make an empty list for the (station, town, distance) tuples to go into
    std_tuple_list = []

    # create the tuples and add them to the std list
    for i in station_distance_tuple_list:
        this_tuple = (i[0].name, i[0].town, i[1])
        std_tuple_list.append(this_tuple)
    
    closest_10 = std_tuple_list[:10]
    furthest_10 = std_tuple_list[-10:]

    # Print the lists of (station name, town, distance) tuples
    print("Taken from the Cambridge town centre:", '\n')
    print("10 closest stations: {}".format(closest_10), '\n')
    print("10 furthest stations: {}".format(furthest_10))

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()