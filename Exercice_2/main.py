## MAIN CODE EXERCICE 2 ##

# Importation de bibliothèques aditionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# On fixe les variables globales qui ne servent que pour le main
coeff_diffusion = 0.0000988

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


#Affichage du point chaud après 800 secondes à l'aide de la fonction avancement qui utilise la fonction Affichage_temp
print("\nVOICI LE POINT CHAUD A L'INSTANT 800")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 800, instant_initial)

#Affichage du point chaud après 1600 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 1600")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 1600, instant_initial)

#Affichage du point chaud après 2000 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 2000")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 2000, instant_initial)

#Affichage du point chaud après 3000 secondes
print("\nVOICI LE POINT CHAUD A L'INSTANT 3000")
instant_initial = time.perf_counter()
avancement_temporel(Temp_init, Grille, coeff_diffusion, 3000, instant_initial)
