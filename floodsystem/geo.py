# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from typing import Type
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
from haversine import haversine

# for task 1B
def stations_by_distance(stations, p):
    "Takes a list of stations and a coordinate p. returns a list of (station, distance) tuples in order of distance"

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
    
    # convert to a set to remove duplicates
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

'''TASK 1E'''
def rivers_by_station_number(stations, N):
    '''Returns a list of tuples containing river name and number of stations, sorted by number of stations'''
<<<<<<< HEAD
    
    # Get a list of rivers with at least one station
    valid_rivers = rivers_with_station(stations)
=======
>>>>>>> 324e8493f647d047c6e2b53cdcbe672c83f591b2

    # Get the dictionary from above
    river_dict = stations_by_river(stations)

    # List of tuples (river name, number of stations)
    river_number_list = []

    # Iterate through the list of all rivers, and find how many stations they each have
<<<<<<< HEAD
    for i in valid_rivers:
        # Use extend method to deal with tuples being added to a list
        river_number_list.extend(i, len((stations_by_river(stations))[i]))
=======
    for name, stations in river_dict.items():
        river_station_tuple = (name, len(stations))
        # I changed this from extend to append, and it worked instantly
        river_number_list.append(river_station_tuple)
>>>>>>> 324e8493f647d047c6e2b53cdcbe672c83f591b2
    
    # Check N is a valid number
    if type(N) != int:
        raise TypeError("N must be an integer")
    elif N > len(river_number_list):
        raise ValueError("N must be less than the total number of rivers with at least one monitoring station")
    else:
        pass
<<<<<<< HEAD
    
    # Sort list by number of stations descending
    river_number_list = sorted_by_key(river_number_list, 1, reverse=True)

    # Final list for holding number of stations for each river
    river_output_list = []

    # Iterate N times through sorted list
    for i in range(N-1):
        river_output_list.extend(river_number_list[i])
            
    # Check to see if next key has same value when i = N using a while True  
    while True:
        river_output_list.extend(river_number_list[N])
        # Can use N to count as we don't need it for sorting
        if river_number_list[N+1][1] == river_number_list[N][1]:
            N += 1 
            continue
        else:
            break
    
    # The final ouput of the function
    return river_output_list
=======

    # Sort list by number of stations descending
    river_number_list = sorted_by_key(river_number_list, 1, reverse=True)
 
    # Final list for holding number of stations for each river
    river_output_list = river_number_list[:N]
    
    # Check to see if next key has same value
    if river_number_list[N][1] != river_number_list[N-1][1]:
        return river_output_list
    else:
        for i in range(N, len(river_number_list)):
            if river_number_list[i][1] == river_number_list[i-1][1]:
                river_output_list.append(river_number_list[i])
            else:
                break
        return river_output_list
>>>>>>> 324e8493f647d047c6e2b53cdcbe672c83f591b2
