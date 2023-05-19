"""import networkx as nx
import osmnx as ox
from queue import PriorityQueue

def drone_path(start, goal, graph):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            break
        for neighbor in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph[current][neighbor]['weight']
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    
    path = reconstruct_path(came_from, start, goal)
    return path

def heuristic(a,b): #implementer votre heurstiaue ici
    return 0

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start :
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

graph = ox.graph_from_place('Montreal, Canada', network_type='all')

start_node = [1,1]
goal_node = [10,10]

path = drone_path(start_node, goal_node, graph)

print(path)"""

import numpy as np
import osmnx as ox

def calculate_distance(coords, path):
    distance = 0
    for i in range(len(path)-1):
        distance += np.linalg.norm(coords[path[i]] - coords[path[i+1]])
    return distance

def two_opt(coords, path):
    best_path = path.copy()
    improve = True
    while improve:
        improve = False
        for i in range(1, len(path)-2):
            for j in range(i+1, len(path)):
                if j - i == 1:
                    continue
                new_path = path.copy()
                new_path[i:j] = path[j-1:i-1:-1]
                new_distance = calculate_distance(coords, new_path)
                if new_distance < calculate_distance(coords, best_path):
                    best_path = new_path
                    improve = True
        path = best_path
    return best_path

#Coordonnées des intersections routières (exemples)
intersections = ox.graph_from_place('Montreal, Canada', network_type='all') #np.array([[0, 0], [1, 3], [4, 2], [3, 5], [2, 1]])

#Nombre de villes
num_cities = len(intersections)

#Création d'un chemin initial aléatoire
initial_path = np.random.permutation(num_cities)

#Application de l'algorithme 2-opt
optimized_path = two_opt(intersections, initial_path)

#Affichage du chemin optimisé
print("Chemin initial :", initial_path)
print("Chemin optimisé :", optimized_path)
print("Distance totale initiale :", calculate_distance(intersections, initial_path))
print("Distance totale optimisée :", calculate_distance(intersections, optimized_path))