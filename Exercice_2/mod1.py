## MODULE 1 EXERCICE 2 ##

# Importation de bibliothèques additionnelles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#initialisations de variables globales
instant = 0
min_temp = []
max_temp = []
mean_temp = []
Linfini = []
L2 = []
Statistiques = np.array([[],[],[],[],[]])

#FONCTIIONS
# Fonction qui génère une grille de calcul et qui la pose sur un graphique matplotlib
def grille(longueur, hauteur, nb_segments_x, nb_segments_y): 
    #creation de deux vecteurs qui contiennent les points en x et les pints en y  
    x = np.linspace(0,longueur,nb_segments_x + 1)
    y = np.linspace(0,hauteur,nb_segments_y + 1)
    #création de la grille, xv est une matrice contenant les x et yv contient les y de la grille
    xv, yv = np.meshgrid(x,y)
    #création d'un dictionnaire grid 
    grid = {}
    grid['X'] = x
    grid['Y'] = y
    #Dessin de la grille sur le graphique
    plt.figure()
    plt.plot(grid['X'], yv.transpose(), linestyle='-', color='grey', linewidth=0.5)
    plt.plot(xv, grid['Y'], linestyle='-', color='grey', linewidth=1)
    return grid

#fonction qui calcule la solution iniiale de la distribution du point chaud sur la grille
def solution_initiale(grid, Amplitude, écartement, XC, YC, temperature_atmosphere):
    #initialisation de la matrice de temperature aux dimensions de la grille 
    Temp_init=np.ones((len(grid['X']), len(grid['Y'])))*temperature_atmosphere
    #Pour chaque point de la matrice de tenperature, on calcule sa valeur
    for index_X in range(1, len(grid['X'])-1):
        for index_Y in range(1, len(grid['Y'])-1):
            Temp_init[index_X, index_Y] += Amplitude*np.exp(-(((grid['X'][index_X]-XC)**2)/(2*écartement**2)+((grid['Y'][index_Y]-YC)**2)/(2*écartement**2)))
    return Temp_init

#Fonction d'affichage de la temoerature
def Affichage_temp(grid, Temp):
    #on dessine les contours de la matrice de Temperature sur la figure qui a été construite par grille()
    plt.contourf(grid['X'], grid['Y'], Temp.transpose())
    plt.show()

#Fonction qui calcule le RHS        
def Calcul_RHS(grid, coeff_diffusion, Temp):
    #initialisation du RHS à une matrice de zeros de meme taille que la grille 
    RHS = np.zeros((len(grid['X']), len(grid['Y'])))
    #on parcours la grille et on calcule le RHS corresppondant à chaque point
    for index_X in range(1, len(grid['X'])-1):
        for index_Y in range(1, len(grid['Y'])-1):
            RHS[index_X, index_Y] = coeff_diffusion*((Temp[index_X+1, index_Y] - 2*Temp[index_X, index_Y] + Temp[index_X-1, index_Y])/(grid['X'][1]**2) + (Temp[index_X, index_Y+1] - 2*Temp[index_X, index_Y] + Temp[index_X, index_Y-1])/(grid['Y'][1]**2))
    return RHS


#Fonction qui réalise l'avancement temporelle du point chaud dans la plaque
def avancement_temporel(Temp, grid, coeff_diffusion, instant_avancement, instant_initial):
    #on calcule le pas temporel 
    dt = (0.25 * (grid['X'][1])**2)/coeff_diffusion
    #incorporation des variables globales
    global instant, longueur, nb_segment_x, nb_segment_y, Statistiques, nb_segment_x, nb_segment_y
    #Calcul de l'instant correspondant à l'exécution en cours, la fonction sera appelée en imbriqué pour faire avancer le temps
    instant += dt 

    #Calcul de la nouvelle matrice de température correspondant à l'instant suivant
    New_Temp = Temp + dt*Calcul_RHS(grid, coeff_diffusion, Temp)
    
    #Si l'instant d'exécution est inférieur à l'instant demandé, alors il faut continuer d'avancer dans le temps
    if instant<instant_avancement :
        #Calcul des statistiques de température au cours du temps 
        Statistiques = enregistrement(Temp, New_Temp, False)
        avancement_temporel(New_Temp, grid, coeff_diffusion, instant_avancement, instant_initial)
    #sinon, il faut dessiner le nouveau vecteur de température, afficher les statistiques et réinitialiser les variables globales
    else:
        Temps_calcul = time.perf_counter() - instant_initial
        Grille=grille(longueur, hauteur, nb_segment_x, nb_segment_y)
        plt.title(f"Point chaud à l'instant {instant_avancement}s")
        Affichage_temp(grid, Temp)
        print(f"\nTemps de Calul = {Temps_calcul}")
        instant = 0
        print(f"\nLa température minimale est {Statistiques[0, :]}")
        print(f"\nLa température maximale est {Statistiques[1, :]}")
        print(f"\nLa température moyenne est {Statistiques[2, :]}")
        print(f"\nLa norme Linfini est {Statistiques[3, :]}")
        print(f"\nLa norme L2 est {Statistiques[4, :]}")
        Statistiques = enregistrement(None, None, True)

