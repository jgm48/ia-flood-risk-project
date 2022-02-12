from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2C"""

    # Build station objects and update their levels
    stations = build_station_list()
    update_water_levels(stations)

    # Print in descending order 10 rivers with highest levels
    N = 10
    highest_n = stations_highest_rel_level(stations, N)
    for i in highest_n:
        print(i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()  