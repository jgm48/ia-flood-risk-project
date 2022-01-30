# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
from haversine import haversine

# for task 1B
def stations_by_distance(stations, p):
    "Takes a list of stations and a coordinate p. returns a list of (station, distance) tuples in order of distance"

    # Build the lsit of stations
    stations = build_station_list()

    # Make an empty list for the (station, distance) tuples to go into
    list_of_tuples = []

    for i in stations:
        distance = haversine(i.coord, p)
        station_distance_tuple = (i, distance)
        list_of_tuples.append(station_distance_tuple)
    
    return sorted_by_key(list_of_tuples, 1)

# for task 1C
def stations_within_radius(stations, centre, r):
    """Returns a list of stations within a radius of a given coordinate"""

    # Build a list of stations
    stations = build_station_list()

    # Create an empty list for the stations within the radius to go in to
    list_of_stations_in_radius = []
    
    # check if the distance between the station and the centre is < r
    for i in stations:
        if haversine(i.coord, centre) < r:
            list_of_stations_in_radius.append(i.name)
    
    return list_of_stations_in_radius

# for task 1D
def rivers_with_station(stations):
    """Return a set with the names of the rivers with a monitoring station"""

    # make an empty list for the items to go into
    river_names = []

    for i in stations: 
        river_names.append(i.river)
    
    # convert to a set to romove duplicates
    river_names_set = set(river_names)

    return river_names_set

# for task 1D
def stations_by_river(stations):
    """Return a dictionary that maps river names to a list of station objects on a given river"""

    # create an empty dictionary
    river_dict = {}

    # add river names as keys with empty values
    for i in rivers_with_station(stations):
        river_dict.update({i: []})
    
    # add station names as values to corresponding keys in dictionary
    for i in stations:
        for j in rivers_with_station(stations):
            if i.river == j:
                river_dict[j].append(i.name)

    return river_dict