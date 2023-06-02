import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt




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
def aire_poly_exacte(limites, coefs):
    resultat = coefs[0] * (limites[1] - limites[0]) + coefs[1] * ((limites[1]**2-limites[0]**2)/2) + coefs[2] * ((limites[1]**3-limites[0]**3)/3) + coefs[3] * ((limites[1]**4-limites[0]**4)/4)
    return resultat

def error_integ(aire_anal, aire_rect):
    return abs(aire_anal-aire_rect)

def evolution_erreur(limites, coefs):
    error_integr = []

    for i in range (1, 100):
        nb_seg = i
        aire_poly_rectangle = aire_poly_rect(limites, coefs, nb_seg)
        aire_poly_anal = aire_poly_exacte(limites, coefs)

        error_integr.append(error_integ(aire_poly_anal, aire_poly_rectangle))

    plt.plot(error_integr)
    plt.show()
    return error_integr


