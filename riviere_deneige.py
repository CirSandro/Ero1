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
graph = ox.graph_from_place("Rivière-des-prairies-pointe-aux-trembles, Montréal, Canada", network_type='drive') #juste voiture


north = 45.800
south = 45.520
east = -73.400
west = -73.680

graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')
# print(graph[8891093461])
# print(graph[8891081678])
# print(graph_montreal.edges())#2388532789
# route = nx.shortest_path(graph_montreal, source=2388532789, target=2388532780, weight='length') #8891081688   a    110468282
# fig, ax = ox.plot_graph_route(graph_montreal, route, node_size=0)#10913959485, 8875463745
# print(route)
d_graph = nx.DiGraph()
n_graph = nx.Graph()
edges = set()
for (a, b, c) in graph.edges(data=True):
    d_graph.add_edge(a, b, weight=c)
    n_graph.add_edge(a, b, weight=c)
    edges.add((a, b))

# print(graph[8891081688])
# def trouver_noeuds_pointant_vers(graphe, noeud_cible):
#     noeuds_pointant_vers = []
#     for noeud, voisins,z in graphe.edges:
#         if voisins == noeud_cible or noeud == noeud_cible:
#             noeuds_pointant_vers+=[(noeud,voisins)]
#     return noeuds_pointant_vers
# print(trouver_noeuds_pointant_vers(graph_montreal,8891081688))
# ox.plot_graph(graph)
# ox.plot_graph(graph_montreal)
# plt.show()

# graph_montreal = nx.compose(graph_montreal,graph) #8891093461 and 8891081678
# print(graph_montreal[8891081678])
ox.plot_graph(graph_montreal)
plt.show()


def gps(depart, arrive,graph) : #il faut afficher le chemian on fait un tour de boucle, on repasse et re 1tour
    if depart == 8891093461:
        depart = 573353392
    elif arrive == 8891093461:
        arrive = 573353392
    elif depart == 110468282 :
        depart = 10917010402
    elif arrive == 110468282 :
        arrive = 10917010402
    route = nx.shortest_path(graph, source=depart, target=arrive, weight='length')
    #fig, ax = ox.plot_graph_route(graph, route, node_size=0)
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
        if v in graph[u] :#or( u ==8891093461 and v == 8891081678) or (u==8891081688 and v==110468282):
            if u == 8891093461:
                u = 573353392
            elif v == 8891093461:
                v = 573353392
            elif u == 110468282 :
                u = 10917010402
            elif v == 110468282 :
                v = 10917010402
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
    #print(circuit_non_oriente)

    circuit = circuit_euler(graph,circuit_non_oriente,graph_montreal)
else:
    graph_euler = graph_copy
    circuit = list(nx.eulerian_circuit(graph_euler))

circuit = depart_deneigeuse(circuit, 2388532789)

print(circuit)
print("Depart deneigeuse Biodôme/Planétarium aller noeud:", circuit[0][0], "arrive bien à la fin:", circuit[-1][-1], ", retour entrepôt (les km sont comptés)")


color = ['blue' for i in graph.edges] #graph_montreal ici ou remettre autre node
for x,y in circuit:
    j = 0
    if x == 573353392:
        x = 8891093461
    elif y == 573353392:
        y = 8891093461
    elif x == 10917010402 :
        x = 110468282
    elif y == 10917010402 :
        y = 110468282

    for u,v,z in graph.edges :
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
            #print(u,v)
            # ox.plot_graph(graph, edge_color=color)
            # plt.show()
        j+=1
    if x == 8891093461:
        x = 573353392
    elif y == 8891093461:
        y = 573353392
    elif x == 110468282 :
        x = 10917010402
    elif y == 110468282 :
        y = 10917010402


km_parcouru = 20800 #5600 #du a une autoraut en bord d'arrete

att = 0
stock = 0
for u, v in circuit:
    # if (u in graph_montreal and v in graph_montreal[u]):
    # if (u in graph_montreal and v in graph_montreal[u]):
        km_parcouru += graph_montreal[u][v][0]['length']
    # else : 
    #   km_parcouru += graph[u][v][0]['length']
    #     att = 0
    # else :
    #     att = 1#marchera pas car pb des le premier noeuds
    #     stock = u



km = 20800

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
