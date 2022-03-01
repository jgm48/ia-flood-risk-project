import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import analysis
from analysis import polyfit

# for task 2e
def plot_water_levels(station, dates, levels):
    """produce a plot of water levels against time for a station"""
    """include on the plot lines for the typical low and high levels."""

    # plot the low and high typical values
    low_typ_range_list = len(dates) * [station.typical_range[0]]
    plt.plot(dates, low_typ_range_list, color='r', label='low level')
    high_typ_range_list = len(dates) * [station.typical_range[1]]
    plt.plot(dates, high_typ_range_list, color='g', label='high level')

    # plot the water level data
    if dates == [] or levels == []:
        return "Invalid data"
    else:
        plt.plot(dates, levels, color='b', label='water level')
    
    # setting up graph layout
    plt.xlabel('Date')
    plt.ylabel('Water level data (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend(loc='best')

    # maximise the window
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
    # gimmie dat plot!
    plt.show()

# for Task 2F

def plot_water_level_with_fit(station, dates, levels, p):
    
    dates_float_list = matplotlib.dates.date2num(dates)
    # best fit polynomial
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, poly(dates_float_list - d0), color='gold', label='best fit polynomial order {0}'.format(p))
    plt.legend(loc='best')
    # data from before
    plot_water_levels(station, dates, levels)
    
    plt.show()