'''TASK 1E'''

from distutils.command.build import *
from floodsystem.geo import *
from floodsystem.station import *
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list

def run():
    
    # Obtain list of stations
    stations = build_station_list()
    
    # Run the demonstration with N = 9
    N = 9
    tempList = rivers_by_station_number(stations, N)
    print("The {0} rivers with the greatest number of monitoring stations are:\n{1}".format(N, tempList))

if __name__ == "__main__":
    print("***Task 1E: CUED Part IA Flood Warning System***")
    run()
