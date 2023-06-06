# Mini-Projet B - Analyse numérique
# Script contenant toutes les fonctions pour l'exercice 1
# Par: Gabriel Gunther et Alxandre Panhaleux
# Code permanent: GUNG19029902 et PANA87310001
# Date de remise: 6 juin 2023 à minuit

# Importation de bibliothèques additionnelles
import numpy as np
import matplotlib.pyplot as plt
import timeit

'''FONCTIONS CODÉES SEULEMENT AVEC PYTHON DE BASE'''

# Fonction qui calcule l'aire sous la courbe I d'une fonction polynomiale de degré 3 avec la méthode des rectangles
# Retourne l'aire sous la courbe
def aire_poly_rect(limite_inf, limite_sup, coefs, nb_seg):
    sum_aire_rect = 0
    increm = (limite_sup - limite_inf)/nb_seg

    for i in range (0, nb_seg):
        x = limite_inf + i*increm + increm/2
        hauteur_rect = coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3
        aire_rect = hauteur_rect*increm
        sum_aire_rect += aire_rect

    return sum_aire_rect


# On calcule l'aire sous la courbe I selon la méthode exacte (méthode analytique)
# Retourne la valeur exacte de l'aire sous la courbe
def aire_poly_exacte(limite_inf, limite_sup, coefs):
    aire_exacte = coefs[0] * (limite_sup - limite_inf) + coefs[1] * ((limite_sup**2-limite_inf**2)/2) + coefs[2] * ((limite_sup**3-limite_inf**3)/3) + coefs[3] * ((limite_sup**4-limite_inf**4)/4)
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
def evolution_erreur(limite_inf, limite_sup, coefs, nb_seg):
    erreur_integr = [] #Initialisation de la liste contenant chaque valeur d'erreur d'intégration

    for i in range (1, nb_seg): #On calcule l'erreur pour un nombre croissant de segments, de 1 à la limite spécifiée
        aire_poly_rectangle = aire_poly_rect(limite_inf, limite_sup, coefs, i)
        aire_poly_analytique = aire_poly_exacte(limite_inf, limite_sup, coefs)
        #On calcule l'erreur et on ajoute sa valeur à la liste
        erreur_integr.append(erreur_integ(aire_poly_analytique, aire_poly_rectangle))

    # Génératon d'un graphe illustrant la convergence de l'erreur d'intégration
    plt.plot(erreur_integr)
    plt.title("Convergence de l'erreur d'intégration, en fonction du nombre de segments", loc = "center")
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur d\'intégration en %')
    plt.show()
    return erreur_integr

def temps_exec_evolution_erreur(limite_inf, limite_sup, coefs, nb_seg):
    temps_exec_erreur_integr = [float()] #Initialisation de la liste contenant chaque valeur du temps d'exécution de la fonction d'erreur d'intégration

    for i in range (1, nb_seg): #On calcule l'erreur pour un nombre croissant de segments, de 1 à la limite spécifiée
        temps = timeit.timeit(lambda: aire_poly_rect(limite_inf, limite_sup, coefs, i), number=1)
        temps += timeit.timeit(lambda: aire_poly_exacte(limite_inf, limite_sup, coefs), number=1)
        #On calcule l'erreur et on ajoute sa valeur à la liste
        temps += timeit.timeit(lambda: erreur_integ(aire_poly_exacte(limite_inf, limite_sup, coefs), aire_poly_rect(limite_inf, limite_sup, coefs, i)), number=1)
        temps_exec_erreur_integr.append(temps)
    temps_exec_erreur_integr.pop(0)
    return(temps_exec_erreur_integr)


'''FONCTIONS CODÉES AVEC NUMPY'''

# Fonction qui créé un tableau ndarray avec le nombre de segments spécifiés dans le main.
# Retourne un tableau ndarray contenant le nombre croissant (à partir de 1) du nombre de segments.
def np_tableau_nb_segments(nb_seg):
    np_nb_seg = np.arange(1, nb_seg + 1, dtype=float)
    np_nb_seg = np_nb_seg.reshape(len(np_nb_seg), 1)
    return np_nb_seg

# Fonction qui calcule l'aire sous la courbe I d'une fonction polynomiale de degré 3 avec la méthode des rectangles
# Retourne l'aire sous la courbe
def np_aire_poly_rect(limite_inf, limite_sup, coefs, np_nb_seg):

    sum_aire_rect = 0
    np_aire_rect = np.ones(np_nb_seg.shape)
    increm = (limite_sup - limite_inf)/np_nb_seg

    for j in range (0, len(np_nb_seg)):
        sum_aire_rect = 0
        for i in range (0, int(np_nb_seg[j,0])):
            x = limite_inf + i*increm[j,0] + increm[j,0]/2
            hauteur_rect = coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3
            aire_rect = hauteur_rect*increm[j,0]
            sum_aire_rect += aire_rect
        np_aire_rect[j,0] = sum_aire_rect

    return np_aire_rect

# Fonction qui calcule l'aire sous la courbe I avec la méthode exacte, en faisant appel à des fonctions numpy.
# Retourne un tableau de la même taille
def np_aire_poly_exacte(limite_inf, limite_sup, coefs, np_nb_seg):
    np_aire_exacte = np.ones(np_nb_seg.shape)
    np_aire_exacte = np_aire_exacte*(coefs[0] * (limite_sup - limite_inf) + coefs[1] * ((limite_sup**2-limite_inf**2)/2) + coefs[2] * ((limite_sup**3-limite_inf**3)/3) + coefs[3] * ((limite_sup**4-limite_inf**4)/4))
    return np_aire_exacte


# Fonction qui calcule l'erreur d'intégration pour le nombre de segments spécifié. La commence a calculer à partir de
# 1 segment, puis augmente le nombre de segments de 1 jusqu'à atteindre la limite spécifiée.
# Retourne un tableau illustrant l'erreur d'intégration en fonction du nombre de segments
def np_evolution_erreur(limite_inf, limite_sup, coefs, np_nb_seg):
    np_aire_poly_rectangle = np_aire_poly_rect(limite_inf, limite_sup, coefs, np_nb_seg)
    np_aire_poly_analytique = np_aire_poly_exacte(limite_inf, limite_sup, coefs, np_nb_seg)

    tableau_erreur = (np.abs(np_aire_poly_rectangle-np_aire_poly_analytique)/np_aire_poly_analytique)*100
    return tableau_erreur

def np_temps_execution(limite_inf, limite_sup, coefs, np_nb_seg):
    #tableau_erreur = np_evolution_erreur(limite_inf, limite_sup, coefs, np_nb_seg)
    temps_exec_erreur_integr_np = [float()] #Initialisation de la liste contenant chaque valeur du temps d'exécution de la fonction d'erreur d'intégration

    for i in range (1, len(np_nb_seg)): #On calcule l'erreur pour un nombre croissant de segments, de 1 à la limite spécifiée
        temps = timeit.timeit(lambda: np_aire_poly_exacte(limite_inf, limite_sup, coefs, np_nb_seg), number=1)
        temps += timeit.timeit(lambda: np_aire_poly_exacte(limite_inf, limite_sup, coefs, np_nb_seg), number=1)
        #On calcule l'erreur et on ajoute sa valeur à la liste
        temps += timeit.timeit(lambda: np_evolution_erreur(limite_inf, limite_sup, coefs, np_nb_seg), number=1)
        temps_exec_erreur_integr_np.append(temps)

    temps_exec_erreur_integr_np.pop(0)

    return temps_exec_erreur_integr_np