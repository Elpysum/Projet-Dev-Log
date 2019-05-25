{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
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
   "execution_count": 2,
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
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0, 0, 0, 0],\n",
       " [0, 1, 3, 1, 2, 0],\n",
       " [0, 1, 5, 3, 3, 0],\n",
       " [0, 2, 3, 2, 2, 0],\n",
       " [0, 1, 2, 2, 1, 0],\n",
       " [0, 0, 0, 0, 0, 0]]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "N = calcul_nb_voisins(Z)\n",
    "N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nCette fonction fait donc une simulation d'un tour du jeu pour une matrice Z donnée.\\n\""
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
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
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0, 0, 0, 0],\n",
       " [0, 0, 1, 0, 0, 0],\n",
       " [0, 0, 0, 1, 1, 0],\n",
       " [0, 0, 1, 1, 0, 0],\n",
       " [0, 0, 0, 0, 0, 0],\n",
       " [0, 0, 0, 0, 0, 0]]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iteration_jeu(Z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nCette fonction affiche une simulation de 0 à 9 itérations pour une matrice Z de n'importe qu'elle taille. \\n\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
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
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x720 with 10 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
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
   "execution_count": 8,
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
   "execution_count": 9,
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
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Elapsed (with compilation) = 0.4108760356903076\n",
      "Elapsed (after compilation) = 0.0\n"
     ]
    }
   ],
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
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Elapsed (with compilation) = 0.2426624298095703\n",
      "Elapsed (after compilation) = 0.0\n"
     ]
    }
   ],
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
   "execution_count": 12,
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
   "execution_count": 13,
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
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Exemple : L'itération 5 de la matrice Z.\n",
    "step_i(Z,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2b6a85fc14b840649375e18b9abc7476",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(IntSlider(value=0, description='iter', max=30), Output()), _dom_classes=('widget-interac…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.step_i(Z_initial, iter=0)>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
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
