import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime

print(datetime.now())
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all')

ox.plot_graph(graph)
plt.show()
  

import copy
"""
def ParcourirArretes(graphe, sommet, visites,i): #parcours profondeur 
    visites.add(sommet)  # Ajouter le sommet à l'ensemble des visites
    voisins = graphe.neighbors(sommet)  # Récupérer les voisins du sommet
    for voisin in voisins:
        if voisin not in visites:  # Vérifier si le voisin n'a pas été visité
            visiter_arrete(sommet, voisin)
            ParcourirArretes(graphe, voisin, visites,1)
            nx.set_edge_attributes(graphe, {(sommet, voisin, None): {'color': 'red'}})  # Changer la couleur de l'arête visitée
            visiter_arrete(voisin,sommet)
    if (i==0):
        dessiner_graphe(graphe)"""
"""
def ParcourirArretes(graphe, sommet):
    visites = set()  # Ensemble pour garder une trace des sommets visités
    pile = [(sommet, None)]  # Pile pour stocker les sommets à visiter et les arêtes parcourues

    while pile:
        sommet_actuel, arrete_precedente = pile.pop()

        if sommet_actuel not in visites:
            visites.add(sommet_actuel)

            if arrete_precedente is not None:
                visiter_arrete(arrete_precedente[0], arrete_precedente[1])

            voisins = graphe.neighbors(sommet_actuel)
            for voisin in voisins:
                if voisin not in visites:
                    #visiter_arrete(sommet_actuel, voisin)
                    pile.append((voisin, (sommet_actuel, voisin)))

    dessiner_graphe(graphe)

def visiter_arrete(sommet, voisin):
    print(f"Chemain entre {sommet} et {voisin}")

def dessiner_graphe(graphe):
    print(datetime.now())
    pos = nx.spring_layout(graphe)
    edge_colors = [data.get('color', 'skyblue') for _, _, data in graphe.edges(data=True)]
    nx.draw(graphe, pos, with_labels=False, node_size=2, node_color='red', edge_color=edge_colors, width=2)

    plt.show()

print(datetime.now())
graphe_modifie = copy.deepcopy(graph)
#ParcourirArretes(graphe_modifie, list(graphe_modifie.nodes)[0], set(),0)
ParcourirArretes(graphe_modifie, list(graphe_modifie.nodes)[0])
print(datetime.now())"""


def trouver_chemin_eulerien(graph):
    chemin_eulerien = []

    stack = [next(iter(graph.nodes()))]  # Sommet de départ arbitraire

    while stack:
        sommet = stack[-1]

        if graph.out_degree(sommet) == 0:
            chemin_eulerien.append(stack.pop())
        else:
            prochain_sommet = next(iter(graph[sommet]))
            graph.remove_edge(sommet, prochain_sommet)
            stack.append(prochain_sommet)

    return chemin_eulerien[::-1]


def parcourir_ville(graph):
    chemin_eulerien = trouver_chemin_eulerien(graph)

    print("Parcours de la ville :")
    for i in range(len(chemin_eulerien) - 1):
        sommet_actuel = chemin_eulerien[i]
        sommet_suivant = chemin_eulerien[i + 1]
        print(f"Route de {sommet_actuel} à {sommet_suivant}")

    print(f"Retour au sommet de départ : {chemin_eulerien[0]}")
    #dessiner_graphe(graph)

"""def parcourir_ville(graph):
    chemin_eulerien = trouver_chemin_eulerien(graph)

    # Création de la figure et du graphe
    plt.figure()
    pos = nx.spring_layout(graph)  # Layout pour le positionnement des noeuds
    nx.draw(graph, pos, with_labels=True, node_color='lightblue')

    print("Parcours de la ville :")
    for i in range(len(chemin_eulerien) - 1):
        sommet_actuel = chemin_eulerien[i]
        sommet_suivant = chemin_eulerien[i + 1]
        print(f"Route de {sommet_actuel} à {sommet_suivant}")
        nx.draw_networkx_edges(graph, pos, edgelist=[(sommet_actuel, sommet_suivant)], edge_color='red')

    print(f"Retour au sommet de départ : {chemin_eulerien[0]}")

    # Affichage du graphe
    plt.show()"""

def dessiner_graphe(graphe):
    print(datetime.now())
    pos = nx.spring_layout(graphe)
    edge_colors = [data.get('color', 'skyblue') for _, _, data in graphe.edges(data=True)]
    nx.draw(graphe, pos, with_labels=False, node_size=2, node_color='red', edge_color=edge_colors, width=2)

    plt.show()




graphe_modifie = copy.deepcopy(graph)
parcourir_ville(graphe_modifie)