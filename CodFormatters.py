import math
import os
import numpy as np


def calcular_area_radio(radio):
    return math.pi * radio**2


def suma_matrices(m1, m2):
    return m1 + m2


print("Área del círculo con radio 5:", calcular_area_radio(5))

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
print("\nLa suma de matrices es\n", suma_matrices(matriz1, matriz2))
