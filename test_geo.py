"""Unit test for the geo module"""

import floodsystem.geo
from floodsystem.station import *
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list

"""John pls write your test functions here, pls make sure all 
your tempVar are only defined inside functions so there are no clashes"""

# Task 1E
def test_rivers_by_station_number():
    
    # Run test with N = 9
    N = 9

    # Obtain list of stations
    stations = build_station_list()
    
    testList = floodsystem.geo.rivers_by_station_number(stations, N)
    # Check that there are at least N rivers in the list
    assert len(testList) >= N