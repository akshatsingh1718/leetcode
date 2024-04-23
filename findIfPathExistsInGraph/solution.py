from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        # create adjacency list
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # check for path if exist
        visited = [0 for _ in range(n)]
        queue = [source]

        while queue:
            pop = queue.pop(0)
            visited[pop] = 1
            if pop == destination:
                print(pop, destination)
                return True

            for node in adj[pop]:
                if visited[node] == 0:
                    visited[node] = 1
                    queue.append(node)

        return False


# TS1
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

# TS2
# n = 6
# edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
# source = 0
# destination = 5

print(Solution().validPath(n, edges, source, destination))
