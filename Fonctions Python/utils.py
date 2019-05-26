# Voici les codes Python :
# Ces codes seront appelés depuis le Jupyter Notebook.

########################################################### EXERCICE 1 #########################################################
## Première fonction 
def calcul_nb_voisins(Z):
    """
    Arguments : 
    - Z = une liste de listes

    La fonction calcule le nombre de cellules voisines vivantes de chaque autre cellule.
    """
    
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
  
## Deuxième fonction
def iteration_jeu(Z):
    """
    Arguments : 
    - Z = une liste de listes
    
    Propriétés : 
    - On parcourt avec la boucle for chaque cellule de Z avec son nombre de voisins vivants.
    - Si une cellule vivante a 0, 1 ou 4 voisins vivants on lui affecte la valeur 0 (mort).
    - Si une cellule morte a exactement 3 voisins vivants on lui affecte 1 (naissance).
    - Tout autre cas garde la meme valeur.
    
    Cette fonction fait donc une simulation d'un tour du jeu pour une liste Z donnée.
    """
    
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z



## Troisième fonction
def iterations_09(Z):
    """
    Arguments : 
    - Z = une liste de listes (carrée)
    
    Cette fonction affiche une simulation de 0 à 9 itérations pour un Z de n'importe quelle taille, sur 2 lignes et 5 colonnes.
    
    """
    plt.subplots(figsize=(15,10))
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])
        plt.grid(True)
        ax.set_xticks(range(0,len(Z[0]),1))
        plt.title('Itération ' + str(i))
               
        Z = iteration_jeu(Z) 

    plt.show()


## Quatrième fonction
from numba import jit
@jit(nopython=True)
def calcul_nb_voisins_rapide(Z):
    """
    Arguments : 
    - Z = une liste de listes

    La fonction calcule le nombre de cellules voisines vivantes de chaque autre cellule, mais d'une façon plus rapide.
    """
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N



## Cinquième fonction
@jit(nopython=True)
def iteration_jeu_rapide(Z):
    """
    Arguments : 
    - Z = une liste de listes
    
    Cette fonction fait donc une simulation d'un tour du jeu pour une liste Z donnée, d'une manière plus rapide.
    
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins_rapide(Z)

    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z


## Sixième fonction
import numpy as np
import matplotlib.pyplot as plt

def step_i(Z_initial, iter):
    """
    Arguments : 
    - Z_initial = une liste de listes initiale
    - iter = nombre d'iterations 
    
    Cette fonction affiche l'étape i (choisie par l'utilisateur) du jeu de la vie, pour une matrice Z.
    """
    
    plt.figure(figsize = (5, 5))
    Z_i = np.array(Z_initial)
    for i in range(iter):
        Z_i = iteration_jeu(Z_i)
    
    plt.imshow(Z_i, extent=[0,len(Z_i[0]),0,len(Z_i)])
    plt.grid(True)
    plt.title("Affichage de l'itération " + str(iter)) 



########################################################### EXERCICE 2 #########################################################


## Septième fonction
def fig_digit(x, w, alpha):
    """
    Arguments : 
    - x = un vecteur associé à une image
    - w = un vecteur des coefficiens de régression
    - alpha (ou le pas) = un réel de 0 à 100 (avec alpha = 0 : x_mod = x)

    La fonction transforme une image x par l'opération donnée dans l'énoncé, puis affiche son image ainsi que l'image avant la transformation.
    """


    x_mod = x.reshape(784,1) - alpha * np.dot(w.T,x) * w / np.linalg.norm(w)**2
    

    plt.imshow(x_mod.reshape(28,28))
    plt.title("Image transformée")
    
    
## Huitième fonction    
def reglog(x, w, alpha):
    """
    Arguments : 
    - x = un vecteur associé à une image
    - w = un vecteur des coefficiens de régression
    - alpha (ou le pas) = un réel de 0 à 100 (avec alpha = 0 : x_mod = x)

    La fonction transforme une liste d'incidence d'une image par l'opération donnée dans l'énoncé et renvoi une nouvelle liste transformée.
    """


    return((x.reshape(784,1) - alpha * np.dot(w.T, x.reshape(784,1)) * w / np.linalg.norm(w)**2).reshape(28,28))


