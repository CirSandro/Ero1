import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy
import random
import math
from decimal import Decimal, ROUND_DOWN

print(datetime.now())
graph = ox.graph_from_place("Le Plateau-Mont-Royal, Montréal, Canada", network_type='drive') #juste voiture


north = 45.570
south = 45.470
east = -73.530
west = -73.650

graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')

d_graph = nx.DiGraph()
n_graph = nx.Graph()
edges = set()
for (a, b, c) in graph.edges(data=True):
    d_graph.add_edge(a, b, weight=c)
    n_graph.add_edge(a, b, weight=c)
    edges.add((a, b))


ox.plot_graph(graph)
ox.plot_graph(graph_montreal)
plt.show()


def gps(depart, arrive,graph) : #il faut afficher le chemian on fait un tour de boucle, on repasse et re 1tour
    route = nx.shortest_path(graph, source=depart, target=arrive, weight='length')
    #fig, ax = ox.plot_graph_route(graph, route_by_length, node_size=0)
    L = []
    i = 0
    while(i+1<len(route)):
        L+=[(route[i],route[i+1])]
        i+=1
    L+=[(arrive,depart)] + L
    return L

def circuit_euler(graph,parcour,graph_montreal):
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

    circuit = circuit_euler(graph,circuit_non_oriente,graph_montreal)
else:
    graph_euler = graph_copy
    circuit = list(nx.eulerian_circuit(graph_euler))

circuit = depart_deneigeuse(circuit, 3373402628)

print(circuit)
print("Depart Depart deneigeuse Sherbrooke aller noeud::", circuit[0][0], "arrive bien à la fin:", circuit[-1][-1])


color = ['blue' for i in graph.edges]
for x,y in circuit:
    j = 0
    for u,v,z in graph.edges :
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
            # print(u,v) #3373402628
            # ox.plot_graph(graph, edge_color=color)
            # plt.show()
        j+=1


km_parcouru = 0

for u, v in circuit:
    km_parcouru += graph_montreal[u][v][0]['length']


km = 0

for u, v,z in graph.edges:
    km += graph[u][v][0]['length']

print("Distance parcourue:", km_parcouru, "m. Distance routes ville:",km)
#ici on fait avec véhicule le plus long/moin chere

vitess = 10
temps = (km_parcouru /1000)/vitess
print("temps de parcours:",temps)

jour = 500
conso = 1.1
prix_time = 0
if temps>8:
    prix_time = 8.8 + (temps-8)*1.3
else:
    prix_time= 1.1*temps
#1,1€ /h les 8premieres heures puis 1,3€ /h
prix = jour + conso*km_parcouru/1000 + prix_time
prix = math.floor(prix *100)/100 + 0.01
prix = Decimal(prix).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print("Prix deneigement outremont :", prix, "€")


ox.plot_graph(graph, edge_color=color)
plt.show()
