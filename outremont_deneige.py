
#SANDRO2
import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy
import random

print(datetime.now())
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='drive') #juste voiture
graph_juste_montreal = ox.graph_from_place("Montréal, Canada", network_type='drive')
graph_juste_royal = ox.graph_from_place("Mont-Royal, Canada", network_type='drive')

graph_montreal = nx.compose(graph_juste_montreal,graph_juste_royal)

# route = nx.shortest_path(graph_montreal, source=213955306, target=213955379, weight='length') #213955379 and 213955306
# fig, ax = ox.plot_graph_route(graph_montreal, route, node_size=0)
# route = nx.shortest_path(graph, source=6188314203, target=9810017200, weight='length')
# fig, ax = ox.plot_graph_route(graph, route, node_size=0)

# print(6188314203 in graph[9810017200]) #9810017200, 6188314203
# i=0
# j=0
# for a,b,c in graph.edges(data=True):
#     i+=1
#     if c['oneway']==True: #arrete est oriente
#         j+=1
# print("pour", i,"arretes, il y a",j,"oriente")

d_graph = nx.DiGraph()
n_graph = nx.Graph()
edges = set()
for (a, b, c) in graph.edges(data=True):
    d_graph.add_edge(a, b, weight=c)
    n_graph.add_edge(a, b, weight=c)
    edges.add((a, b))
# print(graph)
# print(n_graph)
# print(d_graph)


ox.plot_graph(graph)
plt.show()


def gps(depart, arrive,graph) : #il faut afficher le chemian on fait un tour de boucle, on repasse et re 1tour
    if (depart==213955395 and arrive==213955379): 
        return[(depart,arrive)] #1,8km = demi tour,Prendre Ch. Bates en direction de Av. Rockland, Prendre à droite sur Av. du Manoir,Av. Rockland,Av. Dresden/Rue Jean-Talon O, Rue Fleet, Av. Beaumont, Chem. Rockland/Av. Rockland, Av. Rockland
    elif (depart==213955444 and arrive==213955379): #presque pareil apres 
        return[(depart,arrive)]
    elif(depart==213955379 and arrive==213955306): #rien en bas car deja deneiger
        return[(depart,arrive)] #je crois pas bon = probleme dcp avec tout avant on est pas passer par la route il faut revenir au point d'avant et refair le tour??
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
        else :#autre = chemain le plus cours entre u et v ?ap, pour coin creee arrete
            circ+=gps(u,v,graph_montreal) #ATTENTION, pour route sens unique en coin de graph peut etre faire gps sur Montreal entier
    return circ



graph_copy = copy.deepcopy(graph)
graph_oriente = copy.deepcopy(graph)

if not nx.is_eulerian(graph):
    graph_temp = graph_copy.to_undirected() #probleme = graphe n'est plus orienter mais sans cela compile pas
    graph_euler = nx.eulerize(graph_temp)
    circuit_non_oriente = list(nx.eulerian_circuit(graph_euler))

    circuit = circuit_euler(graph,circuit_non_oriente,graph_montreal)
else:
    graph_euler = graph_copy
    circuit = list(nx.eulerian_circuit(graph_euler))



print(circuit)
print("Depart:", circuit[0][0], "arrive bien à la fin:", circuit[-1][-1])


color = ['blue' for i in graph.edges]
for x,y in circuit:
    j = 0
    for u,v,z in graph.edges :
        if (x == u and y == v) or (x == v and y == u):
            color[j] = 'red'
            #ox.plot_graph(graph, edge_color=color)
            #plt.show()
        j+=1


km_parcouru = 0

for u, v in circuit:
    if (u==213955395 and v==213955379):
        km_parcouru+= 1800
    elif (u==213955444 and v==213955379): #presque pareil
        km_parcouru+= 2000
    elif(u==213955379 and v==213955306): #rien en bas car deja deneiger
        km_parcouru+=0
    else:
        km_parcouru += graph_montreal[u][v][0]['length']


km = 0

for u, v,z in graph.edges:
    km += graph[u][v][0]['length']

print("Distance parcourue:", km_parcouru, "m. Distance routes ville:",km)


ox.plot_graph(graph, edge_color=color)
plt.show()










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
