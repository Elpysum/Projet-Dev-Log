# Voici les codes Python :

########################################################### EXERCICE 1 #########################################################
## Première fonction 
def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
  



def iteration_jeu(Z):
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    """
    On parcourt avec la boucle for chaque cellule de Z avec son nombre de voisins vivants.
    Si une cellule vivante a 0, 1 ou 4 voisins vivants on lui affecte la valeur 0 (mort).
    Si une cellule morte a exactement 3 voisins vivants on lui affecte 1 (naissance).
    Tout autre cas garde la meme valeur.
    """
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z
"""
Cette fonction fait donc une simulation d'un tour du jeu pour une matrice Z donnée.
"""



## On créé une fonction 
def iterations_09(Z):
    plt.subplots(figsize=(15,10))
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])
        plt.grid(True)
        ax.set_xticks(range(0,len(Z[0]),1))
        plt.title('Itération ' + str(i))
               
        Z = iteration_jeu(Z) 

    plt.show()
"""
Cette fonction affiche une simulation de 0 à 9 itérations pour une matrice Z de n'importe qu'elle taille. 
"""



import numpy as np
import matplotlib.pyplot as plt

def step_i(Z_initial, iter = 0):
    plt.figure(figsize = (10, 10))
    Z_i = np.array(Z_initial)
    for i in range(iter):
        Z_i = iteration_jeu(Z_i)
    
    plt.imshow(Z_i, extent=[0,len(Z_i[0]),0,len(Z_i)])
    plt.grid(True)
    plt.title("Affichage de l'itération " + str(iter))
    

from numba import jit
@jit(nopython=True)
def calcul_nb_voisins_rapide(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N



@jit(nopython=True)
def iteration_jeu_rapide(Z):
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins_rapide(Z)

    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z

########################################################### EXERCICE 2 #########################################################
