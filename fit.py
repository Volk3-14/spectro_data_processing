#! /usr/bin/env python3

import math
import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt

# fit experimental data
# with function y = alpha*x**2p + beta*x + gamma
def fit_data(maxima, freq_cm, param_array):
    # maxima - list (array) of coordinates of maxima (spectrum with etalon)
    # freq_cm - numpy array of frequency in reciprocal centimeters
    # param_array - numpy array for optimal value search (of parameter param)
    length_maxima = len(maxima)
    RMSE_array = list()
    # least squares method
    # numerical solution for param
    # analitical - for alpha, beta, gamma
    for param in param_array:
        # analitical least squares method with fixed parameter param
        # supportive variables
        (a1, a2, a2_hat, a3, a4) = (0.0, 0.0, 0.0, 0.0, 0.0)
        (c0, c1, c2) = (0.0, 0.0, 0.0)
        for i in range(length_maxima):
            a1 += maxima[i]
            a2 += maxima[i]**(2*param)
            a2_hat += maxima[i]*maxima[i]
            a3 += maxima[i]**(2*param+1)
            a4 += maxima[i]**(4*param)
            c0 += freq_cm[i]
            c1 += freq_cm[i]*maxima[i]
            c2 += freq_cm[i]*(maxima[i]**(2*param))
        #print(a1, a2, a2_hat, a3, a4, c0, c1, c2)
        alpha = ((c2-c0*a2)*(a2_hat-a1*a1) - (c1-c0*a1)*(a3-a1*a2)) / ((a4-a2*a2)*(a2_hat-a1*a1) - (a3-a1*a2)**2)
        beta = (c1 - c0*a1 - alpha*(a3-a1*a2))/(a2_hat - a1*a1)
        gamma = c0 - alpha*a2 - beta*a1
        RMSE = 0.0
        for i in range(length_maxima):
            RMSE += (freq_cm[i] - alpha*maxima[i]**(2*param) - beta*maxima[i] - gamma)**2
        RMSE_array.append(RMSE)
        #print("alpha, beta, gamma, param, RMSE = ", alpha, beta, gamma, param, RMSE)


    # take extremum from spline by derivative
    bspline = spi.splrep(param_array ,RMSE_array, k=4)
    bspline_der1 = spi.splder(bspline, n=1)
    param = spi.sproot(bspline_der1)[0]
    # take minimum "integer" point
    #RMSE = min(RMSE_array)
    #param = param_array[RMSE_array.index(RMSE)]
    (a1, a2, a2_hat, a3, a4) = (0.0, 0.0, 0.0, 0.0, 0.0)
    (c0, c1, c2) = (0.0, 0.0, 0.0)
    for i in range(length_maxima):
        a1 += maxima[i]
        a2 += maxima[i]**(2*param)
        a2_hat += maxima[i]*maxima[i]
        a3 += maxima[i]**(2*param+1)
        a4 += maxima[i]**(4*param)
        c0 += freq_cm[i]
        c1 += freq_cm[i]*maxima[i]
        c2 += freq_cm[i]*(maxima[i]**(2*param))
    alpha = ((c2-c0*a2)*(a2_hat-a1*a1) - (c1-c0*a1)*(a3-a1*a2)) / ((a4-a2*a2)*(a2_hat-a1*a1) - (a3-a1*a2)**2)
    beta = (c1 - c0*a1 - alpha*(a3-a1*a2))/(a2_hat - a1*a1)
    gamma = c0 - alpha*a2 - beta*a1
    RMSE = 0.0
    for i in range(length_maxima):
        RMSE += (freq_cm[i] - alpha*maxima[i]**(2*param) - beta*maxima[i] - gamma)**2
    print("param = ", param, "    RMSE = ", RMSE)
    print("alpha, beta, gamma = ", alpha, beta, gamma)


    # plot
    plt.plot(param_array, RMSE_array, 'o', label='RMSE(p)')
    plt.legend()
    plt.show()

    # return list of max positions
    return (alpha, beta, gamma, param, RMSE)


# calculate function fitted with etalon data
def calc_fit(coeffs, x):
    alpha = coeffs[0]
    beta = coeffs[1]
    gamma = coeffs[2]
    param = coeffs[3]
    return alpha*x**(2*param) + beta*x + gamma


# get coefficients for final function
# (number of point) -> cm**(-1)
# fitted with etalon data and line positions (+HITRAN)
#
# get array of frequencies in cm^(-1)
# for spectrum (with <length> points)
def get_freq_array(lines, hitran_lines, coeffs, length):
    # solve linear system
    matrix = list()
    for i in range(len(lines)):
        f = calc_fit(coeffs, lines[i])
        matrix.append(list())
        for j in range(len(lines)):
            matrix[i].append(f**j)
    coeff_array = np.linalg.solve(matrix, hitran_lines)
    #print('matrix = ', matrix)
    print('coeff_array = ', coeff_array)

    # calculate frequency array
    numbers = np.arange(float(length))
    freq_array = np.zeros_like(numbers)
    for i in range(length):
        f = calc_fit(coeffs, numbers[i])
        for j in range(len(lines)):
            freq_array[i] += coeff_array[j]*(f**j)
        #if (i < min(lines)) or (i > max(lines)):
        #    # linear extrapolation
        #    freq_array[i] = coeff_array[0] + coeff_array[1]*f
        #else:
        #    for j in range(len(lines)):
        #        freq_array[i] += coeff_array[j]*(f**j)

    # plot
    #numbers = np.arange(0, length, 0.1)
    #freq = np.zeros_like(numbers)
    #for i in range(len(numbers)):
    #    f = calc_fit(coeffs, numbers[i])
    #    for j in range(len(lines)):
    #        freq[i] += coeff_array[j]*(f**j)
    plt.plot(numbers, freq_array, '-', label='fitted function')
    plt.plot(lines, hitran_lines, 'o', label='exp data (+hitran)')
    plt.legend()
    plt.show()

    return freq_array

