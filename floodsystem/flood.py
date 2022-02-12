from .utils import sorted_by_key

# for task 2B
def stations_level_over_threshold(stations, tol):
    "returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over 'tol'"
    "and (ii) the relative water level at the station. The returned list should be sorted by the relative level in descending order"
    "Consider only stations with consistent typical low/high data."

    # create an empty list for the tuples to go into
    stations_over_threshold = []

    # go through each station and check to see if the relative water level is over the tolerence
    for i in stations:
        if i.typical_range_consistent() is True and type(i.latest_level) == float:
            if i.relative_water_level() > tol:
                # create tuple and add it to the list
                station_tuple = (i, i.relative_water_level())
                stations_over_threshold.append(station_tuple)

    #sort list and return that
    sorted_threshold_list = sorted_by_key(stations_over_threshold, 1, reverse=True)
    return sorted_threshold_list