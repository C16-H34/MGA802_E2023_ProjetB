# Mini-Projet B - Analyse numérique
# Script contenant toutes les fonctions pour l'exercice 1
# Par: Gabriel Gunther et Alxandre Panhaleux
# Code permanent: GUNG19029902 et PANA87310001
# Date de remise: 6 juin 2023 à minuit

# Importation de bibliothèques additionnelles
import numpy as np
import matplotlib.pyplot as plt

'''FONCTIONS CODÉES SEULEMENT AVEC PYTHON DE BASE'''

# Fonction qui calcule l'aire sous la courbe I d'une fonction polynomiale de degré 3 avec la méthode des rectangles
# Retourne l'aire sous la courbe
def aire_poly_rect(limites, coefs, nb_seg):
    sum_aire_rect = 0
    increm = (limites[1] - limites[0])/nb_seg

    for i in range (0, nb_seg):
        x = limites[0] + i*increm + increm/2
        hauteur_rect = coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3
        aire_rect = hauteur_rect*increm
        sum_aire_rect += aire_rect

    return sum_aire_rect


# On calcule l'aire sous la courbe I selon la méthode exacte (méthode analytique)
# Retourne la valeur exacte de l'aire sous la courbe
def aire_poly_exacte(limites, coefs):
    aire_exacte = coefs[0] * (limites[1] - limites[0]) + coefs[1] * ((limites[1]**2-limites[0]**2)/2) + coefs[2] * ((limites[1]**3-limites[0]**3)/3) + coefs[3] * ((limites[1]**4-limites[0]**4)/4)
    return aire_exacte

# Fonction qui calcule l'erreur entre la valeur de l'aire sous la courbe calculée par la méthode exacte (analytique)
# et la méthode des rectangles
# Retourne l'erreur d'intgration en pourcentage
def erreur_integ(aire_exacte, aire_rect):
    erreur = (abs(aire_exacte-aire_rect)/aire_exacte)*100
    return erreur

# Fonction qui calcule l'erreur d'intégration pour le nombre de segments spécifié. La commence a calculer à partir de
# 1 segment, puis augmente le nombre de segments de 1 jusqu'à atteindre la limite spécifiée.
# Retourne un graphique illustrant l'erreur en fonction du nombre de segments utilisés dans la fonction de calcul de
# l'aire avec la méthode des rectangles. On cherche à vérifier s'il y a convergence plus le nombre de rectangles augmente.
def evolution_erreur(limites, coefs, nb_seg):
    erreur_integr = [] #Initialisation de la liste contenant chaque valeur d'erreur d'intégration

    for i in range (1, nb_seg): #On calcule l'erreur pour un nombre croissant de segments, de 1 à la limite spécifiée
        aire_poly_rectangle = aire_poly_rect(limites, coefs, i)
        aire_poly_analytique = aire_poly_exacte(limites, coefs)
        #On calcule l'erreur et on ajoute sa valeur à la liste
        erreur_integr.append(erreur_integ(aire_poly_analytique, aire_poly_rectangle))

    # Génératon d'un graphe illustrant la convergence de l'erreur d'intégration
    plt.plot(erreur_integr)
    plt.title("Convergence de l'erreur d'intégration, en fonction du nombre de segments", loc = "center")
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur d\'intégration en %')
    plt.show()
    return erreur_integr


'''FONCTIONS CODÉES AVEC NUMPY'''
# Fonction qui calcule l'erreur d'intégration pour le nombre de segments spécifié. La commence a calculer à partir de
# 1 segment, puis augmente le nombre de segments de 1 jusqu'à atteindre la limite spécifiée.
# Retourne un graphique illustrant l'erreur en fonction du nombre de segments utilisés dans la fonction de calcul de
# l'aire avec la méthode des rectangles. On cherche à vérifier s'il y a convergence plus le nombre de rectangles augmente.
#def np_evolution_erreur(limites, coefs, nb_seg):
    #tableau_erreur = np.arange(1, nb_seg + 1, dtype=int)
    #tableau_erreur = np.zeros([nb_seg+1,2],dtype = float)
    #for i in range(tableau_erreur.shape[0]):
        #tableau_erreur[i,0] = tableau_erreur[i,0] + 1
        #aire_poly_rectangle = aire_poly_rect(limites, coefs, tableau_erreur[i,0])
        #aire_poly_analytique = aire_poly_exacte(limites, coefs)

        #tableau_erreur[i,1] = erreur_integ(aire_poly_analytique, aire_poly_rectangle)