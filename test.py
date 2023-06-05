import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy
import random
import matplotlib.colors as mcolors

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

# Demander à l'utilisateur le nombre de déneigeuses (n)
n = int(input("Entrez le nombre de déneigeuses : "))

# Diviser le circuit en n sous-circuits pour les n déneigeuses
circuit_departures = []
step = len(circuit_depart) // n
for i in range(n):
    circuit_departure = circuit_depart[i*step:(i+1)*step]
    circuit_departures.append(circuit_departure)

# Générer des couleurs aléatoires pour chaque déneigeuse
#colors = [random.choice(['blue', 'red', 'green', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta']) for _ in graph.edges]

#for i, circuit_departure in enumerate(circuit_departures):
#    color = colors[i]

    # Colorier le circuit de la déneigeuse i
#    for x, y in circuit_departure:
#        for j, (u, v, _) in enumerate(graph.edges):
#            if (x == u and y == v) or (x == v and y == u):
#                colors[j] = color




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

for i, circuit_departure in enumerate(circuit_departures):
    color = unique_colors[i]

    # Colorier le circuit de la déneigeuse i
    for x, y in circuit_departure:
        for j, (u, v, _) in enumerate(graph.edges):
            if (x == u and y == v) or (x == v and y == u):
                colors[j] = color




    km_parcouru = 0
    for u, v in circuit_departure:
        km_parcouru += graph_montreal[u][v][0]['length']

    km = 0
    for u, v, _ in graph.edges:
        km += graph[u][v][0]['length']

    print(f"Distance parcourue déneigeuse {i+1}: {km_parcouru} m. Distance totale des routes dans le quartier: {km} m.")

    vitess = 10
    temps = (km_parcouru / 1000) / vitess
    print(f"Temps de parcours déneigeuse {i+1}: {temps} heures")

    jour = 500
    conso = 1.1
    prix_time = 0

    if temps > 8:
        prix_time = 8.8 + (temps - 8) * 1.3
    else:
        prix_time = 1.1 * temps

    prix = jour + conso * km_parcouru / 1000 + prix_time
    prix = round(prix, 2)

    print(f"Prix déneigement déneigeuse {i+1} à Outremont: {prix} €")

ox.plot_graph(graph, edge_color=colors)
plt.show()
