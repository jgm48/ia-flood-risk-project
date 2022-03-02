#test_analysis

"""Unit test for analysis module"""

import datetime
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
#from floodsystem.analysis import risk_level_towns

def test_polyfit():
    """Tests polyfit function"""
    # station data as before
    stations = build_station_list()
    update_water_levels(stations)
    
    dt = 10 
    
    # output data types
    for x in range(1, 1500, 100):
        i = stations[x]
        dates, levels = fetch_measure_levels(i.measure_id,
        dt=datetime.timedelta(days=dt))
        for n in range(2, 4):
            assert type(polyfit(dates, levels, n)[1]) == np.float64
            assert type(polyfit(dates, levels, n)[0]) == np.poly1d
            

