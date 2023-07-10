#!/usr/bin/env python3

import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt
from pyemd import emd
import readdata
import config

def make_emd(spectrum):
    # empirical mode decomposition
    emd = emd()
    Emfs = emd(spectrum)

    # correlation coefficient
    mean_spectrum = np.mean(spectrum)
    std_spectrum = np.std(spectrum)
    corr_coeff = list()
    for i in range(len(Emfs)-1):
        mean_mode = np.mean(Emfs[i])
        std_mode = np.std(Emfs[i])
        coeff = np.mean((spectrum-mean_spectrum)*(Emfs[i]-mean_mode))/(std_spectrum*std_mode)
        corr_coeff.append(coeff)
        print("mode "+str(i)+"   corr coeff = "+str(coeff))

    cleaned_spectrum = Emfs[-1]
    corr_cutoff = 0.4
    #for i in range(len(Emfs)-4):
        #if corr_coeff[i] < corr_cutoff:
    #    cleaned_spectrum = cleaned_spectrum + Emfs[i]
    # print and plot
    plt.plot(spectrum, label='input EMD spectrum')
    plt.legend()
    plt.show()
    for i in range(len(Emfs)-1):
        plt.plot(Emfs[i]-2*std_spectrum*i, label="mode "+str(i))
    plt.legend()
    plt.show()
    plt.plot(Emfs[-1], label='residual')
    plt.legend()
    plt.show()
    plt.plot(spectrum-mean_spectrum, label = 'input EMD spectrum')
    plt.plot(np.sum(Emfs, axis=0)-Emfs[-1], label='sum of modes')
    plt.plot(Emfs[-1]-mean_spectrum, label='residual')
    #plt.plot(cleaned_spectrum-mean_spectrum, label='cleaned spectrum')
    plt.legend()
    plt.show()
    return 0

# read spectrum from file
spectrum = np.array(readdata.get_spectrum(config.file_spectrum))
make_emd(spectrum)
