from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    """Test stations_level_over_threshold function"""

    stations = build_station_list()
    update_water_levels(stations)

    #check for unreasonable upper limit
    assert len(stations_level_over_threshold(stations, 100000000)) == 0

    # check that the list is sorted
    for i in range(len(stations_level_over_threshold(stations, 0)) - 1):
        assert stations_level_over_threshold(stations, 0)[i][1] >= stations_level_over_threshold(stations, 0)[i + 1][1]

