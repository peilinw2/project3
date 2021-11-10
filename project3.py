"""
Math 560
Project 3
Fall 2021

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####

    
    start = None
    for v in adjList:
        for neigh in v.neigh:
            if neigh.dist > v.dist + adjMat[v.rank][neigh.rank] + tol:
                neigh.dist = v.dist + adjMat[v.rank][neigh.rank]
                neigh.prev = v
                start = neigh.prev

    if start is None:
        return []

    x = [0 for vertex in adjList]

    while x[start.rank] == 0:
            x[start.rank] += 1
            start = start.prev
            start_ = start

            path = [start_.rank]
            while start.prev != start_:
                start = start.prev
                path.append(start.rank)
                path.append(start.prev.rank)

            path.reverse()
            return path




    


"""
rates2mat
"""
def rates2mat(rates):
   
    return [[ -math.log(R) for R in row] for row in rates]
    

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
