#! /usr/bin/env python3

import numpy as np
import scipy as sp
import scipy.fft
import matplotlib.pyplot as plt
import baseline
import readdata
import fit
import filter_diff as fd
import config
import lib

raw_spectrum = readdata.get_spectrum(config.file_spectrum)
raw_spectrum = fd.filterSG(raw_spectrum)
(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_spectrum[100:-50])

hitran = readdata.get_hitran_parameters(config.file_hitran)
hitran_lines = readdata.get_hitran_lines(hitran)
print(hitran_lines)
line_pos_part = line_positions
hitran_line_part = hitran_lines
linearized_freq_scale = fit.get_lin_freq_scale(line_pos_part, hitran_line_part, len(spectrum_normed))
absorption_spectrum = (-1)*np.log(spectrum_normed)
#modeled_spectrum = model.fit_spectrum(hitran_lines, hitran_S, linearized_freq_scale)

plt.plot(linearized_freq_scale, absorption_spectrum, '-', label='absorption spectrum')
plt.legend()
plt.show()
