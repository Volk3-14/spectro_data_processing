#! /usr/bin/env python3

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import baseline
import readdata
import fit
import filter_diff as fd
import model
import lsq_main as lsq
import config
import const

raw_spectrum = readdata.get_spectrum(config.file_spectrum)
raw_spectrum = fd.filterSG(raw_spectrum)
(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_spectrum[100:-50])

# data from database
hitran = readdata.get_hitran_parameters(config.file_hitran)
# lines from modeled spectrum
hitran_lines = readdata.get_hitran_lines(hitran)
#print(hitran)
line_pos_part = line_positions
hitran_line_part = hitran_lines
linearized_freq_scale = fit.get_lin_freq_scale(line_pos_part, hitran_line_part, len(spectrum_normed))
absorption_spectrum = (-1)*np.log(spectrum_normed)
(density, sigma, modeled_spectrum) = lsq.get_parameters(absorption_spectrum, hitran, linearized_freq_scale)
density_ppm = 1.0e6*density/(const.press_ref_sgs/const.k/config.temp)
sigma_ppm = 1.0e6*sigma/(const.press_ref_sgs/const.k/config.temp)
print("density = "+format(density, '6.3e'))
print("density = "+format(density_ppm, '6.3f')+"ppm")
print("sigma = "+format(sigma, '6.3e'))
print("sigma = "+format(sigma_ppm, '6.3e')+"ppm")

plt.plot(linearized_freq_scale, absorption_spectrum, '-', label='absorption spectrum')
plt.legend()
plt.show()
plt.plot(linearized_freq_scale, modeled_spectrum, '-', label='modeled spectrum')
plt.legend()
plt.show()
plt.plot(linearized_freq_scale, absorption_spectrum, '-', linewidth=4, label='absorption spectrum')
plt.plot(linearized_freq_scale, density*config.opt_path*modeled_spectrum, '-', linewidth=4, label='modeled spectrum')
plt.legend()
plt.show()
plt.plot(linearized_freq_scale, absorption_spectrum-density*config.opt_path*modeled_spectrum, '-', label='difference')
plt.legend()
plt.show()
