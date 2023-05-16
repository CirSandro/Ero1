import osmnx as ox
import matplotlib.pyplot as plt

city = ox.graph_from_place('Montréal, Canada', network_type='all')

ox.plot_graph(city)
plt.show()
