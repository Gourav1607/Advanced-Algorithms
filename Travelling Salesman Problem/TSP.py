#!/usr/bin/env python
# coding: utf-8

# Travelling Salesman Problem
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################


def mwhc(graph, param, tpath):
    [flag, current, count, cost] = param

    if (count == len(graph) and graph[current][0]):
        answer.append(cost + graph[current][0])
        path.append(tpath + [current])
        return

    for i in range(len(graph)):
        if (flag[i] == False and graph[current][i]):
            flag[i] = True
            param = [flag, i, count + 1,  cost + graph[current][i]]
            mwhc(graph, param, tpath + [current])
            flag[i] = False


def printpath(answer, path, graph):
    fpath = path[np.argmin(answer)]
    fpath = fpath + [fpath[0]]

    print('{:8s} :'.format('Ham Path'), fpath)
    print('{:8s} : '.format('Distance'), end='')

    ans = 0
    for i in range(len(fpath)-1):
        if i == len(fpath)-2:
            print('{:d}'.format(graph[fpath[i]][fpath[i+1]]), end='')
        else:
            print('{:d}'.format(graph[fpath[i]][fpath[i+1]]), end=' + ')
        ans += graph[fpath[i]][fpath[i+1]]
    print(' =', ans)
    print()

#################################################################


answer, path = [], []

graph = [[0, 12, 5, 15],
         [10, 0, 25, 18],
         [16, 13, 0, 17],
         [17, 8,  4, 0]]

flag = [False for i in range(len(graph))]
flag[0] = True

param = [flag, 0, 1, 0]
mwhc(graph, param, [])
printpath(answer, path, graph)

#################################################################

answer, path = [], []

graph = [[0, 132, 217, 164, 58],
         [132, 0, 290, 201, 79],
         [217, 290, 0, 113, 303],
         [164, 201, 113, 0, 196],
         [58, 79, 303, 196, 0]]

flag = [False for i in range(len(graph))]
flag[0] = True

param = [flag, 0, 1, 0]
mwhc(graph, param, [])
printpath(answer, path, graph)

#################################################################
