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

from mod1 import grille
from mod1 import solution_initiale
from mod1 import avancement_temporel


#Affichage_temp(Grille, Temp_init)
#Calcul_RHS(Grille, coeff_diffusion, Temp_init)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
print("\nVoici le point chaud à l'instant initialinitail")
plt.title('Point chaud initial')
Temp_init = solution_initiale(Grille, amplitude_point_chaud, sigma_point_chaud, XC, YC, temperature_atmosphere)
avancement_temporel(Temp_init, Grille, coeff_diffusion, 0)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
print("\nVoici le point chaud après 2 dt")
plt.title('Point chaud après 2 dt')
avancement_temporel(Temp_init, Grille, coeff_diffusion, 600)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
print("\nVoici le point chaud après 3 dt")
plt.title('Point chaud après 3 dt')
avancement_temporel(Temp_init, Grille, coeff_diffusion, 860)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
print("\nVoici le point chaud après 4 dt")
plt.title('Point chaud après 4 dt')
avancement_temporel(Temp_init, Grille, coeff_diffusion, 1200)

Grille=grille(longueur, hauteur, nb_segments_x, nb_segment_y)
print("\nVoici le point chaud après 5 dt")
plt.title('Point chaud après 5 dt')
avancement_temporel(Temp_init, Grille, coeff_diffusion, 1500)

