#New submodule analysis
import matplotlib.dates
import numpy as np
from .stationdata import build_station_list, update_water_levels
from .datafetcher import fetch_measure_levels
from .flood import stations_level_over_threshold
import datetime
from .station import MonitoringStation, inconsistent_typical_range_stations

# polynomial fitting for Task 2F
def polyfit(dates, levels, p):
    """given the water level time history (dates, levels) for a station computes a least-squares fit 
    of a polynomial of degree p to water level data. The function returns a tuple of the polynomial object
    and any shift of the time (date) axis"""

    # deal with dates to floating points
    dates_float_list = matplotlib.dates.date2num(dates)
    d0 = dates_float_list[0]

    # find the coefficients for general order p and convert to useful form

    # zero the time axis
    p_coeff = np.polyfit((dates_float_list - d0), levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0 #a tuple of the poly object and time shift

# determining flood risk level of towns for task 2G
def risk_level_stations():
    
    # build list of stations and water levels therein...
    stations = build_station_list()
    update_water_levels(stations)


    # List of stations with inconsistent typical data
    inconsistent_station_list = inconsistent_typical_range_stations(stations)
    # remove stations with inconsistent data or no data
    valid_stations = stations
    for i in valid_stations:
        if i in inconsistent_station_list:
            valid_stations.remove(i)


    # create lists for all the STATIONS
    severe_stations = []
    high_stations = []
    moderate_stations = []
    low_stations = []
    
    sorted_with_level = stations_level_over_threshold(valid_stations, -100000)

    counter = 0
    # sort all of the stations into their risk levels
    for i in sorted_with_level:
        for n in stations_level_over_threshold(valid_stations, 2):
            if i[0] == n[0]:
                severe_stations.append(i[0])
                counter += 1
    for i in range(counter, len(sorted_with_level)):
        for a in stations_level_over_threshold(valid_stations, 1.5):
            if sorted_with_level[i][0] == a[0]:
                high_stations.append(sorted_with_level[i][0])
                counter += 1
    for i in range(counter, len(sorted_with_level)):
        for a in stations_level_over_threshold(valid_stations, 0.5):
            if sorted_with_level[i][0] == a[0]:
                moderate_stations.append(sorted_with_level[i][0])
                counter += 1
    for i in range(counter, len(sorted_with_level)):
        for a in stations_level_over_threshold(valid_stations, -100000):
            if sorted_with_level[i][0] == a[0]:
                low_stations.append(sorted_with_level[i][0])
                counter += 1
    return severe_stations, high_stations, moderate_stations, low_stations

# now need to obtain risk for each TOWN from the stations
# consider the highest level threat for each town
def risk_level_towns():
    
    severe, high, moderate, low = risk_level_stations()
    severe_towns = []
    high_towns = []
    moderate_towns = []
    low_towns = []

    # cascading assignment of risk levels to towns
    for i in severe:
        if i.town is None:
            severe_towns.append(i.town)
    for i in high:
        if i.town not in severe_towns:
            high_towns.append(i.town)
    for i in moderate:
        if i.town not in severe_towns and i.town not in high_towns:
            moderate_towns.append(i.town)
    for i in low:
        if i.town not in severe_towns and i.town not in high_towns and i.town not in moderate_towns:
            low_towns.append(i.town)

    return severe_towns, high_towns, moderate_towns, low_towns


