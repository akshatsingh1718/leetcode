import numpy as np
from typing import List


def dfs(node, adj, visited):
    visited[node] = 1

    # iterate over all the neighbour's
    for n in adj[node]:
        if not visited[n]:
            dfs(n, adj, visited)


def noOfProvincesFromList(start_node: int, N: int, adj: List[List[int]]):
    visited = [0] * N

    provinces = 0

    for i in range(start_node, N):
        if not visited[i]:
            provinces += 1
            dfs(node=i, adj=adj, visited=visited)

    return provinces


def visitMatrix(node, adjMatrix, visited):
    visited[node] = 1

    for i, n in enumerate(adjMatrix[node]):
        if n != 1:  # there is no connection
            continue
        if not visited[i]:  # node is not yet visited
            visitMatrix(i, adjMatrix, visited)


def noOfProvincesFromMatrix(start_idx, N: int, adjMatrix: List[List[int]]):
    '''
    Runtime
    Details
    203ms
    Beats 85.73%of users with Python3
    Memory
    Details
    17.20MB
    Beats 82.32%of users with Python3
    '''
    visited = [0] * N

    provinces = 0
    for i in range(start_idx, N):
        if not visited[i]:
            provinces += 1
            visitMatrix(i, adjMatrix, visited)
    return provinces


def createAdjMatrix(adjList: List[List[int]]) -> List[List[int]]:
    return [[1 if j in node else 0 for j in range(len(adjList))] for node in adjList]


def createAdjList(adjMatrix: List[List[int]]):
    adjList = [[] for _ in range(len(adjMatrix))]

    for rIdx, row in enumerate(adjMatrix):
        for cIdx, col in enumerate(row):
            if col == 1:
                adjList[rIdx].append(cIdx)

    return adjList


def main():
    adjList = [
        [],
        [2],  # 1
        [1, 3],  # 2
        [2],  # 3
        [5],  # 4
        [4, 6],  # 5
        [5],  # 6
        [8],  # 7
        [7],  # 8
    ]

    adjMatrix = createAdjMatrix(adjList)
    # l = createAdjList(adjMatrix)
    # print(l)

    start_node = 1
    n = noOfProvincesFromMatrix(start_node, len(adjMatrix), adjMatrix)
    print(n)


if __name__ == "__main__":
    main()
