# Mini-Projet B - Analyse numérique
# Script contenant la fonction principale pour réaliser l'exercice 1
# Par: Gabriel Gunther et Alxandre Panhaleux
# Code permanent: GUNG19029902 et PANA87310001
# Date de remise: 6 juin 2023 à minuit

# Importation de bibliothèques additionnelles
import numpy as np
import matplotlib.pyplot as plt
import timeit

# On importe la fonction pour calculer l'aire sous
from mod1 import aire_poly_rect
from mod1 import erreur_integ
from mod1 import aire_poly_exacte
from mod1 import evolution_erreur

from mod1 import np_evolution_erreur


# Définitions des constantes
# Ont définie les limites inférieures et supérieures où l'on évalue la courbe
limite_inf = -2
limite_sup = 2
# Les 3 premiers coefficients sont des nombres réels. Le  4ème coefficient est un nombre réel positif
coefs = [2, 3, 4, 5]
# Nombre de segments avec lesquels ont veut diviser la plage définie par les limites inférieures et supérieures
# afin d'appliquer la méthode des rectangles pour évaluer l'aire sous la courbe
nb_seg = 100


resultat_methode_rect = aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg)
resultat_methode_exacte = aire_poly_exacte(limite_inf, limite_sup, coefs)
erreur_integration = erreur_integ(resultat_methode_rect, resultat_methode_exacte)
print(f'\nAvec la méthode des rectangles et {nb_seg} segments, l\'aire sous la courbe est {resultat_methode_rect}')
print(f'Avec la méthode exacte, l\'aire sous la courbe est {resultat_methode_exacte}')
print(f'L\'erreur d\'intégration est de {erreur_integration}')

evolution_error = evolution_erreur(limite_inf, limite_sup, coefs, nb_seg)
 
# Évaluation du temps d'exécution du script, avec les fonctions codées en python de base
# On affiche à l'utilisateur la valeur calculée
temps_execution_fonctions_base = timeit.timeit(lambda: aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: aire_poly_exacte(limite_inf, limite_sup, coefs), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: erreur_integ(resultat_methode_rect, resultat_methode_exacte), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: evolution_erreur(limite_inf, limite_sup, coefs, nb_seg), number = 1)
print(f"\nTemps requis pour exécuter le script avec les fonctions codées en python de base: {temps_execution_fonctions_base} secondes")

# Évaluation du temps d'exécution du script, avec les fonctions vectorisées et codées avec numpy
# On affiche à l'utilisateur la valeur calculée
temps_execution_avec_numpy = timeit.timeit(lambda: aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: aire_poly_exacte(limite_inf, limite_sup, coefs), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: erreur_integ(resultat_methode_rect, resultat_methode_exacte), number = 1)
temps_execution_fonctions_base = temps_execution_fonctions_base + timeit.timeit(lambda: np_evolution_erreur(limite_inf, limite_sup, coefs, nb_seg), number = 1)
print(f"\nTemps requis pour exécuter le script avec les fonctions avec numpy: {temps_execution_avec_numpy} secondes")

