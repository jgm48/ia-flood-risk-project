from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

# for task 2b
def test_stations_level_over_threshold():
    """Test stations_level_over_threshold function"""

    stations = build_station_list()
    update_water_levels(stations)

    #check for unreasonable upper limit
    assert len(stations_level_over_threshold(stations, 100000000)) == 0

    # check that the list is sorted
    for i in range(len(stations_level_over_threshold(stations, 0)) - 1):
        assert stations_level_over_threshold(stations, 0)[i][1] >= stations_level_over_threshold(stations, 0)[i + 1][1]

# for task 2c
def test_stations_highest_rel_level():
    """Test stations_highest_rel_level function"""
    
    stations = build_station_list()
    update_water_levels(stations)

    # check that list is sorted
    full_list = stations_highest_rel_level(stations, 100000)
    
    for i in range(len(full_list) - 1):
        assert full_list[i][1] >= full_list[i + 1][1]

    # use the function to make a list, then check if it is the expected length
    for i in range(1, 1000, 100):
        i_length = stations_highest_rel_level(stations, i)
        assert len(stations_highest_rel_level(stations, i)) == i

        #also check that the highest value in output list is the same as in the full list
        for n in range(len(full_list) - 1):
            assert i_length[0][1] >= full_list[n][1]