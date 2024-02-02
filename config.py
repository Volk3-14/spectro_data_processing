import numpy as np

##################################
# physical parameters of substance
##################################
# temperature in Kelvins
temp = 296
# molecular mass in g/mol
mol_mass = 18
# pressure in atm
press = 0.012
# partial pressure of measured gas
press_self = 1.0
# density of measured gas in particles/cm^(-3)
density_init = 4.2e17
# measured isotopologies
iso_list = [{'name': 'H2O(16)', 'code': (1, 1), 'dens': 0.997*density_init},   \
            {'name': 'H2O(18)', 'code': (1, 2), 'dens': 2.0e-3*density_init},  \
            {'name': 'H2O(17)', 'code': (1, 3), 'dens': 3.72e-4*density_init}, \
            {'name': 'HDO(16)', 'code': (1, 4), 'dens': 3.11e-4*density_init}]



##################################
# technical parameters of sensor
##################################
# frequency of etalon interference
# 1/(2L) in cm^(-1)
# germanium etalon (?)
etalon_const = 0.025927
# quartz etalon (?)
#etalon_const = 0.05
# optical path length in cm
opt_path = 19
# spontanious emission (in parrots)
spontan = 11     # serie 1


##################################
# some important files with data
##################################
# directory with all data files
datadir = "/home/pavel/workdir/IKI/spectro_data_processing/data_moon/Luna_sp3"

# directory with raw spectra
#dir_spectra = datadir + "/ex"
#dir_spectra = datadir + "/S1/12mbar_H2O"
dir_spectra = datadir + "/S1/16mbar_H2O"
#dir_spectra = datadir + "/S2/12mbar_H2O"

# file with etalon spectrum
file_etalon = datadir + "/J-FP_1.txt"

# file with a piece of HITRAN database
#file_hitran = datadir + "hitran_lines_CH4.dat"
file_hitran = datadir + "/S1/hitran_3792_3794_H2O_cut"
