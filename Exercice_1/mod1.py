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

print(aire_poly_rect(-2, 2, 2,3,4,5,100))