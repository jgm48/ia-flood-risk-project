'''TASK 1E'''

from distutils.command.build import *
from tkinter import N
from floodsystem.geo import *
from floodsystem.station import *
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list

# Run the demonstration with N = 9
stations = build_station_list()
rivers_by_station_number(stations, 9)

