import math
import scipy.interpolate as spi
import numpy as np
import matplotlib.pyplot as plt
import etalon
import config

# fit experimental data
# with function freq = alpha*x**2p + beta*x + gamma
# returns alpha, beta, gamma, p and RMSE
def fit_data(maxes, freq_cm, param_array):
    # maxes - list (array) of coordinates of maxima (spectrum with etalon)
    # freq_cm - numpy array of frequency in reciprocal centimeters
    # param_array - numpy array for optimal value search (of parameter param)
    length_maxes = len(maxes)
    RMSE_array = list()
    # least squares method
    # numerical solution for param
    # analitical - for alpha, beta, gamma
    for param in param_array:
        # analitical least squares method with fixed parameter param
        # supportive variables
        (a1, a2, a2_hat, a3, a4) = (0.0, 0.0, 0.0, 0.0, 0.0)
        (c0, c1, c2) = (0.0, 0.0, 0.0)
        for i in range(length_maxes):
            a1 += maxes[i]
            a2 += maxes[i]**(2*param)
            a2_hat += maxes[i]*maxes[i]
            a3 += maxes[i]**(2*param+1)
            a4 += maxes[i]**(4*param)
            c0 += freq_cm[i]
            c1 += freq_cm[i]*maxes[i]
            c2 += freq_cm[i]*(maxes[i]**(2*param))
        #print(a1, a2, a2_hat, a3, a4, c0, c1, c2)
        alpha = ((c2-c0*a2)*(a2_hat-a1*a1) - (c1-c0*a1)*(a3-a1*a2)) / ((a4-a2*a2)*(a2_hat-a1*a1) - (a3-a1*a2)**2)
        beta = (c1 - c0*a1 - alpha*(a3-a1*a2))/(a2_hat - a1*a1)
        gamma = c0 - alpha*a2 - beta*a1
        RMSE = 0.0
        for i in range(length_maxes):
            RMSE += (freq_cm[i] - alpha*maxes[i]**(2*param) - beta*maxes[i] - gamma)**2
        RMSE_array.append(RMSE)
        #print("alpha, beta, gamma, param, RMSE = ", alpha, beta, gamma, param, RMSE)

    # plot
    plt.plot(param_array, RMSE_array, 'o', label='RMSE(p)')
    plt.legend()
    plt.show()

    # take extremum from spline by derivative
    bspline = spi.splrep(param_array ,RMSE_array, k=4)
    bspline_der1 = spi.splder(bspline, n=1)
    param = spi.sproot(bspline_der1)[0]
    # take minimum "integer" point
    #RMSE = min(RMSE_array)
    #param = param_array[RMSE_array.index(RMSE)]
    (a1, a2, a2_hat, a3, a4) = (0.0, 0.0, 0.0, 0.0, 0.0)
    (c0, c1, c2) = (0.0, 0.0, 0.0)
    for i in range(length_maxes):
        a1 += maxes[i]
        a2 += maxes[i]**(2*param)
        a2_hat += maxes[i]*maxes[i]
        a3 += maxes[i]**(2*param+1)
        a4 += maxes[i]**(4*param)
        c0 += freq_cm[i]
        c1 += freq_cm[i]*maxes[i]
        c2 += freq_cm[i]*(maxes[i]**(2*param))
    alpha = ((c2-c0*a2)*(a2_hat-a1*a1) - (c1-c0*a1)*(a3-a1*a2)) / ((a4-a2*a2)*(a2_hat-a1*a1) - (a3-a1*a2)**2)
    beta = (c1 - c0*a1 - alpha*(a3-a1*a2))/(a2_hat - a1*a1)
    gamma = c0 - alpha*a2 - beta*a1
    RMSE = 0.0
    for i in range(length_maxes):
        RMSE += (freq_cm[i] - alpha*maxes[i]**(2*param) - beta*maxes[i] - gamma)**2
    #print("param = ", param, "    RMSE = ", RMSE)
    #print("alpha, beta, gamma = ", alpha, beta, gamma)

    # return list of coefficients
    return (alpha, beta, gamma, param, RMSE)


# calculate function fitted with etalon data
def calc_fit(alpha, beta, gamma, param, x):
    return alpha*x**(2*param) + beta*x + gamma


