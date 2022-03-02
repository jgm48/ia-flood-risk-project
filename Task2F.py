#Task 2F
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import datetime
def run():
    """Requirements for Task 2F"""

    #build and update list of station objects
    stations = build_station_list()
    update_water_levels(stations)
    valid_stations = []
    for i in stations:
        valid_stations.append(i)

    # get the 5 stations where the water level is highest
    highest = stations_highest_rel_level(valid_stations, 5)

    dt = 2 # number of days
    #cannot get station names directly from list of tuples
    # make list of station ids
    high_station_id = []
    for i in range(5):
        high_station_tuple = (highest[i][0]).measure_id
        high_station_id.append(high_station_tuple)

    # make list of station objects
    high_objects = []
    for i in range(5):
        high_objects.append(highest[i][0])
    
    # actually plot the rivers over time one by one
    for i in range(5):
        dates, levels = fetch_measure_levels(high_objects[i].measure_id, dt=datetime.timedelta(days=dt)) # for 2 days
    plot_water_level_with_fit(high_objects[i], dates, levels, 4) and plot_water_levels(high_objects[i], dates, levels)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()