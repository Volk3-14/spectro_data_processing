#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pybaselines as pbl
import scipy.interpolate as spi

def get_normed_spectrum_and_line_positions():
    data = open("data10/20220722_160350.Ch_B.000.dat", "r")
    lines = data.readlines()
    length = len(lines)
    spectrum = list()
    freq = np.arange(0, length, 1)

    # spectrum with all points
    for i in range(length):
        spectrum.append(int(lines[i]))
    spectrum = np.array(spectrum)
    # reverse
    constant_array = np.ones(len(spectrum))*500000
    spectrum_reverse = constant_array - spectrum

    # interpolate
    baseline_reverse = pbl.polynomial.imodpoly(spectrum_reverse, freq, poly_order=12, tol=1e-6, max_iter=250, use_original=True)[0]
    baseline_imodpoly = constant_array - baseline_reverse
    #baseline_reverse = pbl.polynomial.quant_reg(spectrum_reverse, freq, poly_order=8, quantile=0.05)[0]
    #baseline_quantreg = constant_array - baseline_reverse
    #baseline_reverse = pbl.whittaker.iasls(spectrum_reverse, freq, lam=1e5, p=1e-4, lam_1=1e-4)[0]
    #baseline_iasls = constant_array - baseline_reverse
    #baseline_reverse = pbl.spline.irsqr(spectrum_reverse)[0]
    #baseline_irsqr = constant_array - baseline_reverse
    #baseline_reverse = pbl.classification.fastchrom(spectrum_reverse, half_window=100, threshold=1000)[0]
    #baseline_fastchrom = constant_array - baseline_reverse

    # plot
    plt.plot(freq, spectrum, 'o', label='raw spectrum')
    #plt.plot(freq, baseline_imodpoly, '-', label='baseline imodpoly')
    #plt.plot(freq, baseline_cont_wavelet, '-', label='baseline cont wavelet')
    #plt.plot(freq, baseline_quantreg, '-', label='baseline quantreg')
    #plt.plot(freq, baseline_iasls, '-', label='baseline iasls')
    plt.plot(freq, baseline_imodpoly, '-', label='baseline test')
    plt.legend()
    plt.show()

    #spectrum_normed = spectrum/baseline_imodpoly
    #label_normed ='normed spectrum (imodpoly)'
    #spectrum_normed = spectrum/baseline_quantreg
    #label_normed = 'normed spectrum (quantreg)'
    #spectrum_normed = spectrum/baseline_iasls
    #label_normed = 'normed spectrum (iasls)'
    spectrum_normed = spectrum/baseline_imodpoly
    #label_normed = 'normed spectrum (test)'
    #plt.plot(freq, spectrum_normed, '-', label=label_normed)
    #plt.legend()
    #plt.show()

    # spectral lines
    bspline = spi.splrep(freq, spectrum_normed, k=4)
    bspline_der1 = spi.splder(bspline, n=1)
    minimax = spi.sproot(bspline_der1, mest=1800)
    threshold = 0.01             # min depth of spectral lines
    spectral_lines = list()
    for i in range(len(minimax)):
        if abs(spi.splev(minimax[i], bspline) - 1) > threshold:
            spectral_lines.append(minimax[i])
    spectral_lines.reverse()
    #print(spectral_lines)

    return (spectrum_normed, spectral_lines)

#get_normed_spectrum_and_line_positions()
