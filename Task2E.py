import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    """Requirements for Task 2E"""

    #build and update list of station objects
    stations = build_station_list()
    update_water_levels(stations)

    dt = 10
    
    # Get the list of station object tuples
    high_stations = stations_highest_rel_level(stations, 5)
    
    # Make list of these 5 stations' measure_ids
    high_station_id = []
    
    for i in range(5):
        high_station_tuple = (high_stations[i][0]).measure_id
        high_station_id.append(high_station_tuple)
    
    # Make list of the station names
    high_objects = []
    for i in range(5):
        high_objects.append(high_stations[i][0])

    for i in range(5):
        dates, levels = fetch_measure_levels(high_objects[i].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(high_objects[i], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
