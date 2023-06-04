# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# On fixe les paramètres:
coeff_diffusion = 0.0000988

from mod1 import grille
from mod1 import solution_initiale
from mod1 import avancement_temporel
from mod1 import Affichage_temp
from mod1 import interface_utilisateur

#Affichage_temp(Grille, Temp_init)
#Calcul_RHS(Grille, coeff_diffusion, Temp_init)
'''
probleme = interface_utilisateur()
longueur = int(probleme['longueur'])
hauteur = int(probleme['hauteur'])
nb_segments_x = int(probleme['nb_segment_x'])
nb_segments_y = int(probleme['nb_segment_y'])
XC = int(probleme['XC'])
YC = int(probleme['YC'])
amplitude_point_chaud = int(probleme['amplitude_point_chaud'])
sigma_point_chaud = int(probleme['ecartement_point_chaud'])
temperature_atmosphere = int(probleme['temp_atmosphere'])
'''
longueur = 20
hauteur = 15
nb_segments_x = 45
nb_segments_y = 65
XC = 5
YC = 5
coeff_diffusion = 0.000173
amplitude_point_chaud = 50
sigma_point_chaud = 5
temperature_atmosphere = 20


Grille=grille(longueur, hauteur, nb_segments_x, nb_segments_y)
dt = (0.25 * (Grille['X'][1])**2)/coeff_diffusion
print(dt)
print("\nVOICI LE POINT CHAUD A L'ETAT INITIAL")
plt.title('Point chaud initial')
instant_initial = time.perf_counter()
Temp_init = solution_initiale(Grille, amplitude_point_chaud, sigma_point_chaud, XC, YC, temperature_atmosphere)
Affichage_temp(Grille, Temp_init)


Grille=grille(longueur, hauteur, nb_segments_x, nb_segments_y)
print("\nVOICI LE POINT CHAUD APRES 2 dt")
plt.title('Point chaud après 2 dt')
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 2*dt+1, instant_initial)


Grille=grille(longueur, hauteur, nb_segments_x, nb_segments_y)
print("\nVOICI LE POINT CHAUD APRES 3 dt")
plt.title('Point chaud après 3 dt')
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 3*dt+1, instant_initial)


Grille=grille(longueur, hauteur, nb_segments_x, nb_segments_y)
print("\nVOICI LE POINT CHAUD APRES 4 dt")
plt.title('Point chaud après 4 dt')
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 4*dt+1, instant_initial)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segments_y)
print("\nVOICI LE POINT CHAUD APRES 5 dt")
plt.title('Point chaud après 5 dt')
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 5*dt+1, instant_initial)