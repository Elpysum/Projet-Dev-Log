{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calcul_nb_voisins(Z):\n",
    "    forme = len(Z), len(Z[0])\n",
    "    N = [[0, ] * (forme[0]) for i in range(forme[1])]\n",
    "    for x in range(1, forme[0] - 1):\n",
    "        for y in range(1, forme[1] - 1):\n",
    "            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \\\n",
    "            + Z[x-1][y] + 0 +Z[x+1][y] \\\n",
    "            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]\n",
    "    return N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Z = [[0,0,0,0,0,0],\n",
    "    [0,0,0,1,0,0],\n",
    "    [0,1,0,1,0,0],\n",
    "    [0,0,1,1,0,0],\n",
    "    [0,0,0,0,0,0],\n",
    "    [0,0,0,0,0,0]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N = calcul_nb_voisins(Z)\n",
    "N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def iteration_jeu(Z):\n",
    "    forme = len(Z), len(Z[0])\n",
    "    N = calcul_nb_voisins(Z)\n",
    "    \"\"\"\n",
    "    On parcourt avec la boucle for chaque cellule de Z avec son nombre de voisins vivants.\n",
    "    Si une cellule vivante a 0, 1 ou 4 voisins vivants on lui affecte la valeur 0 (mort).\n",
    "    Si une cellule morte a exactement 3 voisins vivants on lui affecte 1 (naissance).\n",
    "    Tout autre cas garde la meme valeur.\n",
    "    \"\"\"\n",
    "    for x in range(1,forme[0]-1):\n",
    "        for y in range(1,forme[1]-1):\n",
    "            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):\n",
    "                Z[x][y] = 0\n",
    "            elif Z[x][y] == 0 and N[x][y] == 3:\n",
    "                Z[x][y] = 1\n",
    "    return Z\n",
    "\n",
    "\"\"\"\n",
    "Cette fonction fait donc une simulation d'un tour du jeu pour une matrice Z donnée.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "iteration_jeu(Z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# On créé une fonction \n",
    "def iterations_09(Z):\n",
    "    plt.subplots(figsize=(15,10))\n",
    "    for i in range(10):\n",
    "        ax = plt.subplot(2,5,i+1)\n",
    "        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])\n",
    "        plt.grid(True)\n",
    "        ax.set_xticks(range(0,len(Z[0]),1))\n",
    "        plt.title('Itération ' + str(i))\n",
    "               \n",
    "        Z = iteration_jeu(Z) \n",
    "\n",
    "    plt.show()\n",
    "\"\"\"\n",
    "Cette fonction affiche une simulation de 0 à 9 itérations pour une matrice Z de n'importe qu'elle taille. \n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Z = ([[0,0,0,0,0,0],\n",
    "    [0,0,0,1,0,0],\n",
    "    [0,1,0,1,0,0],\n",
    "    [0,0,1,1,0,0],\n",
    "    [0,0,0,0,0,0],\n",
    "    [0,0,0,0,0,0]])\n",
    "\n",
    "iterations_09(Z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import time\n",
    "from numba import jit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Z = np.array([[0,0,0,0,0,0],\n",
    "    [0,0,0,1,0,0],\n",
    "    [0,1,0,1,0,0],\n",
    "    [0,0,1,1,0,0],\n",
    "    [0,0,0,0,0,0],\n",
    "    [0,0,0,0,0,0]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@jit(nopython=True)\n",
    "\n",
    "def calcul_nb_voisins(Z):\n",
    "    forme = len(Z), len(Z[0])\n",
    "    N = [[0, ] * (forme[0]) for i in range(forme[1])]\n",
    "    for x in range(1, forme[0] - 1):\n",
    "        for y in range(1, forme[1] - 1):\n",
    "            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \\\n",
    "            + Z[x-1][y] + 0 +Z[x+1][y] \\\n",
    "            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]\n",
    "    return N\n",
    "\n",
    "# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!\n",
    "start = time.time()\n",
    "calcul_nb_voisins(Z)\n",
    "end = time.time()\n",
    "print(\"Elapsed (with compilation) = %s\" % (end - start))\n",
    "\n",
    "# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE\n",
    "start = time.time()\n",
    "calcul_nb_voisins(Z)\n",
    "end = time.time()\n",
    "print(\"Elapsed (after compilation) = %s\" % (end - start))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@jit(nopython=True)\n",
    "\n",
    "def iteration_jeu(Z):\n",
    "    forme = len(Z), len(Z[0])\n",
    "    N = calcul_nb_voisins(Z)\n",
    "\n",
    "    for x in range(1,forme[0]-1):\n",
    "        for y in range(1,forme[1]-1):\n",
    "            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):\n",
    "                Z[x][y] = 0\n",
    "            elif Z[x][y] == 0 and N[x][y] == 3:\n",
    "                Z[x][y] = 1\n",
    "    return Z\n",
    "\n",
    "\n",
    "# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!\n",
    "start = time.time()\n",
    "iteration_jeu(Z)\n",
    "end = time.time()\n",
    "print(\"Elapsed (with compilation) = %s\" % (end - start))\n",
    "\n",
    "# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE\n",
    "start = time.time()\n",
    "iteration_jeu(Z)\n",
    "end = time.time()\n",
    "print(\"Elapsed (after compilation) = %s\" % (end - start))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Z_huge = np.zeros((100, 100))\n",
    "\n",
    "Z_np = np.array(\n",
    "    [[0, 0, 0, 0, 0, 0],\n",
    "    [0, 0, 0, 1, 0, 0],\n",
    "    [0, 1, 0, 1, 0, 0],\n",
    "    [0, 0, 1, 1, 0, 0],\n",
    "    [0, 0, 0, 0, 0, 0],\n",
    "    [0, 0, 0, 0, 0, 0]])\n",
    "\n",
    "Z_huge[10:16, 10:16] = Z_np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fonction prenant comme argument une matrice d'initialisation du jeu et un entier 'iter'. \n",
    "Puis renvoi la forme de la matrice à l'itération 'iter'.\n",
    "\"\"\"\n",
    "def step_i(Z_initial, iter = 0):\n",
    "    plt.figure(figsize = (10, 10))\n",
    "    Z_i = np.array(Z_initial)\n",
    "    for i in range(iter):\n",
    "        Z_i = iteration_jeu(Z_i)\n",
    "    \n",
    "    plt.imshow(Z_i, extent=[0,len(Z_i[0]),0,len(Z_i)])\n",
    "    plt.grid(True)\n",
    "    plt.title(\"Affichage de l'itération \" + str(iter))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exemple : L'itération 5 de la matrice Z.\n",
    "step_i(Z,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as pw\n",
    "\n",
    "pw.interact(step_i, Z_initial = pw.fixed(Z_huge) , iter = (0, 30, 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
