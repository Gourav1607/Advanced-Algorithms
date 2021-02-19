#!/usr/bin/env python
# coding: utf-8

# Village Road Min Cost
# Gourav Siddhad

#################################################################

import numpy as np

#################################################################

def isValid(u, v, vstatus):
    if u == v: 
        return False
    if vstatus[u] == False and vstatus[v] == False: 
        return False
    elif vstatus[u] == True and vstatus[v] == True: 
        return False
    return True

def primMST(cost): 
    print('\n| {:^8} | {:^8} |'.format('Edge', 'Cost'))
    print('|' + '-'*10 + '+' + '-'*10 + '|')
    
    nVertex = len(cost)
    vstatus = [False] * nVertex
    vstatus[0] = True

    edge_count = 0
    mincost = 0
    while edge_count < nVertex-1:
        minn = 9999
        buf = [-1, -1]
        for i in range(nVertex):
            for j in range(nVertex):
                if cost[i][j] < minn and cost[i][j] != 0:
                    if isValid(i, j, vstatus):
                        minn = cost[i][j]
                        buf = [i, j]
  
        if buf[0] != -1 and buf[1] != -1:
            print("| {:^3d}  {:^3d} | {:^8d} |".format(edge_count, buf[0], buf[1], minn)) 
            edge_count += 1
            mincost += minn
            vstatus[buf[0]] = vstatus[buf[1]] = True
            
    print('|' + '-'*10 + '+' + '-'*10 + '|')
    print("| {:^8} | {:^8d} |".format('Min Cost', mincost), end='\n\n')

#################################################################

buildcost = [[0, 6, 7, 0, 3, 0],
             [6, 0, 0, 5, 4, 2],
             [7, 0, 0, 0, 8, 0],
             [0, 5, 0, 0, 0, 2],
             [3, 4, 8, 0, 0, 3],
             [0, 2, 0, 2, 3, 0]]

buildcost = np.array(buildcost)
print('Build Cost Adjacency Matrix\n')
print(buildcost)

primMST(buildcost)

#################################################################

# Sample : 0 2 0 6 0 2 0 3 8 5 0 3 0 0 7 6 8 0 0 9 0 5 7 9 0

inp = input('Enter Adjacency Matrix Values seperated by Space : ')
buildcost = inp.split()
buildcost = np.array(buildcost, dtype='int')

try:
    buildcost = np.reshape(buildcost, (int(np.sqrt(len(buildcost))), int(np.sqrt(len(buildcost)))))
    print('\nBuild Cost Adjacency Matrix\n')
    print(buildcost)
    primMST(buildcost)
except:
    print('Not a NxN Matrix. Please Try Again\n')
