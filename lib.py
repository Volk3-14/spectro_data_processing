# library with some useful routines

import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

def make_uniform(spectrum, freq_scale):
# function evaluates spline and returns spectrum in uniform points
# spectrum - numpy array with signal power
# freq_scale - numpy array, non-uniform scale of frequencies
# (usially in cm**(-1)
# freq_scale must be sorted and freq_scale[0] = min
#                               freq_scale[-1] = max
    #print(spectrum)
    #print(freq_scale)
    uniform_freq_scale = (freq_scale[-1]-freq_scale[0])/(len(freq_scale)-1)*np.arange(len(freq_scale))
    uniform_freq_scale += freq_scale[0]
    spline = spi.splrep(freq_scale-freq_scale[0], spectrum, k=3)
    uniform_spectrum = spi.splev(uniform_freq_scale-freq_scale[0], spline)
    return uniform_spectrum
