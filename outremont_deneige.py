
# #SANDRO2
# import osmnx as ox
# import matplotlib.pyplot as plt
# import networkx as nx
# from datetime import datetime
# from time import strftime
# import copy
# import random

# print(datetime.now())
# graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='drive') #juste voiture
# # graph_juste_montreal = ox.graph_from_place("Montréal, Canada", network_type='drive')
# # graph_juste_royal = ox.graph_from_place("Mont-Royal, Canada", network_type='drive')

# # graph_montreal = nx.compose(graph_juste_montreal,graph_juste_royal)

# north = 45.530
# south = 45.480
# east = -73.570
# west = -73.640
# #bbox = (north, south, east, west)

# graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')


# # route = nx.shortest_path(graph_montreal, source=213955306, target=213955379, weight='length') #213955379 and 213955306
# # fig, ax = ox.plot_graph_route(graph_montreal, route, node_size=0)
# # route = nx.shortest_path(graph, source=6188314203, target=9810017200, weight='length')
# # fig, ax = ox.plot_graph_route(graph, route, node_size=0)

# # print(6188314203 in graph[9810017200]) #9810017200, 6188314203
# # i=0
# # j=0
# # for a,b,c in graph.edges(data=True):
# #     i+=1
# #     if c['oneway']==True: #arrete est oriente
# #         j+=1
# # print("pour", i,"arretes, il y a",j,"oriente")

# d_graph = nx.DiGraph()
# n_graph = nx.Graph()
# edges = set()
# for (a, b, c) in graph.edges(data=True):
#     d_graph.add_edge(a, b, weight=c)
#     n_graph.add_edge(a, b, weight=c)
#     edges.add((a, b))
# # print(graph)
# # print(n_graph)
# # print(d_graph)


# ox.plot_graph(graph_montreal)
# plt.show()


# def gps(depart, arrive,graph) : #il faut afficher le chemian on fait un tour de boucle, on repasse et re 1tour
#     route = nx.shortest_path(graph, source=depart, target=arrive, weight='length')
#     #fig, ax = ox.plot_graph_route(graph, route_by_length, node_size=0)
#     L = []
#     i = 0
#     while(i+1<len(route)):
#         L+=[(route[i],route[i+1])]
#         i+=1
#     L+=[(arrive,depart)] + L
#     return L

# def circuit_euler(graph,parcour,graph_montreal):
#     circ = []
#     for u,v in parcour :
#         if v in graph[u]:
#             circ+=[(u,v)]
#         else :
#             circ+=gps(u,v,graph_montreal)
#     return circ



# graph_copy = copy.deepcopy(graph)
# graph_oriente = copy.deepcopy(graph)

# if not nx.is_eulerian(graph):
#     graph_temp = graph_copy.to_undirected()
#     graph_euler = nx.eulerize(graph_temp)
#     circuit_non_oriente = list(nx.eulerian_circuit(graph_euler))

#     circuit = circuit_euler(graph,circuit_non_oriente,graph_montreal)
# else:
#     graph_euler = graph_copy
#     circuit = list(nx.eulerian_circuit(graph_euler))



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
#     km_parcouru += graph_montreal[u][v][0]['length']


# km = 0

# for u, v,z in graph.edges:
#     km += graph[u][v][0]['length']

# print("Distance parcourue:", km_parcouru, "m. Distance routes ville:",km)
# #ici on fait avec véhicule le plus long/moin chere

# vitess = 10
# temps = (km_parcouru /1000)/vitess
# print("temps de parcours:",temps)

# jour = 500
# conso = 1.1
# prix_time = 0
# if temps>8:
#     prix_time = 8.8 + (temps-8)*1.3
# else:
#     prix_time= 1.1*temps
# #1,1€ /h les 8premieres heures puis 1,3€ /h
# prix = jour + conso*km_parcouru/1000 + prix_time
# prix = ((prix *100)//1)/100 + 0.01
# print("Prix deneigement outremont :", prix, "€")


# ox.plot_graph(graph, edge_color=color)
# plt.show()


# YOU1
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

color = ['blue' for i in graph.edges]
for x, y in circuit_depart:
    j = 0
    for u, v, z in graph.edges:
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
            ox.plot_graph(graph, edge_color=color)
            plt.show()
        j += 1

km_parcouru = 0
for u, v in circuit_depart:
    km_parcouru += graph_montreal[u][v][0]['length']

km = 0
for u, v, z in graph.edges:
    km += graph[u][v][0]['length']

print("Distance parcourue:", km_parcouru, "m. Distance routes ville:", km)

vitess = 10
temps = (km_parcouru / 1000) / vitess
print("Temps de parcours:", temps)

jour = 500
conso = 1.1
prix_time = 0
if temps > 8:
    prix_time = 8.8 + (temps - 8) * 1.3
else:
    prix_time = 1.1 * temps

