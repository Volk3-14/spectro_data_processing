import numpy as np
import model
import config

# function fits absorption spectrum
# and gets all final parameters
def get_parameters(exp_spectrum, hitran_data, freq_scale):
    # exp_spectrum - experimental absorption spectrum (numpy array)
    # hitran_data - dictionary with all data from HITRAN
    # {'freq':[], 'intensity':[], 'gamma_air':[], ...}
    # freq_scale - frequencies of all points in spectrum (numpy array)

    model_spectrum = model.model_spectrum(hitran_data, freq_scale)
    density = np.sum(exp_spectrum*model_spectrum)/np.sum(model_spectrum**2)/config.opt_path
    sigma_res = np.sum((exp_spectrum-model_spectrum*density*config.opt_path)**2)/350 #(len(exp_spectrum)-1)
    sigma_dens = sigma_res/config.opt_path/1.0e-21
    print("sigma_res = "+format(sigma_res, '6.3e'))
    return (density, sigma_dens, model_spectrum)
