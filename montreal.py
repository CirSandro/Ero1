import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import copy

city = ox.graph_from_place('Montréal, Canada', network_type='all')

ox.plot_graph(city)
plt.show()
 
#marche taille neoud bien
def ParcourirArretes(graphe):
    visites = set()  # Ensemble pour stocker les arêtes déjà visitées
    graphe_modifie = copy.deepcopy(graphe)  # Copie du graphe initial

    for u, v, data in graphe_modifie.edges(data=True):
        if 'color' not in data or data['color'] == 'skyblue':
            visiter_arrete(u, v)
            nx.set_edge_attributes(graphe_modifie, {(u, v, None): {'color': 'red'}})  # Changer la couleur de l'arête visitée
            #print(graph[u][v])

    dessiner_graphe(graphe_modifie)

def visiter_arrete(sommet, voisin):
    print(f"Visite de l'arête entre {sommet} et {voisin}")

def dessiner_graphe(graphe):
    pos = nx.spring_layout(graphe)
    edge_colors = [data.get('color', 'skyblue') for _, _, data in graphe.edges(data=True)]
    nx.draw(graphe, pos, with_labels=False, node_size=2, node_color='red', edge_color=edge_colors, width=2)

    plt.show()


ParcourirArretes(city)