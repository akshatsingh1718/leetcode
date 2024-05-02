from typing import List


class Solution:
    """
    TC: O(n^2) [finding distances separately for each node]
    SC: O(n) [for res] + O(n) [for adj list] + O(n) [for visited] + o(n) [for stack]
    """
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        # create adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = [0 for _ in range(n)]
        # Find out the distances
        for i in range(n):
            visited = {i}
            stack = [(i, 0)]
            distances = 0

            while len(stack) > 0:

                node, dist = stack.pop(0)
                distances += dist

                for n in adj[node]:
                    if n not in visited:
                        visited.add(n)
                        stack.append((n, dist + 1))

            res[i] = distances

        return res


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
output = [8, 12, 6, 10, 10, 10]
print(Solution().sumOfDistancesInTree(n, edges))
