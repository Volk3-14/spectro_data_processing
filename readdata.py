# read hitran data file and get frequencies
def get_hitran_lines():
    inf = open("hitran_lines.dat", "r")
    strings = inf.readlines()
    hitran_lines = list()
    for string in strings:
        hitran_lines.append(float(string.split()[2]))
    return hitran_lines

#print(get_hitran_lines())
