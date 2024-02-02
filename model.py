# modeling of spectrum and LSQ

import numpy as np
import matplotlib.pyplot as plt
import const
import config


# gaussian shape function for spectral line
def gauss(main_freq, freq_scale):
    # freq_scale - array with frequencies
    # main_freq - frequency of line center
    # line shape - numpy array with values of shape function

    # gaussian function
    alfa_doppler = main_freq/const.c*np.sqrt(2*const.Na*const.k*const.ln2*config.temp/config.mol_mass)
    line_shape = (np.sqrt(const.ln2/const.pi)/alfa_doppler)*np.exp( -const.ln2*((freq_scale-main_freq)/alfa_doppler)**2)
    return line_shape


# lorentz shape function for spectral line
def lorentz(data, a, freq_scale):
    # freq_scale - numpy array with frequencies
    # data - hitran data with line parameters
    # {'freq': [], 'intensity': [], 'gamma_air': [], ... }
    # a - number of line in dataset

    # lorentzian function
    gamma = ((const.temp_ref/config.temp)**data['n_air'][a]) \
            *(data['gamma_air'][a]*(config.press - config.press_self)+data['gamma_self'][a]*config.press_self)
    line_shape = gamma/const.pi/(gamma**2+(freq_scale-data['freq'][a])**2)
    return line_shape


# function to model absorption lines
def model_spectrum(hitran_data, freq_scale):
    # hitran_data - dictionary with several parameters (HITRAN)
    # freq_scale - linearized freq scale (experiment) (numpy array)
    # returns synthetic spectrum (numpy array)

    freq_scale  = np.array(freq_scale)
    modeled_spectrum = 0
    for a in range(len(hitran_data['freq'])):
        #modeled_spectrum += hitran_data['intensity'][a]*gauss(hitran_data['freq'][a], freq_scale)
        modeled_spectrum += hitran_data['intensity'][a]*lorentz(hitran_data, a, freq_scale)
    return np.array(modeled_spectrum)



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
