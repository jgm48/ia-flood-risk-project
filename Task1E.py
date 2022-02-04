'''TASK 1E'''

<<<<<<< HEAD
from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.station import *
# Run the demonstration with N = 9
rivers_by_station_number(stations, 9)
=======
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
>>>>>>> 324e8493f647d047c6e2b53cdcbe672c83f591b2
