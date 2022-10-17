#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import baseline
import etalon
import readdata
import fit

#(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions()
(alpha, beta, gamma, param)  = etalon.get_coeffs()
coeffs = (alpha, beta, gamma, param)
hitran_lines = readdata.get_hitran_lines()
line_pos_part = list()
hitran_line_part = list()
#for a in [0, 1, 6]:
#for a in [0, 1, 6, 7]:
#for a in [0, 1, 2, 4, 6, 7]:
for a in [0, 1, 2, 3, 4, 5]:
    line_pos_part.append(line_positions[a])
    hitran_line_part.append(hitran_lines[a])
freq_array = fit.get_freq_array(line_pos_part, hitran_line_part, coeffs, len(spectrum_normed))
#linearized_freq_scale = fit.get_lin_freq_scale(line_pos_part, hitran_line_part, len(spectrum_normed)
# plot
#plt.plot(freq_array, spectrum_normed, '-', label='spectrum_normed')
#plt.stem(hitran_lines, np.ones(len(hitran_lines)), 'C1-')
#plt.legend()
#plt.show()
#z = np.arange(0, 3300, 0.1)
#fit = (alpha*z**(2*param) + beta*z + gamma)*0.96
#plt.plot(z, fit, '-', label='fit')
#plt.plot(line_positions, np.array(hitran_lines)-hitran_lines[0] + 0.96*(alpha*line_positions[0]**(2*param) + beta*line_positions[0] + gamma), 'o')
#plt.legend()
#plt.show()

print("line positions = ", line_positions)
print("hitran lines = ", hitran_lines)
