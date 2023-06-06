## MAIN CODE EXERCICE 2 ##

# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# On fixe les variables globales qui ne servent que pour le main
coeff_diffusion = 0.988 #en cm^2/s car on travaille en cm dans notre code

#Importation des fonctions du fichier module 1 
from mod1 import grille
from mod1 import solution_initiale
from mod1 import avancement_temporel
from mod1 import Affichage_temp
from mod1 import interface_utilisateur
from mod1 import enregistrement

#On lance l'interface utilisatuer qui nous permet de récupérer les variables du problème
interface_utilisateur()
from mod1 import longueur, XC, YC, hauteur, nb_segment_x, nb_segment_y, amplitude_point_chaud, ecartement_point_chaud, temp_atmosphere

#Création de la grille avec la fonction grille
Grille=grille(longueur, hauteur, nb_segment_x, nb_segment_y)
#Calcul du pas de temps adapté à la configuration du problème
dt = (0.25 * (Grille['X'][1])**2)/coeff_diffusion

#Affichage du point chaud initial à l'aide de la fonction solution_initiale et Affichage_temp
print("\nVOICI LE POINT CHAUD A L'ETAT INITIAL")
plt.title('Point chaud initial')
instant_initial = time.perf_counter()
Temp_init = solution_initiale(Grille, amplitude_point_chaud, ecartement_point_chaud, XC, YC, temp_atmosphere)
Affichage_temp(Grille, Temp_init)


#Affichage du point chaud après 0.1 secondes à l'aide de la fonction avancement qui utilise la fonction Affichage_temp
print("\nVOICI LE POINT CHAUD A L'INSTANT 0.1")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 0.5, instant_initial)

#Affichage du point chaud après 0.2 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 0.2")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 1, instant_initial)

#Affichage du point chaud après 0.25 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 0.25")
instant_initial = time.perf_counter() 
avancement_temporel(Temp_init, Grille, coeff_diffusion, 5, instant_initial)

#Affichage du point chaud après 0.28 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 0.28")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 30, instant_initial)
