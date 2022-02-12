from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B"""
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print the name and relative level of each station with a relative level over the tolerance
    over_tol = stations_level_over_threshold(stations, 0.8)
    for i in over_tol:
        print(i[0].name, i[1])
    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
