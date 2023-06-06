# Mini-Projet B - Analyse numérique
# Script contenant la fonction principale pour réaliser l'exercice 1
# Par: Gabriel Gunther et Alxandre Panhaleux
# Code permanent: GUNG19029902 et PANA87310001
# Date de remise: 6 juin 2023 à minuit

# Importation de bibliothèques additionnelles
import numpy as np
import matplotlib.pyplot as plt
import timeit

# Importation des fonctions codées en python de base
from mod1 import aire_poly_rect
from mod1 import erreur_integ
from mod1 import aire_poly_exacte
from mod1 import evolution_erreur
from mod1 import temps_exec_evolution_erreur
# Importation des fonctions codées avec numpy
from mod1 import np_tableau_nb_segments
from mod1 import np_aire_poly_rect
from mod1 import np_evolution_erreur
from mod1 import np_temps_execution


'''DÉFINITION DES CONSTANTES'''
# Ont définie les limites inférieures et supérieures où l'on évalue la courbe
limite_inf = -2
limite_sup = 2
# Les 3 premiers coefficients sont des nombres réels. Le  4ème coefficient est un nombre réel positif
coefs = [2, 3, 4, 5]
# Nombre de segments avec lesquels ont veut diviser la plage définie par les limites inférieures et supérieures
# afin d'appliquer la méthode des rectangles pour évaluer l'aire sous la courbe
nb_seg = 100
tableau_np_nb_seg = np_tableau_nb_segments(nb_seg)


'''EXÉCUTION DES FONCTIONS ET CALCULS'''
#On calcule l'aire sous la courbe I avec la méthode des rectangles et on affiche le résulat
resultat_methode_rect = aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg)
print(f'\nAvec la méthode des rectangles et {nb_seg} segments, l\'aire sous la courbe est {resultat_methode_rect}')
#On calcule l'aire sous la courbe I avec la méthode exacte et on affiche le résulat
resultat_methode_exacte = aire_poly_exacte(limite_inf, limite_sup, coefs)
print(f'Avec la méthode exacte, l\'aire sous la courbe est {resultat_methode_exacte}')
#On calcule l'erreur d'intégration entre la méthode des rectangles et la méthode exacte et on affiche le résulat
erreur_integration = erreur_integ(resultat_methode_rect, resultat_methode_exacte)
print(f'L\'erreur d\'intégration est de {erreur_integration}')

#On évalue la convergence de l'erreur d'intégration avec un nombre croissant de segments, jusqu'à atteindre la valeur spécifiée "nb_seg"
#On affiche ensuite un graphe démontrant l'erreur d'intégration en fonction du nombre de segments
convergence_erreur = evolution_erreur(limite_inf, limite_sup, coefs, nb_seg)


'''ÉVALUATION DU TEMPS D'EXÉCUTION DES FONCTIONS'''
# Évaluation du temps d'exécution du script, avec les fonctions codées en python de base
# On affiche à l'utilisateur la valeur calculée
temps_execution_fonction_base = timeit.timeit(lambda: aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg), number = 1)
print(f"\nTemps requis pour calculer l'intégrale de la courbe I avec la fonction codée en python de base: {temps_execution_fonction_base} secondes")

# Évaluation du temps d'exécution du script, avec les fonctions vectorisées et codées avec numpy
# On affiche à l'utilisateur la valeur calculée
temps_execution_avec_numpy = timeit.timeit(lambda: np_tableau_nb_segments(nb_seg), number = 1)
temps_execution_avec_numpy = temps_execution_avec_numpy + timeit.timeit(lambda: np_aire_poly_rect(limite_inf, limite_sup, coefs, tableau_np_nb_seg), number = 1)
print(f"\nTemps requis pour calculer l'intégrale de la courbe I avec la fonction codée avec numpy: {temps_execution_avec_numpy} secondes")


'''COMPARAISON DE L'ERREUR DES 2 TYPES DE FONCTIONS EN FONCTION DU TEMPS D'EXÉCUTION'''
temps_exec_erreur_integr = temps_exec_evolution_erreur(limite_inf, limite_sup, coefs, nb_seg)
temps_exec_erreur_integr_np = np_temps_execution(limite_inf, limite_sup, coefs, tableau_np_nb_seg)
tableau_erreur_np = np_evolution_erreur(limite_inf, limite_sup, coefs, tableau_np_nb_seg)
new_tableau_erreur_np = np.delete(tableau_erreur_np,0)

#plt.plot(temps_exec_erreur_integr, erreur_integration, label = "Fonctions Python de base",color='b')
plt.plot(temps_exec_erreur_integr_np, new_tableau_erreur_np, label = "Fonction Python avec numpy",color='r')
plt.title("Erreur d'intégration en fonction du temps d'exécution",loc="center")
plt.xlabel("Temps d'exécution en secondes")
plt.ylabel("Erreur d'intégration")
plt.legend
plt.show()