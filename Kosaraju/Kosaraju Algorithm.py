#!/usr/bin/env python
# coding: utf-8

# Kosaraju's Algorithm
# Gourav Siddhad

#################################################################

from collections import defaultdict
import numpy as np

#################################################################

temp = []

def add_edge(graph, src, dst):
    graph[src].add(dst)
    return graph

def DFS(graph, v, visited):
    global temp
    visited[v]= True
    temp.append(v)
    for i in graph[v]: 
        if visited[i]==False: 
            DFS(graph, i, visited)

def fill_order(v, visited, stack): 
    visited[v]= True
    for i in adj_list[v]: 
        if visited[i]==False: 
            fill_order(i, visited, stack) 
    stack = stack.append(v) 

def get_transpose(adj_list): 
    g = defaultdict(set)
    for i in adj_list: 
        for j in adj_list[i]:
            g = add_edge(g, j, i)
    return g 

def SCCs(adj_list, V):
    scc = []
    global temp
    stack = [] 
    visited =[False]*(V) 
    for i in range(V): 
        if visited[i]==False: 
            fill_order(i, visited, stack) 
  
    gr = get_transpose(adj_list)
    visited =[False]*(V) 
    
    while stack: 
        i = stack.pop() 
        if visited[i]==False: 
            DFS(gr, i, visited) 
            scc.append(temp)
            temp = []
            
    del visited
    return scc

#################################################################

menu = dict()
menu['1'] = "Load Graph from File." 
menu['2'] = "Add Vertices"
menu['3'] = "Add Edge"
menu['4'] = 'Print Graph'
menu['5'] = "Strongly Connected Components"
menu['6'] = "Exit"

V = 0
adj_list = defaultdict(set)

while True: 
    options = menu.keys()
    print()
    print(' '*10, 'MENU', ' '*10)
    for entry in options: 
        print(entry, menu[entry])

    selection = input('Enter Option : ')
    
    if selection =='1': 
        inp = str(input('Enter File Name Containing the Graph : ')) # 'T02_Q4_input.txt'
        with open(inp, 'r') as infile:
            V = int(infile.readline())
            for line in infile:
                vals = line.rstrip().split()
                [adj_list[int(vals[0])].add((int(val))) for val in vals[1:]]

    elif selection == '2': 
        vertices = input('Enter Vertices seperated by space (v1 v2 .. vn) : ')
        vals = vertices.rstrip().split()
        for val in vals:
            if int(val) not in adj_list.keys():
                V += 1
                adj_list[int(val)]
            
    elif selection == '3':
        edges = input('Enter Edges seperated by space (src dst1 dst2 ... dstn) : ')
        vals = edges.rstrip().split()
        if int(vals[0]) not in adj_list.keys():
            V += 1
        for val in vals[1:]:
            if int(val) not in adj_list.keys():
                V += 1
            adj_list[int(vals[0])].add((int(val)))
        
    elif selection == '4': 
        print('\nGraph Adjacency List is : ')
        print(V, 'vertices')
        print(dict(adj_list))

    elif selection == '5':
        scc = SCCs(adj_list, V)
        print('\nTotal {:02d} SSC exists in the graph : '.format(len(scc)))
        for i, one in enumerate(scc):
            print('SCC {:02d} : {:}'.format(i+1, one))
        del scc
    
    elif selection == '6':
        break
        
    else: 
        print('Please Reenter Option')

#################################################################
