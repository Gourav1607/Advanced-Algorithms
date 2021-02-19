# Kosaraju's Algorithm

Read graph from a text file. Format of the text file will be
```
12
0 3 5 17
1 4 6 7 2 10
2 1 7 9
. . .
. . .
```

The first line is the number of the vertex in the graph, and the rest of the lines are adjacency list. 

For example, line 0 3 5 17 means there is an the edge between node 0 to nodes 3, 5, and 17. 

Additionally, graph data structure should support insert vertex and insert edge functionality.

Programme should be able to print number of strongly connected components (SCC) and nodes in each of SCC.