#Fonction qui réalise les statistiques et enregistrements de la température au cours du temps 
def enregistrement(Temp, New_Temp, nettoyage):
    global min_temp, max_temp, mean_temp, Linfini, L2, nb_segment_x, nb_segment_y

    #Si on doir faire le nettoyage en fin d'avancement temporel, alors on réinitialise les variables globales
    if nettoyage:
        min_temp = []
        max_temp = []
        mean_temp = []
        Linfini = []
        L2 = []
    #sinon, cela veut dire qu'il faut calculer les statistiques de température et les returner pour que le programme d'avncement les affiche
    else:
        min_temp.append(np.min(New_Temp[int(0.1*nb_segment_x):-int(0.1*nb_segment_x), int(0.1*nb_segment_y):-int(0.1*nb_segment_y)]))
        max_temp.append(np.max(New_Temp[int(0.1*nb_segment_x):-int(0.1*nb_segment_x), int(0.1*nb_segment_y):-int(0.1*nb_segment_y)]))
        mean_temp.append(np.mean(New_Temp[int(0.1*nb_segment_x):-int(0.1*nb_segment_x), int(0.1*nb_segment_y):-int(0.1*nb_segment_y)]))

        residu = (New_Temp-Temp)/New_Temp
        Linfini.append(np.max(np.abs(residu[int(0.1*nb_segment_x):-int(0.1*nb_segment_x), int(0.1*nb_segment_y):-int(0.1*nb_segment_y)])))
        L2.append(np.mean(np.square(residu[int(0.1*nb_segment_x):-int(0.1*nb_segment_x), int(0.1*nb_segment_y):-int(0.1*nb_segment_y)])))

    return(np.array([min_temp, max_temp, mean_temp, Linfini, L2]))


 #Fonction qui réalise l'interface utilisatuer qui permet de récupérer les données du problème
def interface_utilisateur():
    global longueur, XC, YC, hauteur, nb_segment_x, nb_segment_y, amplitude_point_chaud, ecartement_point_chaud, temp_atmosphere
    
    print("BIENVENUE SUR LE PROGRAMME POINT CHAUD \n\nCe programme montre l'évoltion d'un point chaud dans une plaque d'Aluminium supposée infinie dans la direction perpendiculaire au plan de l'ordinateur")
    longueur = int(input('Veillez choisir la longueur de la plaque en cm :'))
    hauteur = int(input('Veillez choisir la hauteur de la plaque en cm :'))
    nb_segment_x = int(input('Veillez choisir le nombre de segments de mesure suivant la longueur (suivant x) :'))
    nb_segment_y = int(input('Veillez choisir le nombre de segments de mesure suivant la hauteur (suivant y) :'))
    XC =  int(input("Veillez choisir l'emplacment du point chaud suivant la longueur (Xpoint_chaud) :"))
    YC =  int(input("Veillez choisir l'emplacment du point chaud suivant la hauteur (Ypoint_chaud) :"))
    amplitude_point_chaud = int(input("Veillez choisir l'amplitude du point chaud en °C :"))
    ecartement_point_chaud = int(input("Veillez choisir l'écartement du point chaud en cm :"))
    temp_atmosphere = int(input("Veillez choisir la température de l'atmosphere en °C :"))
    #probleme = pd.Series([longueur, hauteur, nb_segment_x, nb_segment_y, XC, YC, amplitude_point_chaud, ecartement_point_chaud, temp_atmosphere])
    #probleme.index = ['longueur', 'hauteur', 'nb_segment_x', 'nb_segment_y', 'XC', 'YC', 'amplitude_point_chaud', 'ecartement_point_chaud', 'temp_atmosphere']
    #return(probleme)