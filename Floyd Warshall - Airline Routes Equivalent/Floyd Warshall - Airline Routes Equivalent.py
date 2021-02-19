#!/usr/bin/env python
# coding: utf-8

# Airline Routes Equivalent
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################

V = 6
F, T = False, True

def floydWarshall(graph): 
    dist = np.array(graph)
    
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                if dist[i, j] or (dist[i, k] and dist[k, j]):
                    dist[i][j] = T
    return np.array(dist)

#################################################################

graph1 = [[F, T, F, F, T, F],
          [F, F, F, F, T, F],
          [F, F, F, F, F, T],
          [T, F, F, F, F, F],
          [F, F, T, F, F, F],
          [F, F, F, F, F, F]]

graph2 = [[F, T, F, F, F, F],
          [F, F, F, F, T, F],
          [F, F, F, F, F, T],
          [T, T, F, F, F, T],
          [F, F, T, F, F, F],
          [F, F, F, F, F, F]]

dist1 = floydWarshall(graph1)
print(np.array(dist1, dtype='int'))
print()
dist2 = floydWarshall(graph2)
print(np.array(dist2, dtype='int'))

print()
if np.array_equal(dist1, dist2):
    print('Exists')
else:
    print('Doesnt Exist')

#################################################################
