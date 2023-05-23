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
ParcourirArretes(graphe_modifie, list(graphe_modifie.nodes)[0], set(),0)
print(datetime.now())