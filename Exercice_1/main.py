
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
limite_inf = -2
limite_sup = 2
# Les coefficients p1, p2 et p3 sont des nombres réels
coef_p1 = 2
coef_p2 = 3
coef_p3 = 4
# Le coefficient p4 est un nombre réel positif
coef_p4 = 5
nb_seg = 100


resultat = aire_poly_rect(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4, nb_seg)
resultat_anal = aire_poly_exacte(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4)
print(resultat)
print(resultat_anal)
print(error_integ(resultat, resultat_anal))

evolution_error = evolution_erreur(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4)

print(timeit.timeit(lambda: evolution_erreur(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4), number = 1000))
