import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt




def aire_poly_rect(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4, nb_seg):
    sum_aire_rect = 0
    increm = (limite_sup - limite_inf)/nb_seg

    for i in range (0, nb_seg):
        x = limite_inf + i*increm + increm/2
        hauteur_rect = coef_p1 + coef_p2*x + coef_p3*x**2 + coef_p4*x**3
        aire_rect = hauteur_rect*increm
        sum_aire_rect += aire_rect
    
    return sum_aire_rect


# On calcule l'aire sous la courbe I selon la méthode exacte (méthode analytique)
def aire_poly_exacte(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4):
    resultat = coef_p1 * (limite_sup-limite_inf) + coef_p2 * ((limite_sup**2-limite_inf**2)/2) + coef_p3 * ((limite_sup**3-limite_inf**3)/3) + coef_p4 * ((limite_sup**4-limite_inf**4)/4)
    return resultat

def error_integ(aire_anal, aire_rect):
    return abs(aire_anal-aire_rect)

def evolution_erreur(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4):
    error_integr = []

    for i in range (1, 100):
        nb_seg = i
        aire_poly_rectangle = aire_poly_rect(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4, nb_seg)
        aire_poly_anal = aire_poly_exacte(limite_inf, limite_sup, coef_p1, coef_p2, coef_p3, coef_p4)

        error_integr.append(error_integ(aire_poly_anal, aire_poly_rectangle))

    plt.plot(error_integr)
    plt.show()
    return error_integr


