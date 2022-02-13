import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# for task 2e
def plot_water_levels(station, dates, levels):
    """produce a plot of water levels against time for a station"""
    """include on the plot lines for the typical low and high levels."""

    # plot the low and high typical values
    low_typ_range_list = len(dates) * [station.typical_range[0]]
    plt.plot(dates, low_typ_range_list, 'r')
    high_typ_range_list = len(dates) * [station.typical_range[1]]
    plt.plot(dates, high_typ_range_list, 'r')

    # plot the water level data
    if dates == [] or levels == []:
        return "Invalid data"
    else:
        plt.plot(dates, levels, 'g')
    
    # setting up graph layout
    plt.xlabel('Date')
    plt.ylabel('Water level data (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    
    # gimmie dat plot!
    plt.show()
