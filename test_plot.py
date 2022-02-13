from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation

#test for 2E
def test_plot_water_levels():

    # does a plot and checks that there isn't invalid data
    Mersey_test = MonitoringStation("Mersey", "ID", "Mersey", "0,0", [0.5, 1.5], "Mersey", "Liverpool")
    assert plot_water_levels(Mersey_test, [], []) == "Invalid data"
