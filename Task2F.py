#Task 2F
from floodsystem.stationdata import *
from floodsystem.flood import *
from floodsystem.datafetcher import *
from floodsystem.plot import *

def run():
    """Requirements for Task 2F"""

    #build and update list of station objects
    stations = build_station_list()
    update_water_levels(stations)

    # get the 5 stations where the water level is highest
    highest = stations_highest_rel_level(stations, 5)
   
    # Make list of the station names
    high_objects = []
    for i in range(5):
        high_objects.append(highest[i][0])
    for i in range(5):
        dates, levels = fetch_measure_levels(high_objects[i].measure_id,
   
    dt=datetime.timedelta(days=2)) # for 2 days
    plot_water_level_with_fit(high_objects[i], dates, levels, 4)\
    and plot_water_levels(high_objects[i], dates, levels)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()