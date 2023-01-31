import numpy as np

# frequency of etalon interference
# 1/(2L) in cm^(-1)
etalon_const = 0.025927

# array for optimal value search of param
# while fitting function
# y = alpha*x**(2*param) + beta*x + gamma
param_array = np.arange(0.51, 0.8, 0.001)
#param_array = np.arange(0.01, 0.2, 0.001)

# file with main spectrum
#file_spectrum = "model_example/model_spectrum.dat"
#file_spectrum = "data26/20221101_212208.Ch_A.000.dat"
file_spectrum = "data25/20221101_201220.Ch_A.002.dat"
#file_spectrum = "data10/20220722_160350.Ch_B.000.dat"
#file_spectrum = "data11/20220722_173703.Ch_B.000.dat"
#file_spectrum = "data25/20221101_201220.Ch_B.002.dat"
#file_spectrum = "data26/20221101_212208.Ch_B.004.dat"

# file with etalon spectrum
#file_etalon = "etalon/20220722_161044.Ch_B.000.dat"
#file_etalon = "etalon/20220722_161044.Ch_B.001.dat"
#file_etalon = "etalon/3762-3766_F-P.dat"
file_etalon = "etalon/20221101_194836.Ch_A.000.dat"

# file with a piece of HITRAN database
file_hitran = "hitran_lines.dat"
