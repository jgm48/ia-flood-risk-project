# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Checks data for consistency. Returns true if data is consistent
        and false if data is unavailable or inconsistent."""
    
        """If data is consistent, there will be data available 
        and typical low range will be lower than typical high range"""
        if self.typical_range != None: # Ie if there is data available
            if self.typical_range[0] < self.typical_range[1]:
                return True
        else:
            return False    

    # for task 2B
    def relative_water_level(self):
        "Returns the latest water level as a fraction of the typical range. If the necessary data is not available or is inconsistent, the function should return None."

        # check for consistent data
        if self.typical_range_consistent is False or self.latest_level is None:
            return None
        else:
            # Calculates relative level
            relative_water_level = ((self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0]))
            return relative_water_level


def inconsistent_typical_range_stations(stations):
    """Returns a list of stations that have inconsistent data given a list of station objects"""
    

    # List comprehension to build a list of inconsistent stations
    full_inconsistent_list = [x for x in stations if MonitoringStation.typical_range_consistent(x) == False]
    inconsistent_names_list = [station.name for station in full_inconsistent_list]
   
    return inconsistent_names_list