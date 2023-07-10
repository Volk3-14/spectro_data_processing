import numpy as np

# frequency of etalon interference
# 1/(2L) in cm^(-1)
#etalon_const = 0.025927
etalon_const = 0.05

# array for optimal value search of param
# while fitting function
# y = alpha*x**(2*param) + beta*x + gamma
param_array = np.arange(0.51, 0.8, 0.001)
#param_array = np.arange(0.01, 0.2, 0.001)

# file with main spectrum
datadir = "/home/pavel/workdir/IKI/spectro_data_processing/data/"
#file_spectrum = "model_example/model_spectrum.dat"
#file_spectrum = datadir + "data26/20221101_212208.Ch_A.000.dat"
#file_spectrum = datadir + "data25/20221101_201220.Ch_A.002.dat"
#file_spectrum = datadir + "data10/20220722_160350.Ch_B.000.dat"
#file_spectrum = datadir + "data11/20220722_173703.Ch_B.000.dat"
#file_spectrum = datadir + "data25/20221101_201220.Ch_B.002.dat"
#file_spectrum = datadir + "data26/20221101_212208.Ch_B.004.dat"
#file_spectrum = datadir + "data27/20230425_171127.Ch_B.000.dat"
#file_spectrum = datadir + "data27/20230425_171313.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_160246.Ch_B.000.dat"
# атмосферный метан
#file_spectrum = datadir + "data28/20230502_160351.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_160604.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_173953.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_175327.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_181657.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_181830.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_182002.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_184842.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_211817.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_211936.Ch_B.000.dat"
#file_spectrum = datadir + "data28/20230502_221222.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_200434.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_200625.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_202543.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_202800.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_202922.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_210044.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_210203.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_212726.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_212819.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_213122.Ch_B.000.dat"
#file_spectrum = datadir + "data29/20230503_213241.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_161553.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_161711.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_164847.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_170034.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_172548.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_172706.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_172810.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_180718.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_182135.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_182745.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_185525.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_185903.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_190020.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_191243.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_191505.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_205905.Ch_B.000.dat"
#file_spectrum = datadir + "data30/20230504_210717.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_164037.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_165251.Ch_B.000.dat"
#file_spectrum = datadir + "data31/20230505_165537.Ch_B.000.dat"
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
file_hitran = datadir + "hitran_lines_CH4.dat"
