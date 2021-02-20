#!/usr/bin/env python
# coding: utf-8

# DAG All Paths
# Gourav Siddhad

#################################################################

from collections import defaultdict
import numpy as np

#################################################################


def dfs(s):
    path.append(s)
    if len(path) > 1:
        allpaths.append(np.array(path))
        print(*path)

    for node in adj[s]:
        dfs(node)

    path.pop()


def print_all(n):
    for i in range(n):
        if adj[i]:
            path = []
            dfs(i)

#################################################################

# edges = [(5, 0), (5, 2), (2, 3), (4, 0), (4, 1), (3, 1)]
# Sample 5 0 5 2 2 3 4 0 4 1 3 1


inp = input('Enter Edge Connections seperated by Space u1 v1 .. un vn : ')
edges = inp.split()
edges = np.array(edges, dtype='int')

n = len(set(edges))
path, allpaths = [], []

adj = defaultdict(list)
for i in range(0, len(edges), 2):
    u, v = edges[i], edges[i+1]
    adj[u].append(v)

print_all(n)
print()
print('There are total {:02d} possible paths in this graph.'.format(
    len(allpaths)))
print(*list(allpaths))

#################################################################
