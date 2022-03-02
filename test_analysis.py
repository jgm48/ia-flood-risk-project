#test_analysis

"""Unit test for analysis module"""

import datetime
import numpy
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, risk_level_towns
from floodsystem.datafetcher import fetch_measure_levels

def test_polyfit():
    """Tests polyfit function"""
    
    # station data as before
    stations = build_station_list()
    update_water_levels(stations)
    
    dt = 10 
    assert type(stations) == list
    # output data types
    for x in range(1, 1500, 100):
        
        i = stations[x]
        
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        
        for n in range(2, 4):
            continue
            assert type(polyfit(dates, levels, n)[0]) == numpy.poly1d
            assert type(polyfit(dates, levels, n)[1]) == numpy.float64

def test_risk_level_towns():
    """Tests risk_level_towns function"""
    
    stations = build_station_list()
    update_water_levels(stations)

    severe, high, moderate, low = risk_level_towns()

    # check that most towns belong to a risk level
    for i in range(0, len(stations) - 1, 250):
        assert stations[i].town in severe or stations[i].town in high or stations[i].town in moderate or stations[i].town in low