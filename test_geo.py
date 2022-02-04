"""Unit test for the geo module"""

import floodsystem.geo
from floodsystem.geo import *
from floodsystem.station import *
from floodsystem.datafetcher import *
from haversine import haversine
from floodsystem.stationdata import build_station_list

# Task 1B
def test_stations_by_distance():
    
    stations = build_station_list()

    # check the data type of the stations list
    assert type(stations) == list

    # set p to a value with known results (Cambridge town centre)
    p = (52.2053, 0.1218)

    # create the list to test
    test_list_B = stations_by_distance(stations, p)

    # checking each element of the list is a tuple of length 2
    for i in test_list_B:
        assert type(i) == tuple
        assert len(i) == 2

    # check data type of values in p and that their values make sense
    for i in p:
        assert type(i) == float
        assert abs(p[0]) <= 180
        assert abs(p[1]) <= 90

# Task 1C
def test_stations_within_radius():

    stations = build_station_list()
    
    # check the data type of the stations list
    assert type(stations) == list

    # give values for centre and radius, that will give known results
    centre = (52.2053, 0.1218)
    r = 0.0

    # create the list to test
    test_list_C = stations_within_radius(stations, centre, r)
    
    # check data type of test_list_c, radius and centre (as well as the values in centre)
    assert type(centre) == tuple
    assert type(test_list_C) == list
    assert type(r) == float
    
    for i in centre:
        assert type(i) == float
        assert abs(centre[0]) <= 180
        assert abs(centre[1]) <= 90

    # check the length of c is 0 (radius = 0, therefore no rivers in radius)
    assert len(test_list_C) == 0

# Task 1D
def test_rivers_with_station():

    stations = build_station_list()

    rivers = rivers_with_station(stations)

    # check data type of rivers
    assert type(rivers) == set

    # Check that set contains values
    assert len(rivers) > 0
    
    # Check that values in container are strings
    for i in rivers:
        assert type(i) == str

# also task 1D :)
def test_stations_by_river():
    
    stations = build_station_list()

    rivers = rivers_with_station(stations)

    river_dict = stations_by_river(stations)

    # check the type of river_dict is a dictionary
    assert type(river_dict) == dict

    # check length of river_dict is the same as rivers
    assert len(river_dict) == len(rivers)

    #check that every river name in river_dict is in the 'rivers' set
    for i in range(len(river_dict)):
        assert (list(river_dict))[i] in rivers

# Task 1E
def test_rivers_by_station_number():
    
    # Run test with N = 9
    N = 9

    # Obtain list of stations
    stations = build_station_list()
    
    testList = floodsystem.geo.rivers_by_station_number(stations, N)
    # Check that there are at least N rivers in the list
    assert len(testList) >= N