#! /usr/bin/env python3

import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle
import baseline
import etalon
import lsq
import readdata
import config

# get normed spectrum
# (exclude baseline from raw spectrum)
raw_spectrum = readdata.get_spectrum(config.file_spectrum)
(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions(raw_spectrum)

# linearize freq scale
#maxes = etalon.get_etalon_maxes()
#freq_cm = const.etalon_const*np.arange(0, len(maxes), 1)
#freq_cm = max(freq_cm) - freq_cm
#bspline_etalon = spi.splrep(maxes, freq_cm, k=3)
#linearized_freq_scale = np.zeros_like(spectrum_normed)
#for i in range(len(linearized_freq_scale)):
#    linearized_freq_scale[i] = spi.splev(i, bspline_etalon)
#linearized_freq_scale = np.flip(linearized_freq_scale - min(linearized_freq_scale))
#spectrum_normed = np.flip(spectrum_normed)
#bspline_spectrum = spi.splrep(linearized_freq_scale, spectrum_normed, k=3)
#spectrum_linearized = np.zeros_like(spectrum_normed)
#step = (max(linearized_freq_scale) - min(linearized_freq_scale))/len(spectrum_normed)
#for i in range(len(spectrum_linearized)):
#    spectrum_linearized[i] = spi.splev(i*step, bspline_spectrum)
spectrum_linearized = spectrum_normed

# fast fourier transform
transform = np.fft.fft(spectrum_linearized)
transform_ampl = (np.real(transform)**2 + np.imag(transform)**2)**0.5
transform_ampl = transform_ampl[1:]
transform_angle = np.angle(transform)
plt.plot(transform_ampl, 'b-', label='FFT (amplitude)')
plt.legend()
plt.show()
# LombScargle
#frequency, power = LombScargle(np.arange(len(spectrum_linearized)), spectrum_linearized).autopower()
#plt.plot(frequency, power, 'b-', label='LombScargle')
#plt.legend()
#plt.show()

# fit linearized spectrum with sinusoidal signal
spectrum_linearized = lsq.shift_to_zero(spectrum_linearized)
print("frequency 1")
spectrum_linearized = lsq.fit_sin(spectrum_linearized[50:-100])
for a in range(1):
    print("frequency " + str(a+2))
    spectrum_linearized = lsq.shift_to_zero(spectrum_linearized)
    spectrum_linearized = lsq.fit_sin(spectrum_linearized)

# fast fourier transform (yes, again)
transform = np.fft.fft(spectrum_linearized)
transform_ampl = (np.real(transform)**2 + np.imag(transform)**2)**0.5
transform_ampl = transform_ampl[1:]
transform_angle = np.angle(transform)

# output
#print(maxes)
#print(linearized_freq_scale)
#plt.plot(maxes, freq_cm)
#plt.show()
#plt.plot(linearized_freq_scale, spectrum_normed, 'bo', label='linearized spectrum (1)')
#plt.legend()
#plt.show()
plt.plot(spectrum_linearized, 'b-', label='linearized spectrum (2)')
plt.legend()
plt.show()
plt.plot(transform_ampl, 'b-', label='FFT (amplitude)')
plt.legend()
plt.show()
#plt.plot(transform_angle, 'bo', label='FFT (angle)')
#plt.legend()
#plt.show()
