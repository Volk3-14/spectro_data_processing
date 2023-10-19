import numpy as np

# frequency of etalon interference
# 1/(2L) in cm^(-1)
# germanium etalon (?)
#etalon_const = 0.025927
# quartz etalon (?)
etalon_const = 0.05

# temperature in Kelvins
temp = 296

# molecular mass in g/mol
mol_mass = 16

# array for optimal value search of param
# while fitting function
# y = alpha*x**(2*param) + beta*x + gamma
param_array = np.arange(0.51, 0.8, 0.001)
#param_array = np.arange(0.01, 0.2, 0.001)

# file with main spectrum
datadir = "/home/pavel/workdir/IKI/spectro_data_processing/data/"
# атмосферный метан
#file_spectrum = datadir + "data28/20230502_160351.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_170058.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_170310.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_174034.Ch_B.000.dat"
#
#file_spectrum = datadir + "data31/20230505_175509.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_175601.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_175627.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_180302.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_180353.Ch_B.000.dat"
#file_spectrum = datadir + "data32/20230516_203423.Ch_B.000.dat"
#file_spectrum = datadir + "data32/20230522_221228.Ch_B.000.dat"
file_spectrum = datadir + "data32/20230517_210651.Ch_B.000.dat"

# file with additional empty spectrum
# to fight with interference
file_empty_spectrum = datadir + "data32/20230516_204530.Ch_B.000.dat"
#file_empty_spectrum = datadir + "data32/20230517_210006.Ch_B.000.dat"

# file with etalon spectrum
#file_etalon = "etalon/20220722_161044.Ch_B.000.dat"
#file_etalon = "etalon/20220722_161044.Ch_B.001.dat"
#file_etalon = "etalon/3762-3766_F-P.dat"
#file_etalon = "etalon/20221101_194836.Ch_A.000.dat"
#file_etalon = datadir + "data28/20230502_160246.Ch_B.000.dat"
file_etalon = datadir + "data31/20230505_165251.Ch_B.000.dat"
#file_etalon = datadir + "data32/20230522_221228.Ch_B.000.dat"

# file with a piece of HITRAN database
#file_hitran = datadir + "hitran_lines.dat"
file_hitran = datadir + "hitran_lines_CH4.dat.orig"
