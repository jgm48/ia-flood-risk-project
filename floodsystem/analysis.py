#New submodule analysis
import matplotlib.dates
import numpy as np

# polynomial fitting for Task 2F
def polyfit(dates, levels, p):
    """given the water level time history (dates, levels) for a station computes a least-squares fit 
    of a polynomial of degree p to water level data. The function returns a tuple of the polynomial object
    and any shift of the time (date) axis"""

    # deal with dates to floating points
    dates_float_list = matplotlib.dates.date2num(dates)
    d0 = dates_float_list[0]

    # find the coefficients for general order p and convert to useful form

    # zero the time axis
    p_coeff = np.polyfit((dates_float_list - d0), levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0 #a tuple of the poly object and time shift