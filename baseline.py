import numpy as np
import matplotlib.pyplot as plt
import pybaselines as pbl
import scipy.interpolate as spi
import readdata

def get_normed_spectrum_and_line_positions(spectrum):
    #data = open("data10/20220722_160350.Ch_B.000.dat", "r")
    #data = open("data11/20220722_173703.Ch_B.000.dat", "r")
    #data = open("data25/20221101_201220.Ch_B.002.dat", "r")
    #data = open("data26/20221101_212208.Ch_B.004.dat", "r")
    #data = open("model_example/model_spectrum.dat", "r")
    #lines = data.readlines()
    #length = len(lines)
    #spectrum = list()

    # spectrum with all points
    #for i in range(length):
    #    spectrum.append(float(lines[i]))
    spectrum = np.array(spectrum)
    length = len(spectrum)
    freq = np.arange(0, length, 1)
    # reverse
    constant_array = np.ones(len(spectrum))*500000
    spectrum_reverse = constant_array - spectrum

    # interpolate
    baseline_reverse = pbl.polynomial.imodpoly(spectrum_reverse, freq, poly_order=3, tol=1e-6, max_iter=250, use_original=True)[0]
    baseline_imodpoly = constant_array - baseline_reverse
    #baseline_model_spectrum = (np.sum(spectrum)/len(spectrum))*np.ones_like(spectrum)
    #baseline_reverse = pbl.polynomial.quant_reg(spectrum_reverse, freq, poly_order=5, quantile=0.05)[0]
    #baseline_quantreg = constant_array - baseline_reverse
    #baseline_reverse = pbl.whittaker.iasls(spectrum_reverse, freq, lam=1e5, p=1e-4, lam_1=1e-4)[0]
    #baseline_iasls = constant_array - baseline_reverse
    #baseline_reverse = pbl.spline.irsqr(spectrum_reverse)[0]
    #baseline_irsqr = constant_array - baseline_reverse
    #baseline_reverse = pbl.classification.fastchrom(spectrum_reverse, half_window=100, threshold=1000)[0]
    #baseline_fastchrom = constant_array - baseline_reverse

    # plot
    baseline = baseline_imodpoly
    #baseline = baseline_model_spectrum
    plt.plot(freq, spectrum, '-', label='raw spectrum')
    #plt.plot(freq, baseline, '-', label='baseline imodpoly')
    #plt.plot(freq, baseline_cont_wavelet, '-', label='baseline cont wavelet')
    #plt.plot(freq, baseline_quantreg, '-', label='baseline quantreg')
    #plt.plot(freq, baseline_iasls, '-', label='baseline iasls')
    #plt.plot(freq, baseline_imodpoly, '-', label='baseline test')
    plt.legend()
    plt.show()

    #spectrum_normed = spectrum/baseline_imodpoly
    #label_normed ='normed spectrum (imodpoly)'
    #spectrum_normed = spectrum/baseline_quantreg
    #label_normed = 'normed spectrum (quantreg)'
    #spectrum_normed = spectrum/baseline_iasls
    #label_normed = 'normed spectrum (iasls)'
    spectrum_normed = spectrum/baseline
    label_normed = 'normed spectrum'
    plt.plot(freq, spectrum_normed, '-', linewidth=4, label=label_normed)
    plt.legend()
    plt.show()

    # spectral lines
    bspline = spi.splrep(freq, spectrum_normed, k=4)
    bspline_der1 = spi.splder(bspline, n=1)
    minimax = spi.sproot(bspline_der1, mest=10000)
    threshold = 0.0015             # min depth of spectral lines
    spectral_lines = list()
    for i in range(len(minimax)):
        if abs(spi.splev(minimax[i], bspline) - 1) > threshold:
            spectral_lines.append(minimax[i])
    spectral_lines.reverse()
    #print(spectral_lines)

    return (spectrum_normed, spectral_lines)

#get_normed_spectrum_and_line_positions()
