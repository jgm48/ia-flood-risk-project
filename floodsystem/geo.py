# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    "Takes a list of stations and a coordinate p. returns a lsit of (station, distance) tuples in order of distance"

    # Build the lsit of stations
    stations = build_station_list()

    # Make an empty list for the (station, distance) tuples to go into
    list_of_tuples = []

    for i in stations:
        distance = haversine(i.coord, p)
        station_distance_tuple = (i, distance)
        list_of_tuples.append(station_distance_tuple)
    
    return sorted_by_key(list_of_tuples, 1)
