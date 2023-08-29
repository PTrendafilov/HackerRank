#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = {}
    # Visualize the Original tree
    for i in range(1, t_nodes+1):
        graph[i] = []
        
    for index in range(len(t_from)):
        graph[t_from[index]].append(t_to[index])
        graph[t_to[index]].append(t_from[index])
        
    print(graph)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
