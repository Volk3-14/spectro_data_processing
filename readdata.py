import numpy as np

# read spectrum
def get_spectrum(filename):
    inf = open(filename, "r")
    spectrum = list()
    while(1):
        line = inf.readline()
        if line == '': break
        spectrum.append(float(line))
    inf.close()
    return spectrum


# read hitran data file and get frequencies
def get_hitran_lines(filename):
    inf = open(filename, "r")
    strings = inf.readlines()
    hitran_lines = list()
    for string in strings:
        hitran_lines.append(float(string.split()[2]))
    inf.close()
    return hitran_lines

#print(get_hitran_lines())
