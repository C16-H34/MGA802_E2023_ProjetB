# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On fixe les paramètres:
longueur = 20
hauteur = 15
nb_segments_x = 45
nb_segment_y = 65
XC = 5
YC = 5
#diffusivite =
amplitude_point_chaud = 5
sigma_point_chaud = 5
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
    plt.figure()
    plt.plot(grid['X'], yv.transpose(), linestyle='-', color='grey', linewidth=0.5)
    plt.plot(xv, grid['Y'], linestyle='-', color='grey', linewidth=0.5)
    return grid

# Sur la grille de calcul, on trace le contour en couleur pour le champ de température
#plt.contourf([xc,yc],temperature_initiale)

def interface():
    params = {}
    params['L'] = 10
    params['H'] = 10

def solution_initiale(grid, Amplitude, écartement, XC, YC):
    Temp_init=np.zeros((len(grid['X']), len(grid['Y'])))
    for index_X in range(len(grid['X'])):
        for index_Y in range(len(grid['Y'])):
            Temp_init[index_X, index_Y] = Amplitude*np.exp(-(((grid['X'][index_X]-XC)**2)/(2*écartement**2)+((grid['Y'][index_Y]-YC)**2)/(2*écartement**2)))
    
    return Temp_init

def Affichage_temp(grid, Temp):
    plt.contourf(grid['X'], grid['Y'], Temp.transpose())
    plt.show()
            

#def temperature_pts_chaud(xc,yc,amplitude,ecart):
    #amplitude np.exp(-(()))

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
Temp_init = solution_initiale(Grille, amplitude_point_chaud, sigma_point_chaud, XC, YC)
Affichage_temp(Grille, Temp_init)