#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# fit spectrum with fucntion y = A*sin(wx) + B*cos(wx)
def fit_sin(spectrum):
    N = len(spectrum)      # number of points
    error_min = 0.0        # sum of square errors
    for i in range(N):
        error_min += spectrum[i]*spectrum[i]
    omega_init = 0.0
    omega_final = 0.4
    omega_min = (omega_init + omega_final)/2
    step = (omega_final - omega_init)/4
    error_min_old = error_min + 1
    A_min = 1.0                   # A, corresponding to minimal square error
    B_min = 1.0                   # B, corresponding to minimal square error
    A_old = A_min
    B_old = B_min
    a = 1
    while (a <= 5) or (abs((A_min - A_old)/A_old) + abs((B_min - B_old)/B_old) > 1.0e-9):
        a += 1
        omega_init = omega_min - 2*step
        if omega_init < 0.0:
            omega_init = 0.0
        omega_final = omega_min + 2*step
        step = (omega_final - omega_init)/200
        error_min_old = error_min
        error_arr = list()
        omega = omega_init + step
        A_old = A_min
        B_old = B_min
        while omega < (omega_final + step/2):
            (sin, cos, cosin, sy, cy) = (0.0, 0.0, 0.0, 0.0, 0.0)
            for i in range(N):
                sin += 1 - np.cos(2*omega*i)
                cos += 1 + np.cos(2*omega*i)
                cosin += np.sin(2*omega*i)
                sy += spectrum[i]*np.sin(omega*i)
                cy += spectrum[i]*np.cos(omega*i)
            sin /= 2
            cos /= 2
            cosin /= 2
            B = (cy*sin - sy*cosin)/(cos*sin - cosin*cosin)
            A = (sy - B*cosin)/sin
            error_sq = 0.0
            for i in range(N):
                error_sq += (spectrum[i] - A*np.sin(omega*i) - B*np.cos(omega*i))**2
            if error_sq < error_min:
                error_min = error_sq
                omega_min = omega
                A_min = A
                B_min = B
            error_arr.append(error_sq)
            omega += step
        print("omega min = %22.16e" % omega_min, "square error = %22.16e" % error_min)
        print("A_min = %22.16e" % A_min, "B_min = %22.16e" % B_min)
        #plt.plot(np.arange(omega_init+step, omega_final+step/2, step), error_arr, label='error array')
        #plt.legend()
        #plt.show()
    plt.plot(spectrum, 'b-', label='spectrum')
    ind = np.arange(N)
    fit = A*np.sin(omega_min*ind) + B*np.cos(omega_min*ind)
    plt.plot(fit, 'r-', label='fit')
    plt.legend()
    plt.show()
    return (spectrum - fit)


def shift_to_zero(spectrum):
    mean = np.sum(spectrum)/len(spectrum)
    spectrum = spectrum - mean
    print("mean = " + str(mean))
    #plt.plot(spectrum, 'b-', label='linearized spectrum shifted to zero')
    #plt.legend()
    #plt.show()
    return spectrum
