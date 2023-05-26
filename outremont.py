import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from time import strftime
import copy


print(datetime.now())
graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all')

ox.plot_graph(graph)
plt.show()

def find_eulerian_cycle(graph):
    cycle = []
    start_vertex = next(iter(graph))
    stack = [start_vertex]

    while stack:
        current_vertex = stack[-1]

        if graph[current_vertex]:
            next_vertex = list(graph[current_vertex])[0]
            graph.remove_edge(current_vertex, next_vertex)
            stack.append(next_vertex)
        else:
            cycle.append(stack.pop())

    return cycle

def make_graph_eulerian(graph):
    odd_degree_vertices = [vertex for vertex in graph if graph.degree(vertex) % 2 != 0]

    while odd_degree_vertices:
        u = odd_degree_vertices.pop()
        v = odd_degree_vertices.pop()
        graph.add_edge(u, v)

    eulerian_cycle = find_eulerian_cycle(graph)
    return eulerian_cycle[::-1]

color = ['blue' for i in graph.edges]
graphe_modifie = copy.deepcopy(graph)
circuit = make_graph_eulerian(graphe_modifie)
for i in range(1,len(circuit)):
    print(f"Route de {circuit[i-1]} à {circuit[i]}")
    node_start = circuit[i-1]
    node_end = circuit[i]
    j = 0
    for u,v,z in graph.edges :
        if (node_start == u and node_end == v) or (node_start == v and node_end == u):
            color[j] = 'red'
        j+=1
    
print(f"Retour au depart {circuit[0]}")
print('red' in color)
ox.plot_graph(graph, edge_color=color)
plt.show()

"""
if nx.is_eulerian(graph) == False:
    print(graph)
    sec_graph = graph.to_undirected()
    print(sec_graph)
    eulerian_graph = nx.eulerize(sec_graph)
    print(eulerian_graph)
    if nx.is_eulerian(eulerian_graph):
        print('OUI')
else :
    eulerian_graph = copy.deepcopy(graph)"""
