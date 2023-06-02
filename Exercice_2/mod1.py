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
coeff_diffusion = 0.000173
amplitude_point_chaud = 50
sigma_point_chaud = 5
temperature_atmosphere = 20
instant = 0

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
    plt.plot(xv, grid['Y'], linestyle='-', color='grey', linewidth=1)
    return grid

# Sur la grille de calcul, on trace le contour en couleur pour le champ de température
#plt.contourf([xc,yc],temperature_initiale)

def interface():
    params = {}
    params['L'] = 10
    params['H'] = 10

def solution_initiale(grid, Amplitude, écartement, XC, YC, temperature_atmosphere):
    Temp_init=np.ones((len(grid['X']), len(grid['Y'])))*temperature_atmosphere
    for index_X in range(1, len(grid['X'])-1):
        for index_Y in range(1, len(grid['Y'])-1):
            Temp_init[index_X, index_Y] += Amplitude*np.exp(-(((grid['X'][index_X]-XC)**2)/(2*écartement**2)+((grid['Y'][index_Y]-YC)**2)/(2*écartement**2)))
    print(Temp_init)

    return Temp_init

def Affichage_temp(grid, Temp):
    plt.contourf(grid['X'], grid['Y'], Temp.transpose())
    plt.show()
            
def Calcul_RHS(grid, coeff_diffusion, Temp):
    RHS = np.zeros((len(grid['X']), len(grid['Y'])))
    for index_X in range(1, len(grid['X'])-1):
        for index_Y in range(1, len(grid['Y'])-1):
            RHS[index_X, index_Y] = coeff_diffusion*((Temp[index_X+1, index_Y] - 2*Temp[index_X, index_Y] + Temp[index_X-1, index_Y])/(grid['X'][1]**2) + (Temp[index_X, index_Y+1] - 2*Temp[index_X, index_Y] + Temp[index_X, index_Y-1])/(grid['Y'][1]**2))
    return RHS


def avancement_temporel(Temp, grid, coeff_diffusion, instant_avancement):
    dt = (0.25 * (grid['X'][1]**2))/coeff_diffusion
    global instant 
    instant += dt 
    print(grid['X'][1])
    print(dt)

    if instant < instant_avancement :
        NewTemp = Temp + dt*Calcul_RHS(grid, coeff_diffusion, Temp)
        avancement_temporel(NewTemp, grid, coeff_diffusion, instant_avancement)
    else:
        Affichage_temp(grid, Temp)
        print(Temp)
        return Temp
    


Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
Temp_init = solution_initiale(Grille, amplitude_point_chaud, sigma_point_chaud, XC, YC, temperature_atmosphere)
#Affichage_temp(Grille, Temp_init)
#Calcul_RHS(Grille, coeff_diffusion, Temp_init)
avancement_temporel(Temp_init, Grille, coeff_diffusion, 1400)