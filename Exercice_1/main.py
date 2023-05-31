
# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On importe la fonction pour calculer l'aire sous
# from mod1 import aire_poly_rect


# Définitions des constantes
limite_inf = -2
limite_sup = 2
# Les coefficients p1, p2 et p3 sont des nombres réels
coef_p1 = 2
coef_p2 = 3
coef_p3 = 4
# Le coefficient p4 est un nombre réel positif
coef_p4 = 5
nb_seg = 10

# On calcule l'aire sous la courbe I selon la méthode exacte (méthode analytique)
def aire_poly_exacte(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4):
    resultat = coef_p1 * (limite_sup-limite_inf) + coef_p2 * ((limite_sup**2-limite_inf**2)/2) + coef_p3 * ((limite_sup**3-limite_inf**3)/3) + coef_p4 * ((limite_sup**4-limite_inf**4)/4)
    return resultat

resultat = aire_poly_exacte(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4)
print(resultat)