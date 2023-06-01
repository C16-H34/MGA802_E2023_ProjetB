# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On fixe les paramètres:
longueur = 20
hauteur = 15
nb_segments_x = 40
nb_segment_y = 40
#xc =
#yc =
#diffusivite =
#amplitude_point_chaud =
#sigma_point_chaud =
temperature_atmosphere = 20
#temperature_initiale =

# Fonction qui génère une grille de calcul (de forme carrée)
# On créé un vecteur X
def grille(longueur, hauteur, nb_segments_x, nb_segments_y):   
    x = np.linspace(0,longueur,nb_segments_x + 1)
    y = np.linspace(0,hauteur,nb_segments_y + 1)
    xv, yv = np.meshgrid(x,y)
    grid = {}
    grid['X'] = x
    grid['Y'] = y
    print(xv)
    print(yv)
    print(grid['X'])
    plt.plot(grid['X'], xv, linestyle='-')
    #plt.plot(yv, xv, linestyle='-')
    #plt.plot(y, yv)
    plt.show()

# Sur la grille de calcul, on trace le contour en couleur pour le champ de température
#plt.contourf([xc,yc],temperature_initiale)

def interface():
    params = {}
    params['L'] = 10
    params['H'] = 10

#def temperature_pts_chaud(xc,yc,amplitude,ecart):
    #amplitude np.exp(-(()))

grille(longueur, hauteur, nb_segments_x, nb_segment_y)