from utils import sorted_by_key

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
            # 2nd part is added to remove values that are probably wrong (Letcombe Bassett has relative level = 666 !!??)
            # this can be removed if its wrong, but 666 seems unreasonable
            if i.relative_water_level() > tol and i.name != "Letcombe Bassett":
                # create tuple and add it to the list
                station_tuple = (i, i.relative_water_level())
                stations_over_threshold.append(station_tuple)

    #sort list and return that
    sorted_threshold_list = sorted_by_key(stations_over_threshold, 1, reverse=True)

    return sorted_threshold_list

# for task 1C :)
def stations_highest_rel_level(stations, N):
    "returns a list of N stations at which the water, relative to the typical range, is highest"
    "List should be sorted in descending order by relative level"

    # Create an ordered list of all stations, using the function made in 2B (using an arbitrary big tolerance)
    full_list = stations_level_over_threshold(stations, -100000000)

    # create new list with the top N values from full_list
    n_list = full_list[0:N]

    return n_list