import networkx as nx
import pygraphviz as pgv

G = nx.Graph(pgv.AGraph('data/grafo.dot'))

a = input("Ingrese una estacion de origen: ")
b = input("Ingrese una estacion de llegada: ")

if nx.has_path(G, a, b) == True:
    print(nx.shortest_path(G, a, b, None, "dijkstra"))
else:
    print(f'No hay forma de conectar esas dos estaciones por tren')