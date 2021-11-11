"""
Math 560
Project 3
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date: 11/12/2021
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""

def detectArbitrage(adjList, adjMat, tol=1e-15):
#set the initial dist and prev values
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
    adjList[0].dist = 0
    
#perform Bell-Ford algorithm and iterate |V|-1 times
    for iter in range(0, len(adjList) - 1):

#look at each vertex
        for vertex in adjList:
#check each neighbor of vertex and update predictions and previous vertex
            for neigh in vertex.neigh:
#only update if the new value is better
                if neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank] + tol:
                    neigh.dist = vertex.dist + adjMat[vertex.rank][neigh.rank]
                    neigh.prev = vertex

#run for 1 extra iteration to check the negative cost cycle
    start = None
#check each neighbor of vertex and update predictions and previous vertex
    for vertex in adjList:
#if the values changed, start tracing the negative cost cycle from this new vertex
        for neigh in vertex.neigh:
            if neigh.dist > vertex.dist + adjMat[vertex.rank][neigh.rank] + tol:
                neigh.dist = vertex.dist + adjMat[vertex.rank][neigh.rank]
                neigh.prev = vertex
                start = neigh.prev
#if no values changed, then there is not a negative cost cycle
    if start is None:
        return []
#trace back to find a vertex in the negative cost cycle
    x = [0 for vertex in adjList]

    while x[start.rank] == 0:
            x[start.rank] += 1
            start = start.prev
            start_ = start
#trace back to find the path that has an arbitrage opportunity
            path = [start_.rank]
            while start.prev != start_:
                start = start.prev
                path.append(start.rank)
                path.append(start.prev.rank)
#reverse the backwards path
            path.reverse()
            return path



    


"""
rates2mat
"""
def rates2mat(rates):
#retur  the adjacency matrix with the correctly weighted edges.   
    return [[ -math.log(R) for R in row] for row in rates]
    

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
