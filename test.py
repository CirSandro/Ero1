import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy
import random

print(datetime.now())
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='drive') #juste voiture

north = 45.530
south = 45.480
east = -73.570
west = -73.640

graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')


def gps(depart, arrive, graph):
    route = nx.shortest_path(graph, source=depart, target=arrive, weight='length')
    L = []
    i = 0
    while(i+1<len(route)):
        L+=[(route[i],route[i+1])]
        i+=1
    L+=[(arrive,depart)] + L
    return L

def circuit_euler(graph, parcour, graph_montreal):
    circ = []
    for u,v in parcour :
        if v in graph[u]:
            circ+=[(u,v)]
        else :
            circ+=gps(u,v,graph_montreal)
    return circ

def depart_deneigeuse(circuit, node):
    index = -1
    for i, (u, v) in enumerate(circuit):
        if u == node:
            index = i
            break

    if index != -1:
        part1 = circuit[:index]
        part2 = circuit[index:]

        circuit_depart = part2 + part1

        return circuit_depart
    else:
        print("Le nœud de départ spécifié n'est pas présent dans le circuit.")
        return None


graph_copy = copy.deepcopy(graph)
graph_oriente = copy.deepcopy(graph)

if not nx.is_eulerian(graph):
    graph_temp = graph_copy.to_undirected()
    graph_euler = nx.eulerize(graph_temp)
    circuit_non_oriente = list(nx.eulerian_circuit(graph_euler))

    circuit = circuit_euler(graph, circuit_non_oriente, graph_montreal)
else:
    graph_euler = graph_copy
    circuit = list(nx.eulerian_circuit(graph_euler))

circuit_depart = depart_deneigeuse(circuit, 221106437)

print(circuit_depart)
print("Départ:", circuit_depart[0][0], "arrive bien à la fin:", circuit_depart[-1][-1])

# Diviser le circuit en deux pour les deux déneigeuses
half_len = len(circuit_depart) // 2
circuit_depart1 = circuit_depart[:half_len]
circuit_depart2 = circuit_depart[half_len:]

print("Circuit déneigeuse 1:", circuit_depart1)
print("Circuit déneigeuse 2:", circuit_depart2)

color = ['blue' for i in graph.edges]

# Colorier le circuit de la déneigeuse 1 en rouge
for x, y in circuit_depart1:
    j = 0
    for u, v, z in graph.edges:
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
        j += 1

# Colorier le circuit de la déneigeuse 2 en vert
for x, y in circuit_depart2:
    j = 0
    for u, v, z in graph.edges:
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'green'
        j += 1

km_parcouru1 = 0
for u, v in circuit_depart1:
    km_parcouru1 += graph_montreal[u][v][0]['length']

km_parcouru2 = 0
for u, v in circuit_depart2:
    km_parcouru2 += graph_montreal[u][v][0]['length']

km = 0
for u, v, z in graph.edges:
    km += graph[u][v][0]['length']

print("Distance parcourue déneigeuse 1:", km_parcouru1, "m. Distance parcourue déneigeuse 2:", km_parcouru2)
print("Distance totale des routes dans le quartier:", km)

vitess = 10
temps1 = (km_parcouru1 / 1000) / vitess
temps2 = (km_parcouru2 / 1000) / vitess

print("Temps de parcours déneigeuse 1:", temps1)
print("Temps de parcours déneigeuse 2:", temps2)

jour = 500
conso = 1.1
prix_time1 = 0
prix_time2 = 0

if temps1 > 8:
    prix_time1 = 8.8 + (temps1 - 8) * 1.3
else:
    prix_time1 = 1.1 * temps1

if temps2 > 8:
    prix_time2 = 8.8 + (temps2 - 8) * 1.3
else:
    prix_time2 = 1.1 * temps2

prix1 = jour + conso * km_parcouru1 / 1000 + prix_time1
prix2 = jour + conso * km_parcouru2 / 1000 + prix_time2

prix1 = ((prix1 * 100) // 1) / 100 + 0.01
prix2 = ((prix2 * 100) // 1) / 100 + 0.01

print("Prix déneigement déneigeuse 1 à Outremont:", prix1, "€")
print("Prix déneigement déneigeuse 2 à Outremont:", prix2, "€")

ox.plot_graph(graph, edge_color=color)
plt.show()