# get coefficients for final function
# (number of point) -> cm**(-1)
# fitted with etalon data and line positions (+HITRAN)
#
# get array of frequencies in cm^(-1)
# for spectrum (with <length> points)
def get_lin_freq_scale(lines, hitran_lines, length):

    # get etalon maxes
    maxes = etalon.get_etalon_maxes()
    # get array with frequencies of etalon in cm^(-1)
    length_maxima = len(maxes)
    freq_cm = config.etalon_const*np.arange(0, length_maxima, 1)

    # get fitting function
    #(alpha, beta, gamma, param, RMSE) = fit_data(maxes, freq_cm, const.param_array)
    # it is more convenient to fit function in such view
    # but in real life function is different: y -> y_max - y
    freq_cm = max(freq_cm) - freq_cm
    bspline = spi.splrep(maxes ,freq_cm, k=3)
    #alpha = - alpha
    #beta = - beta
    #gamma = freq_cm[length_maxima-1] - gamma

    # solve linear system
    #########################
    matrix = list()
    for i in range(len(lines)):
        #f = calc_fit(alpha, beta, gamma, param, lines[i])
        f = spi.splev(lines[i], bspline, der=0, ext=0)
        matrix.append(list())
        for j in range(len(lines)):
            matrix[i].append(f**j)

    # check if there are more hitran lines, than experimental
    # delete the weakest lines
    while len(lines) < len(hitran_lines['freq']):
        minimum = hitran_lines['maxes'][0]
        index_min = 0
        for i in range(1, len(hitran_lines['freq'])):
            if hitran_lines['maxes'][i] < minimum:
                minimum = hitran_lines['maxes'][i]
                index_min = i
        hitran_lines['freq'] = np.delete(hitran_lines['freq'], index_min)
        hitran_lines['maxes'] = np.delete(hitran_lines['maxes'], index_min)
        #print(hitran_lines)

    coeff_array = np.linalg.solve(matrix, hitran_lines['freq'])
    #print('coeff_array = ', coeff_array)
    if len(coeff_array) == 1:
        coeff_array = np.append(coeff_array, 1.0)
        coeff_array[0] -= spi.splev(lines[0], bspline, der=0, ext=0)
    #print('coeff_array = ', coeff_array)

    # calculate frequency array
    numbers = np.arange(float(length))
    freq_array = np.zeros_like(numbers)
    for i in range(length):
        #f = calc_fit(alpha, beta, gamma, param, numbers[i])
        f = spi.splev(numbers[i], bspline, der=0, ext=0)
        for j in range(len(coeff_array)):
            freq_array[i] += coeff_array[j]*(f**j)

    # plot
    #print("maxes = " + str(maxes))
    #plt.plot(maxes, freq_cm, 'o', label='frequency, cm^(-1)')
    y = [freq_cm[0], freq_cm[len(freq_cm)-1]]
    x = [maxes[0], maxes[length_maxima-1]]
    #plt.plot(x, y, '-', label='straight line')
    z = np.arange(min(maxes), max(maxes), 1)
    ###fit = alpha*z**(2*param) + beta*z + gamma
    fit = spi.splev(z, bspline, der=0, ext=0)
    #plt.plot(z, fit, '-', label='fit')
    #plt.legend()
    #plt.show()
    # first derivative
    fit_der1 = spi.splev(z, bspline, der=1, ext=0)
    #plt.plot(z, fit_der1, '-', label='fit derivative 1')
    #plt.legend()
    #plt.show()
    # second derivative
    #fit_der2 = spi.splev(z, bspline, der=2, ext=0)
    #plt.plot(z, fit_der2, '-', label='fit derivative 2')
    #plt.legend()
    #plt.show()
    # residual
    maxes = np.array(maxes)
    #fit2 = alpha*maxes**(2*param) + beta*maxes + gamma
    fit2 = spi.splev(maxes, bspline, der=0, ext=0)
    #plt.plot(maxes, freq_cm-fit2, 'o', label='etalon points - fit')
    #plt.legend()
    #plt.show()

    #plt.plot(numbers, freq_array, '-', label='fitted function')
    #plt.plot(lines, hitran_lines, 'o', label='exp data (+hitran)')
    #plt.legend()
    #plt.show()

    return freq_array
