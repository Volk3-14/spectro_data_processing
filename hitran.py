#! /usr/bin/env python3

base = open("hitran_base_3589_3590.5_H2O_CO2.out", "r")
out = open("hitran_base_cut", "w")
lines = base.readlines()
for i in range(1, len(lines)):
    spectral_intens = float(lines[i].split()[3])
    if spectral_intens > 1.0e-24:
        out.write(lines[i])