prix = jour + conso * km_parcouru / 1000 + prix_time
prix = ((prix * 100) // 1) / 100 + 0.01
print("Prix déneigement Outremont :", prix, "€")

ox.plot_graph(graph, edge_color=color)
plt.show()
# fin YOU1

# import osmnx as ox
# import matplotlib.pyplot as plt
# import networkx as nx
# from datetime import datetime
# from time import strftime
# import copy
# import random

# print(datetime.now())
# graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='drive') #juste voiture

# north = 45.530
# south = 45.480
# east = -73.570
# west = -73.640

# graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')

# def gps(depart, arrive, graph):
#     route = nx.shortest_path(graph, source=depart, target=arrive, weight='length')
#     L = []
#     i = 0
#     while(i+1 < len(route)):
#         L += [(route[i], route[i+1])]
#         i += 1
#     L += [(arrive, depart)] + L
#     return L

# def circuit_euler(graph, parcour, graph_montreal):
#     circ = []
#     for u, v in parcour:
#         if v in graph[u]:
#             circ += [(u, v)]
#         else:
#             circ += gps(u, v, graph_montreal)
#     return circ

# graph_copy = copy.deepcopy(graph)
# graph_oriente = copy.deepcopy(graph)

# if not nx.is_eulerian(graph):
#     graph_temp = graph_copy.to_undirected()
#     graph_euler = nx.eulerize(graph_temp)
#     circuit_non_oriente = list(nx.eulerian_circuit(graph_euler))
#     circuit = circuit_euler(graph, circuit_non_oriente, graph_montreal)
# else:
#     graph_euler = graph_copy
#     circuit = list(nx.eulerian_circuit(graph_euler))

# start_node = 221106437  # Nœud de départ souhaité
# start_index = -1  # Index du nœud de départ dans le circuit Eulerien

# for i, (u, v) in enumerate(circuit):
#     if u == start_node:
#         start_index = i
#         break

# if start_index != -1:
#     path = gps(start_node, circuit[(start_index + 1) % len(circuit)][0], graph_montreal)
#     print("Chemin à partir du nœud de départ :", path)

#     color = ['blue' for i in graph.edges]
#     for x, y in circuit:
#         j = 0
#         for u, v, z in graph.edges(data=True):
#             if (x == u and y == v) or (x == v and y == u):
#                 color[j] = 'red'
#             j += 1

#     ox.plot_graph(graph, edge_color=color)
#     plt.show()
# else:
#     print("Le nœud de départ spécifié n'est pas présent dans le circuit Eulerien")

# km_parcouru = 0

# for u, v in circuit:
#     km_parcouru += graph_montreal[u][v][0]['length']

# km = 0

# for u, v, z in graph.edges:
#     km += graph[u][v][0]['length']

# print("Distance parcourue :", km_parcouru, "m. Distance routes ville :", km)

# vitess = 10
# temps = (km_parcouru / 1000) / vitess
# print("Temps de parcours :", temps)

# jour = 500
# conso = 1.1

# prix_time = 0
# if temps > 8:
#     prix_time = 8.8 + (temps - 8) * 1.3
# else:
#     prix_time = 1.1 * temps

# prix = jour + conso * km_parcouru / 1000 + prix_time
# prix = round(prix, 2)
# print("Prix déneigement Outremont :", prix, "€")

# ox.plot_graph(graph, edge_color=color)
# plt.show()







#SANDRO1
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








#YOUSSEF

# import osmnx as ox
# import matplotlib.pyplot as plt
# import networkx as nx
# from datetime import datetime
# from time import strftime
# import copy


# print("Début :", datetime.now())
# # graph = ox.graph_from_place("Montréal, Canada", network_type='all_private')
# graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all_private')
# # Convertir le graphe en graphe orienté
# graph = graph.to_directed()

# ox.plot_graph(graph)
# plt.show()
# print("Fin du graphique, début du code :", datetime.now())

# graph_copy = copy.deepcopy(graph)

# # Vérifier si le graphe est eulerien, sinon le rendre eulerien
# if not nx.is_eulerian(graph):
#     graph_temp = graph_copy.to_undirected()
#     graph_euler = nx.eulerize(graph_temp)
# else:
#     graph_euler = graph_copy

# circuit = list(nx.eulerian_circuit(graph_euler))

# print(circuit[:10])
# print(circuit[-10:])
# print("Départ :", circuit[0][0], "arrive bien à la fin :", circuit[-1][-1])

# print("Fin du parcours, début de la coloration :", datetime.now())

# color = ['blue' for i in graph.edges]
# for x, y in circuit:
#     j = 0
#     for u, v, z in graph.edges:
#         if (x == u and y == v) or (x == v and y == u):
#             color[j] = 'red'
#             ox.plot_graph(graph, edge_color=color)
#             plt.show()
#         j += 1

# print("Fin de la coloration, début du calcul de la distance :", datetime.now())

# km_parcouru = 0

# for u, v in circuit:
#     km_parcouru += graph_euler[u][v][0]['length']

# km = 0

# for u, v, z in graph.edges:
#     km += graph[u][v][0]['length']

# print("Distance parcourue :", km_parcouru, "km. Distance totale des routes de la ville :", km)

# print("Fin du calcul de la distance, début de l'affichage du graphe :", datetime.now())

# # ox.plot_graph(graph, edge_color=color)
# # plt.show()
# print("Fin :", datetime.now())
