#! /usr/bin/env python3

import math
import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt
import pybaselines as pbl

# 1/(2L) in cm^(-1)
etalon_const = 0.025927

def get_max_positions():
    #data = open("etalon/20220722_161044.Ch_B.000.dat", "r")
    data = open("etalon/3762-3766_F-P.dat", "r")
    lines = data.readlines()
    length = len(lines)
    spectrum = list()
    freq = np.arange(0, length, 1)

    # spectrum with all points
    for i in range(length):
        spectrum.append(int(lines[i]))
    spectrum = np.array(spectrum)
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

    # derivatives
    bspline_der1 = spi.splder(bspline, n=1)
    minimax = spi.sproot(bspline_der1, mest=350)
    #print(minimax)
    maxima = list()
    threshold = (np.amax(spectrum_normed) - np.amin(spectrum_normed))/2
    for i in range(len(minimax)):
        if abs(spi.splev(minimax[i], bspline) - 1) < threshold:
            maxima.append(minimax[i]/1000.0)
    del(maxima[0:4])
    length_maxima = len(maxima)
    #maxima.reverse()
    freq_cm = etalon_const*np.arange(0, length_maxima, 1)
    # supportive variables
    #denominator = 0.0
    (a1, a2, a2_hat, a3, a4) = (0.0, 0.0, 0.0, 0.0, 0.0)
    (c0, c1, c2) = (0.0, 0.0, 0.0)
    # for function y = alpha*x**2p + beta*x + gamma
    param = 1.0
    for i in range(length_maxima):
        a1 += maxima[i]
        #a2 += maxima[i]*maxima[i]
        a2 += maxima[i]**(2*param)
        a2_hat += maxima[i]*maxima[i]
        a3 += maxima[i]**(2*param+1)
        #a3 += maxima[i]**3
        #a4 += maxima[i]**4
        a4 += maxima[i]**(4*param)
        c0 += freq_cm[i]
        c1 += freq_cm[i]*maxima[i]
        c2 += freq_cm[i]*(maxima[i]**(2*param))
    #a2_hat = a2
    alpha = ((c2-c0*a2)*(a2_hat-a1*a1) - (c1-c0*a1)*(a3-a1*a2)) / ((a4-a2*a2)*(a2_hat-a1*a1) - (a3-a1*a2)**2)
    beta = (c1 - c0*a1 - alpha*(a3-a1*a2))/(a2_hat - a1*a1)
    gamma = c0 - alpha*a2 - beta*a1
    print('alpha, beta, gamma = ', alpha, beta, gamma)
    RMSE = 0.0
    for i in range(length_maxima):
        #RMSE += (freq_cm[i] - alpha*maxima[i]**(2*param) - beta*maxima[i] - gamma)**2
        RMSE += (freq_cm[i] - alpha*maxima[i]*maxima[i] - beta*maxima[i] - gamma)**2
    print('RMSE = ', RMSE)
    #log_maxima = list()
    #log_freq_cm = list()
    #for i in range(1, len(maxima)):
    #    log_maxima.append(math.log(maxima[i]))
    #    log_freq_cm.append(math.log(freq_cm[i]))

    # plot
    plt.plot(freq, spectrum, 'o', label='raw spectrum')
    plt.plot(freq, baseline, '-', label='baseline')
    plt.legend()
    plt.show()
    plt.plot(freq, spectrum_normed, 'o', label='normed spectrum')
    plt.plot(freq_new, spectrum_interpolated, 'g-', label='interpolated')
    plt.plot(maxima, spi.splev(maxima, bspline), 'o', label='maxima')
    plt.legend()
    plt.show()
    plt.plot(maxima, freq_cm, 'o', label='frequency, cm^(-1)')
    y = [freq_cm[0], freq_cm[len(freq_cm)-1]]
    x = [maxima[0], maxima[length_maxima-1]]
    plt.plot(x, y, '-', label='straight line')
    z = np.arange(maxima[0], maxima[length_maxima-1], 0.01)
    #fit = alpha**(2*param*z) + beta*z + gamma
    fit = alpha*z*z + beta*z + gamma
    plt.plot(z, fit, '-', label='fit')
    plt.legend()
    plt.show()

    # return list of max positions
    return maxima

#maxima = get_max_positions()
#print(maxima)
