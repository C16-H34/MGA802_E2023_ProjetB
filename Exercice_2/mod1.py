# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

instant = 0
min_temp = []
max_temp = []
mean_temp = []
Linfini = []
L2 = []
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
    global min_temp
    global max_temp
    global mean_temp
    global Linfini
    global L2
    instant += dt 

    New_Temp = Temp + dt*Calcul_RHS(grid, coeff_diffusion, Temp)
    
    if instant < instant_avancement :
        enregistrement(Temp, New_Temp)
        avancement_temporel(New_Temp, grid, coeff_diffusion, instant_avancement)
    else:
        Affichage_temp(grid, Temp)
        instant = 0
        print(min_temp)
        print(max_temp)
        print(mean_temp)
        print(Linfini)
        print(L2)
        min_temp = []
        max_temp = []
        mean_temp = []
        Linfini = []
        L2 = []
        return Temp
    
def enregistrement(Temp, New_Temp):
    global min_temp
    global max_temp
    global mean_temp
    global Linfini
    global L2

    min_temp.append(np.min(New_Temp[5:40, 6:58]))
    max_temp.append(np.max(New_Temp[5:40, 6:58]))
    mean_temp.append(np.mean(New_Temp[5:40, 6:58]))

    residu = (New_Temp-Temp)/New_Temp
    Linfini.append(np.max(np.abs(residu[5:40, 6:58])))
    L2.append(np.mean(np.square(residu[5:40, 6:58])))

