# import osmnx as ox
# import matplotlib.pyplot as plt
# import networkx as nx
# from datetime import datetime
# from time import strftime
# import copy
# import random

# print(datetime.now())
# graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all')


# ox.plot_graph(graph)
# plt.show()

# graph_copy = nx.DiGraph(graph) #graph_copy = copy.deepcopy(graph)

# if not nx.is_eulerian(graph):
#     graph_temp = graph_copy.to_directed() #probleme = graphe n'est plus orienter mais sans cela compile pas
#     graph_euler = nx.eulerize(graph_temp)
# else:
#     graph_euler = graph_copy




# circuit = list(nx.eulerian_circuit(graph_euler)) #non passe par sens interdit =drone

# print(circuit)
# print("Depart:", circuit[0][0], "arrive bien à la fin:", circuit[-1][-1])


# color = ['blue' for i in graph.edges]
# for x,y in circuit:
#     j = 0
#     for u,v,z in graph.edges :
#         if (x == u and y == v) or (x == v and y == u):
#             color[j] = 'red'
#             #ox.plot_graph(graph, edge_color=color)
#             #plt.show()
#         j+=1


# km_parcouru = 0

# for u, v in circuit:
#     km_parcouru += graph_euler[u][v][0]['length']


# km = 0

# for u, v,z in graph.edges:
#     km += graph[u][v][0]['length']

# print("Distance parcourue:", km_parcouru, "m. Distance routes ville:",km)


# ox.plot_graph(graph, edge_color=color)
# plt.show()

import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy


print("Début :", datetime.now())
# graph = ox.graph_from_place("Montréal, Canada", network_type='all_private')
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all_private')
# Convertir le graphe en graphe orienté
graph = graph.to_directed()

ox.plot_graph(graph)
plt.show()
print("Fin du graphique, début du code :", datetime.now())

graph_copy = copy.deepcopy(graph)

# Vérifier si le graphe est eulerien, sinon le rendre eulerien
if not nx.is_eulerian(graph):
    graph_temp = graph_copy.to_undirected()
    graph_euler = nx.eulerize(graph_temp)
else:
    graph_euler = graph_copy

circuit = list(nx.eulerian_circuit(graph_euler))

print(circuit[:10])
print(circuit[-10:])
print("Départ :", circuit[0][0], "arrive bien à la fin :", circuit[-1][-1])

print("Fin du parcours, début de la coloration :", datetime.now())

color = ['blue' for i in graph.edges]
for x, y in circuit:
    j = 0
    for u, v, z in graph.edges:
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
            ox.plot_graph(graph, edge_color=color)
            plt.show()
        j += 1

print("Fin de la coloration, début du calcul de la distance :", datetime.now())

km_parcouru = 0

for u, v in circuit:
    km_parcouru += graph_euler[u][v][0]['length']

km = 0

for u, v, z in graph.edges:
    km += graph[u][v][0]['length']

print("Distance parcourue :", km_parcouru, "km. Distance totale des routes de la ville :", km)

print("Fin du calcul de la distance, début de l'affichage du graphe :", datetime.now())

# ox.plot_graph(graph, edge_color=color)
# plt.show()
print("Fin :", datetime.now())
