#!/usr/bin/env python
# coding: utf-8

# Karger Randomized
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################


def add_vertex(V, v, V1):
    V1.append(v)
    V.remove(v)
    return V, V1


def remove_edge(E, V1, V2):
    Ebkp = E.copy()
    for edge in Ebkp:
        if edge[0] in V1 and edge[1] in V1:
            E.remove(edge)
        elif edge[0] in V2 and edge[1] in V2:
            E.remove(edge)
    return E

#################################################################


def kargermc(V, E):
    V1, V2 = [], []
    V, V2 = add_vertex(V, V[-1], V2)
    for i in range(len(V)-1, -1, -1):
        V, V1 = add_vertex(V, V[i], V1)
        E = remove_edge(E, V1, V2)
    return V1, V2, E

#################################################################


def print_kmc(V1, V2, E):
    print('Two sets of vertices : ')
    print(V1)
    print(V2)

    print('\nMin_cut : ')
    for e in E:
        for el in e:
            print(el, end='')
        print(end=', ')

#################################################################


V = [0, 1, 2, 3, 4]
E = [[0, 1], [0, 3], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
V1, V2, E = kargermc(V, E)
print_kmc(V1, V2, E)

#################################################################

print('\n\n')
inp = input('Enter Edges (e11 e12 e21 e22 .. en1 en2) : ').split()
inp = np.array(inp, dtype='int')

if len(inp) % 2 != 0:
    print('Input should be even. For n edges, 2n points are required')

E = inp.reshape(len(inp)//2, 2).tolist()
V = list(set(inp))

print()
print('Vertices : ')
print(V)
print('Edges : ')
print(E)
print()

V1, V2, E = kargermc(V, E)
print_kmc(V1, V2, E)
