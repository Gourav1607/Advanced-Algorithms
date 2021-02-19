#!/usr/bin/env python
# coding: utf-8

# Topological Sort BFS
# Gourav Siddhad

#################################################################

from collections import defaultdict
import numpy as np

#################################################################

def topological_sort(adj, V):
    in_degree = [0]*(V)
    queue, order = [], []
    count = 0
    
    for i in adj: 
        for j in adj[i]: 
            in_degree[j] += 1
            
    for i in range(V): 
        if in_degree[i] == 0: 
            queue.append(i)
    
    while queue:
        u = queue.pop(0) 
        order.append(u) 

        for i in adj[u]: 
            in_degree[i] -= 1
            if in_degree[i] == 0: 
                queue.append(i) 

        count += 1

    if count != V: 
        print ("There exists a cycle in the graph")
    else : 
        return order

#################################################################

# edges = [(5, 0), (5, 2), (2, 3), (4, 0), (4, 1), (3, 1)]
# Sample 5 0 5 2 2 3 4 0 4 1 3 1

inp = input('Enter Edge Connections seperated by Space u1 v1 .. un vn : ')
edges = inp.split()
edges = np.array(edges, dtype='int')

n = len(set(edges))
path = []

adj = defaultdict(list)
for i in range(0, len(edges), 2):
    u, v = edges[i], edges[i+1]
    adj[u].append(v)

order = topological_sort(adj, n)
print('\nTopological Sorting using Kahn\'s Algorithm is : ', *order)

#################################################################
