import numpy as np
import scipy.interpolate as spi
import model
import matplotlib.pyplot as plt


# read spectrum
def get_spectrum(filename):
    inf = open(filename, "r")
    spectrum = list()
    while(1):
        line = inf.readline()
        if line == '': break
        spectrum.append(float(line))
    inf.close()
    return spectrum


# read hitran data file and get parameters
# frequencies, line intensities, shifts and so on
def get_hitran_parameters(filename):
    inf = open(filename, "r")
    strings = inf.readlines()
    hitran = {'freq':[], 'intensity':[], 'gamma_air':[], 'gamma_self':[], 'n_air':[], 'shift':[]}
    for string in strings:
        hitran['freq'].append(float(string.split()[2]))
        hitran['intensity'].append(float(string.split()[3]))
        hitran['gamma_air'].append(float(string.split()[4]))
        hitran['gamma_self'].append(float(string.split()[5]))
        hitran['n_air'].append(float(string.split()[6]))
        hitran['shift'].append(float(string.split()[7]))
    inf.close()
    return hitran


# model absorption spectrum
# and get line frequencies as extremum points
def get_hitran_lines(hitran):
    # hitran - dictionary with hitran data
    # {'freq':[], 'intensity':[], 'shift':[]}

    freq_min = hitran['freq'][0] - 0.5
    freq_max = hitran['freq'][-1] + 0.5
    N = 4000                               # number of points
    step = (freq_max-freq_min)/N
    freq_scale = np.arange(freq_min, freq_max, step)
    modeled_spectrum = model.model_spectrum(hitran, freq_scale)
    bspline = spi.splrep(freq_scale, modeled_spectrum, k=3)
    spectrum_der1 = spi.splev(freq_scale, bspline, der=1)
    bspline_der1 = spi.splrep(freq_scale, spectrum_der1, k=3)
    hitran_lines = spi.sproot(bspline_der1, mest=100)

    # delete false roots in line wings
    maximum = max(modeled_spectrum)
    false_roots = list()
    for i in range(len(hitran_lines)):
        if spi.splev(hitran_lines[i], bspline) < 0.01*maximum:
            false_roots.append(i)
    hitran_lines = np.delete(hitran_lines, false_roots)

    # delete minimum extremums
    minimums = list()
    for i in range(len(hitran_lines)):
        point = spi.splev(hitran_lines[i], bspline)
        point_front = spi.splev(hitran_lines[i]+step, bspline)
        point_back = spi.splev(hitran_lines[i]-step, bspline)
        if (point < point_front) and (point < point_back):
            minimums.append(i)
    hitran_lines = np.delete(hitran_lines, minimums)

    #plt.plot(freq_scale, modeled_spectrum)
    #plt.plot(freq_scale, spectrum_der1)
    #plt.plot(hitran_lines, np.zeros_like(hitran_lines), 'o')
    #plt.show()
    # maximum points of absorption spectrum
    hitran_maxes = spi.splev(hitran_lines, bspline)
    return {'freq': hitran_lines, 'maxes': hitran_maxes}
