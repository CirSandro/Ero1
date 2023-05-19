import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx

graph = ox.graph_from_place("Outremont, Montréal, Canada", network_type='all')
"""graph_und = graph.to_undirected()
graph_simpl = nx.Graph()
for u,v, key, data in graph_und.edges(keys=True, data=True):
    graph_simpl.add_edge(u,v,**data)
drone_path = [1234,5678,9101,1121]
fig,  ax =ox.plot_graph(graph_simpl, show=False, close=False, figsize=(10,10))
ox.plot_graph(graph_simpl, drone_path, route_linewidth=6, route_color='r', route_alpha=0.7, ax=ax)"""

ox.plot_graph(graph)
plt.show()

def parcours_rapide(graph):
    queue = []
    visited = {node:False for node in graph.nodes()}
    first_node = list(graph.nodes())[0]
    queue.append(list(graph.nodes())[0])
    visited[first_node] = True
    graph_display = graph.copy()
    while queue :
        current_node = queue.pop(0)

        graph_display.nodes[current_node]["visited"] = True

        #print("Noeux :", current_node)
        for neighbor in graph.neighbors(current_node):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

                graph_display.add_edge(current_node,neighbor)

    print("Parcours termine !")

    node_color = ["black" if graph_display.nodes[node].get("visited") else "blue" for node in graph_display.nodes()]
    edge_color = ["red" if graph_display.nodes[node].get("visited") else "gray" for node in graph_display.nodes()]
    nx.draw(graph_display,with_labels=False, node_color=node_color, edge_color=edge_color, node_size=10)
    plt.show()

parcours_rapide(graph)