# modeling of spectrum and LSQ

import numpy as np
import matplotlib.pyplot as plt
import const
import config


# shape function for spectral line
def shape_function(main_freq, freq_scale):
    # freq_scale - array with frequencies
    # main_freq - frequency of line center
    # line shape - numpy array with values of shape function

    # gaussian function
    alfa_doppler = main_freq/const.c*np.sqrt(2*const.Na*const.k*const.ln2*config.temp/config.mol_mass)
    #print(alfa_doppler)
    line_shape = (np.sqrt(const.ln2/const.pi)/alfa_doppler)*np.exp( -const.ln2*((freq_scale-main_freq)/alfa_doppler)**2)
    return line_shape


# function to model absorption lines
def model_spectrum(line_freq, line_S, freq_scale):
    # line_freq - array with line frequencies (HITRAN)
    # line_S - array with line intensities (HITRAN)
    # freq_scale - linearized freq scale (experiment)
    # returns synthetic spectrum

    # parameters from hitran
    # coefficient of pressure shift
    delta = [0.001]
    # coefficient of pressure broadening in air
    gamma_air = []
    # coefficient of pressure self-broadening
    gamma_self = []

    modeled_spectrum = 0
    for a in range(len(line_freq)):
        modeled_spectrum += line_S[a]*shape_function(line_freq[a], freq_scale)
    return modeled_spectrum



# line frequencies in vacuum
#freq = [6057.079548, 6057.091900, 6057.100400, 6057.126950]
# line intensities [cm^(-1)/(molecule*cm^(-2))]
#S = [1.520e-21, 8.244e-22, 6.631e-22, 9.077e-22]

#freq_min = 6056    # in cm^(-1)
#freq_max = 6058
#N = 4000
#freq_scale = np.arange(freq_min, freq_max, (freq_max-freq_min)/N)
#plt.plot(freq_scale, (fit_spectrum(freq, S, freq_scale)), '-', label='modeled spectrum')
#plt.legend()
#plt.show()
