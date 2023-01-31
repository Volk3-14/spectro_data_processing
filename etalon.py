#! /usr/bin/env python3

import math
import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt
import pybaselines as pbl
import readdata
import config


def get_etalon_maxes():
# get maxes from etalon data fit
    #import fit
    #data = open("etalon/20220722_161044.Ch_B.000.dat", "r")
    #data = open("etalon/20220722_161044.Ch_B.001.dat", "r")
    #data = open("etalon/3762-3766_F-P.dat", "r")
    #data = open("etalon/20221101_194836.Ch_A.000.dat")
    #lines = data.readlines()
    #length = len(lines)
    #spectrum = list()

    # spectrum with all points
    #for i in range(length):
    #    spectrum.append(int(lines[i]))
    spectrum = np.array(readdata.get_spectrum(config.file_etalon))
    #spectrum = np.array(spectrum)
    length = len(spectrum)
    freq = np.arange(0, length, 1)
    constant = np.ones(length)*3e6
    spectrum_reverse = constant - spectrum

    # baseline
    baseline = constant - pbl.whittaker.iasls(spectrum_reverse, freq, tol=1e-6)[0]
    spectrum_normed = spectrum/baseline

    # interpolate
    freq_new = np.arange(0, length-1, 0.1)
    bspline = spi.splrep(freq, spectrum_normed, k=4)
    spectrum_interpolated = spi.splev(freq_new, bspline)
    #spline = spi.interp1d(freq, spectrum_normed, kind=3)
    #spectrum_interpolated = spline(freq_new)

    # derivative
    bspline_der1 = spi.splder(bspline, n=1)
    # extremum points
    minimax = spi.sproot(bspline_der1, mest=350)
    maxes = list()
    threshold = (np.amax(spectrum_normed) - np.amin(spectrum_normed))/2
    for i in range(len(minimax)):
        if abs(spi.splev(minimax[i], bspline) - 1) < threshold:
            maxes.append(minimax[i]/1.0)
    #del(maxes[0:4])

    # plot
    #plt.plot(freq, spectrum, 'o', label='raw spectrum')
    #plt.plot(freq, baseline, '-', label='baseline')
    #plt.legend()
    #plt.show()
    #plt.plot(freq, spectrum_normed, 'o', label='normed spectrum')
    #plt.plot(freq_new, spectrum_interpolated, 'g-', label='interpolated')
    #plt.plot(maxes, spi.splev(maxes, bspline), 'o', label='maxes')
    #plt.legend()
    #plt.show()

    # return etalon max positions
    return maxes

#maxima = get_max_positions()
