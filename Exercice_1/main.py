
# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import timeit

# On importe la fonction pour calculer l'aire sous
# from mod1 import aire_poly_rect

from mod1 import aire_poly_rect
from mod1 import error_integ
from mod1 import aire_poly_exacte
from mod1 import evolution_erreur

# Définitions des constantes
limites = [-2, 2]
# Les coefficients p1, p2 et p3 sont des nombres réels
coefs = [2, 3, 4, 5]
# Le coefficient p4 est un nombre réel positif
nb_seg = 100


resultat = aire_poly_rect(limites, coefs, nb_seg)
resultat_anal = aire_poly_exacte(limites, coefs)
print(resultat)
print(resultat_anal)
print(error_integ(resultat, resultat_anal))

evolution_error = evolution_erreur(limites, coefs)

print(timeit.timeit(lambda: aire_poly_rect(limites, coefs, nb_seg), number = 1))
