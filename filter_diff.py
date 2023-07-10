import numpy as np
import scipy as sp
import scipy.interpolate as spi
import matplotlib.pyplot as plt


# get derivative directly
def differentiate(array):
    derivative = np.empty_like(array)
    for i in range(1, len(array)):
        derivative[i] = array[i] - array[i-1]
    derivative[0] = derivative[1]
    return derivative

# get derivative using spline representation
def diff_spline(input_array, order):
    # input_array - 1d array
    # order - integer, order of derivative
    x = np.array(range(len(input_array)))
    bspline = spi.splrep(x, input_array, k=5)
    return spi.splev(x, bspline, der=order)

def filter_diff(raw_spectrum):
    # filter by Savitsky-Golay
    # and take second derivative
    # plot this steps
    spectrum_filtered = sp.signal.savgol_filter(raw_spectrum, window_length=200, polyorder=3)
    #spectrum_diff = differentiate(spectrum_filtered[100:-110])
    spectrum_diff = diff_spline(spectrum_filtered[100: -110], order=1)
    plt.plot(spectrum_diff)
    plt.show()
    spectrum_filtered = sp.signal.savgol_filter(spectrum_diff, window_length=200, polyorder=3)
    plt.plot(spectrum_filtered)
    plt.show()
    spectrum_diff = diff_spline(spectrum_filtered, order=1)
    plt.plot(spectrum_diff)
    plt.show()
    spectrum_filtered = sp.signal.savgol_filter(spectrum_diff, window_length=200, polyorder=3)
    plt.plot(spectrum_filtered)
    plt.show()
    return 0

def filterSG(raw_spectrum):
    # just filter by Savitsky-Golay
    spectrum_filtered = sp.signal.savgol_filter(raw_spectrum, window_length=50, polyorder=3)
    return spectrum_filtered
