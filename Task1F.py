'''TASK 1F'''

from distutils.command.build import *
from floodsystem.geo import *
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range

def run():
    # Build a list of stations
    stations = build_station_list()
    
    # List of stations with inconsistent typical data
    inconsistent_station_list = inconsistent_typical_range_stations(stations)
    
    # Sort the list alphabetically
    inconsistent_station_list = sorted(inconsistent_station_list)

    print("A list of all stations with inconsistent typical data:\n", inconsistent_station_list)

    
if __name__ == "__main__":
    print("***Task 1F: CUED Part IA Flood Warning System***")
    run()