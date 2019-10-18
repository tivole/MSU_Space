import numpy as np

def polar(x, y):
    r = np.sqrt(x**2 + y**2)
    phi = -666

    if y >= 0 and r != 0:
        phi = np.arccos(x/r)
    elif y < 0:
        phi = (-1)*np.arccos(x/r)
    else:
        phi = 0

    return (r, phi)