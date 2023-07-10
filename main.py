#! /usr/bin/env python3

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#plt.rcParams.update({'font.size': 18})
import baseline
import readdata
import fit
#import emd
import filter_diff as fd
import config

raw_spectrum = readdata.get_spectrum(config.file_spectrum)
raw_empty_spectrum = readdata.get_spectrum(config.file_empty_spectrum)
raw_spectrum = fd.filterSG(raw_spectrum)
raw_empty_spectrum = fd.filterSG(raw_empty_spectrum)
(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_spectrum[100:-50])
(empty_spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_empty_spectrum[100:-50])
# least squares for parameter k determination
mean_spectrum = np.mean(spectrum_normed)
mean_empty = np.mean(empty_spectrum_normed)
s1 = np.sum((spectrum_normed[:1000] - mean_spectrum)*(empty_spectrum_normed[:1000] - mean_empty))
s2 = np.sum((spectrum_normed[1800:] - mean_spectrum)*(empty_spectrum_normed[1800:] - mean_empty))
s3 = np.sum((empty_spectrum_normed[:1000] - mean_empty)**2) + np.sum((empty_spectrum_normed[1800:] - mean_empty)**2)
k = (s1+s2)/s3
print("k = "+str(k))
corrected_spectrum = spectrum_normed - (empty_spectrum_normed - np.mean(empty_spectrum_normed))*k
plt.plot(corrected_spectrum, '-', label='corrected_spectrum', linewidth=5)
plt.legend()
plt.show()
#fd.filter_diff(raw_spectrum)
exit(0)
hitran_lines = readdata.get_hitran_lines(config.file_hitran)
line_pos_part = line_positions
hitran_line_part = hitran_lines
print(line_pos_part)
print(hitran_line_part)
#line_pos_part = list()
#hitran_line_part = list()
#for a in [0, 6]:
#for a in [0, 1, 6]:
#for a in [0, 1, 6, 7]:
#for a in [0, 1, 2, 4, 6, 7]:
#for a in [0, 1, 2, 3, 4, 5]:
#for a in [0, 1, 2, 3, 4, 5, 6, 7]:
#    line_pos_part.append(line_positions[a])
#    hitran_line_part.append(hitran_lines[a])
linearized_freq_scale = fit.get_lin_freq_scale(line_pos_part, hitran_line_part, len(spectrum_normed))
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
#emd.make_emd(spectrum_normed)

print("line positions = ", line_positions)
print("hitran lines = ", hitran_lines)
