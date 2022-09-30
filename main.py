#! /usr/bin/env python3

import baseline
import etalon
import readdata

#(spectrum_normed, line_positions) = baseline.get_normed_spectrum_and_line_positions()
etalon_maxes = etalon.get_max_positions()
hitran_lines = readdata.get_hitran_lines()

#print("line positions = ", line_positions)
#print("etalon maxes = ", etalon_maxes)
#print("hitran lines = ", hitran_lines)
