#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import baseline
import readdata
import fit
import emd
import config

raw_spectrum = readdata.get_spectrum(config.file_spectrum)
(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_spectrum)
print(line_positions)
hitran_lines = readdata.get_hitran_lines(config.file_hitran)
line_pos_part = list()
hitran_line_part = list()
#for a in [0, 6]:
#for a in [0, 1, 6]:
#for a in [0, 1, 6, 7]:
#for a in [0, 1, 2, 4, 6, 7]:
#for a in [0, 1, 2, 3, 4, 5]:
#for a in [0, 1, 2, 3, 4, 5, 6, 7]:
#    line_pos_part.append(line_positions[a])
#    hitran_line_part.append(hitran_lines[a])
#linearized_freq_scale = fit.get_lin_freq_scale(line_pos_part, hitran_line_part, len(spectrum_normed))
absorption_spectrum = (-1)*np.log(spectrum_normed)

# plot
#plt.plot(linearized_freq_scale, spectrum_normed, '-', label='normed spectrum')
#plt.stem(hitran_lines, np.ones(len(hitran_lines)), 'C1-')
#plt.legend()
#plt.show()
#plt.plot(linearized_freq_scale, absorption_spectrum, '-', label='absorption spectrum')
#plt.legend()
#plt.show()

# empirical mode decomposition
#emd.make_emd(absorption_spectrum)
emd.make_emd(spectrum_normed)

print("line positions = ", line_positions)
print("hitran lines = ", hitran_lines)
