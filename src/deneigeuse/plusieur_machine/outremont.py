import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy
import random
import math
from decimal import Decimal, ROUND_DOWN
import matplotlib.colors as mcolors

print(datetime.now())
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='drive') #juste voiture

north = 45.530
south = 45.480
east = -73.570
west = -73.640

graph_montreal = ox.graph_from_bbox(north, south, east, west, network_type='drive')

# Demander à l'utilisateur le nombre de déneigeuses (n)
n = int(input("Entrez le nombre de déneigeuses : "))

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
print("Départ deneigeuse St-Domonique aller noeud:", circuit_depart[0][0], "arrive bien à la fin:", circuit_depart[-1][-1], ", retour entrepôt (les km sont comptés)")

# # Diviser le circuit en deux pour les deux déneigeuses
# half_len = len(circuit_depart) // 2 #2véhicule
# circuit_depart1 = circuit_depart[:half_len] 
# L = nx.shortest_path(graph_montreal, source=circuit_depart1[-1][-1], target=221106437, weight='length')
# #print(L)
# i=0
# while(i+1<len(L)):
#     circuit_depart1+=[(L[i],L[i+1])]
#     i+=1
# circuit_depart2 = circuit_depart[half_len:]
# L= nx.shortest_path(graph_montreal, source=221106437, target=circuit_depart1[0][0], weight='length')
# L2=[]
# i=0
# while(i+1<len(L)):
#     L2+=[(L[i],L[i+1])]
#     i+=1
# circuit_depart2 = L2 + circuit_depart2

# print("Circuit déneigeuse 1:", circuit_depart1)
# print("Circuit déneigeuse 2:", circuit_depart2)

# color = ['blue' for i in graph.edges]

# # Colorier le circuit de la déneigeuse 1 en rouge
# for x, y in circuit_depart1:
#     j = 0
#     for u, v, z in graph.edges:
#         if (x == u and y == v) or (x == v and y == u):
#             color[j] = 'red'
#         j += 1

# # Colorier le circuit de la déneigeuse 2 en vert
# for x, y in circuit_depart2:
#     j = 0
#     for u, v, z in graph.edges:
#         if (x == u and y == v) or (x == v and y == u):
#             color[j] = 'green'
#         j += 1
def lister(L):
    Li=[]
    i=0
    while(i+1<len(L)):
        Li+=[(L[i],L[i+1])]
        i+=1
    return Li

machines = []
pas = len(circuit_depart) // n
for i in range(n):
    circuit_machine = circuit_depart[i*pas:(i+1)*pas]
    L1 = nx.shortest_path(graph_montreal, source=221106437, target=circuit_machine[0][0], weight='length')
    L2 = nx.shortest_path(graph_montreal, source=circuit_machine[-1][-1], target=221106437, weight='length')
    if (len(L1)>1):
        circuit_machine = lister(L1) + circuit_machine
    if (len(L2)>1) : 
        circuit_machine += lister(L2)
    machines.append(circuit_machine)





def machine_1(km_parcouru) :
    vitess = 10
    temps = (km_parcouru / 1000) / vitess
    duree = math.floor(temps *100)/100 + 0.01
    duree = Decimal(duree).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    print("Temps de parcours de cette déneigeuse :", duree, "heures")

    jour = 500
    conso = 1.1
    prix_time = 0

    if temps > 8:
        prix_time = 8.8 + (temps - 8) * 1.3
    else:
        prix_time = 1.1 * temps

    prix = jour + conso * km_parcouru / 1000 + prix_time

    prix = ((prix * 100) // 1) / 100 + 0.01

    print("Prix déneigement de cette déneigeuse à Outremont:", prix, "€")

def machine_2(km_parcouru) :
    vitess = 20
    temps = (km_parcouru / 1000) / vitess
    duree = math.floor(temps *100)/100 + 0.01
    duree = Decimal(duree).quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    print("Temps de parcours de cette déneigeuse :", duree, "heures")

    jour = 800
    conso = 1.3
    prix_time = 0

    if temps > 8:
        prix_time = 10.4 + (temps - 8) * 1.5
    else:
        prix_time = 1.3 * temps

    prix = jour + conso * km_parcouru / 1000 + prix_time

    prix = ((prix * 100) // 1) / 100 + 0.01

    print("Prix déneigement de cette déneigeuse à Outremont:", prix, "€")


# colors = [random.choice(['blue', 'red', 'green', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta']) for _ in graph.edges]

# for i, circuit_machine in enumerate(machines):
#     color = colors[i]

#     # Vérifier que la couleur de la déneigeuse i est différente des autres déneigeuses
#     for j in range(i):
#         if colors[j] == color:
#             # Modifier la couleur si elle est identique à une autre déneigeuse
#             color = random.choice(['blue', 'red', 'green', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta'])
#             colors[i] = color
#             break

#     # Colorier le circuit de la déneigeuse i
#     for x, y in circuit_machine:
#         for j, (u, v, _) in enumerate(graph.edges):
#             if (x == u and y == v) or (x == v and y == u):
#                 colors[j] = color

#     # Vérifier que la couleur de la déneigeuse i est différente des autres déneigeuses (à nouveau)
#     for j in range(i):
#         if colors[j] == color:
#             # Afficher un avertissement si la couleur n'a pas pu être modifiée
#             print(f"Attention : La déneigeuse {i+1} a la même couleur qu'une autre déneigeuse.")
#             break

colors = [random.choice(list(mcolors.CSS4_COLORS.keys())) for _ in graph.edges]

# Liste des couleurs uniques pour chaque déneigeuse
unique_colors = []
for i in range(n):
    # Vérifier que la couleur est unique
    while True:
        color = random.choice(list(mcolors.CSS4_COLORS.keys()))
        if color not in unique_colors:
            unique_colors.append(color)
            break

for i, circuit_machine in enumerate(machines):
    color = unique_colors[i]

    # Colorier le circuit de la déneigeuse i
    for x, y in circuit_machine:
        for j, (u, v, _) in enumerate(graph.edges):
            if (x == u and y == v) or (x == v and y == u):
                colors[j] = color



    km_parcouru = 3000
    for u, v in circuit_machine:
        km_parcouru += graph_montreal[u][v][0]['length']

# km_parcouru2 = 3000
# for u, v in circuit_depart2:
#     km_parcouru2 += graph_montreal[u][v][0]['length']

    km = 0
    for u, v, z in graph.edges:
        km += graph[u][v][0]['length']
    
    print(f"Distance parcourue déneigeuse {i+1}: {km_parcouru} m. Distance totale des routes dans le quartier: {km} m.")
    machine_1(km_parcouru)

# print("Distance parcourue déneigeuse 1:", km_parcouru1, "m. Distance parcourue déneigeuse 2:", km_parcouru2)
# print("Distance totale des routes dans le quartier:", km)



#machine_1(km_parcouru1,km_parcouru2)
# machine_2(km_parcouru1,km_parcouru2)

ox.plot_graph(graph, edge_color=color)
plt.show()
