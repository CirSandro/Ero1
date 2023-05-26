import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import copy
from datetime import datetime
from time import strftime

city = ox.graph_from_place('Montréal, Canada', network_type='all')

ox.plot_graph(city)
plt.show()

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
                    visiter_arrete(sommet_actuel, voisin)
                    pile.append((voisin, (sommet_actuel, voisin)))

    dessiner_graphe(graphe)

def visiter_arrete(sommet, voisin):
    #t = 1
    print(f"Chemain entre {sommet} et {voisin}")

def dessiner_graphe(graphe):
    print(datetime.now())
    pos = nx.spring_layout(graphe)
    edge_colors = [data.get('color', 'skyblue') for _, _, data in graphe.edges(data=True)]
    nx.draw(graphe, pos, with_labels=False, node_size=2, node_color='red', edge_color=edge_colors, width=2)

    plt.show()"""
"""
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
        #nx.set_edge_attributes(graphe, {(sommet_actuel, sommet_suivant, None): {'color': 'red'}})
        print(f"Route de {sommet_actuel} à {sommet_suivant}")

    print(f"Retour au sommet de départ : {chemin_eulerien[0]}")
    d#essiner_graphe(graph)

def dessiner_graphe(graphe):
    print(datetime.now())
    pos = nx.spring_layout(graphe)
    edge_colors = [data.get('color', 'skyblue') for _, _, data in graphe.edges(data=True)]
    nx.draw(graphe, pos, with_labels=False, node_size=2, node_color='red', edge_color=edge_colors, width=2)

    plt.show()"""

def trouver_chemin_eulerien(graph): # algorithme de Hierholzer
    chemin_eulerien = []

    stack = [next(iter(graph.nodes()))]  # Sommet de départ arbitraire
    print(len(graph))
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
    routes_empruntees = []

    print
    print("Parcours de la ville :")
    for i in range(len(chemin_eulerien) - 1):
        sommet_actuel = chemin_eulerien[i]
        sommet_suivant = chemin_eulerien[i + 1]
        routes_empruntees.append((sommet_actuel, sommet_suivant))
        i+=1
        print(f"Route de {sommet_actuel} à {sommet_suivant}")
    #print(i)
    print(f"Retour au sommet de départ : {chemin_eulerien[0]}")


def choisir_sommet_depart(graph):
    return list(graph.nodes)[0]  # Choisissez simplement le premier nœud du graphe comme nœud de départ

def trouver_circuit_eulerien_modifie(graph):
    stack = []  # Utilisé pour la recherche en profondeur itérative
    circuit = []  # Circuit eulerien modifié

    # Choisir un sommet de départ arbitraire
    depart = choisir_sommet_depart(graph)
    stack.append(depart)

    # Dictionnaire auxiliaire pour suivre les arêtes visitées
    arretes_visitees = {}

    while stack:
        sommet_actuel = stack[-1]

        if graph.out_degree(sommet_actuel) > 0:
            sommet_suivant = list(graph.successors(sommet_actuel))[0]  # Prendre le premier successeur non visité

            # Ajouter la route au circuit
            circuit.append((sommet_actuel, sommet_suivant))

            # Mettre à jour le dictionnaire auxiliaire des arêtes visitées
            if (sommet_actuel, sommet_suivant) in arretes_visitees:
                arretes_visitees[(sommet_actuel, sommet_suivant)] += 1
            else:
                arretes_visitees[(sommet_actuel, sommet_suivant)] = 1

            # Mettre à jour le graphe en supprimant l'arête visitée
            graph.remove_edge(sommet_actuel, sommet_suivant)

            # Empiler le sommet suivant pour poursuivre la recherche
            stack.append(sommet_suivant)
        else:
            # Si aucun successeur non visité n'est trouvé, retirer le sommet actuel de la pile
            stack.pop()

    # Ajouter la dernière route pour revenir au sommet de départ
    circuit.append((circuit[-1][1], depart))

    # Afficher le circuit
    for arrete in circuit:
        print(f"Route de {arrete[0]} à {arrete[1]}")
    print(f"Retour au depart {circuit[0][0]}")

    return circuit

print(datetime.now())
graphe_modifie = copy.deepcopy(city)
#ParcourirArretes(graphe_modifie, list(graphe_modifie.nodes)[0], set(),0)
#ParcourirArretes(graphe_modifie, list(graphe_modifie.nodes)[0])
#parcourir_ville(graphe_modifie)
trouver_circuit_eulerien_modifie(graphe_modifie)
print(datetime.now())