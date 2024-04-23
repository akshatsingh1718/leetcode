from typing import List


class Solution:
    """
    TC: O(n * E * V)
    SC: O(n) [min_tree_starts] + O(n) [adj] + O(n) [visited] + O(n) [queue]

    Throws TLE

    Algo:
    1. Create adj list.
    2. start with every possible node (0->n).
    3. find the height and add the min to the min_tree_starts.
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        min_tree_starts = []

        # create adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        min_path = n
        for start in range(n):
            height = 0
            queue = []
            visited = set()
            queue.append([start])
            visited.add(start)
            while queue:
                nodes = queue.pop(0)

                temp_queue = []
                for node in nodes:
                    for n in adj[node]:
                        if n not in visited:
                            visited.add(n)
                            temp_queue.append(n)

                if temp_queue:
                    queue.append(temp_queue)
                else:
                    break
                height += 1

                if height > min_path:
                    break

            if height < min_path:
                min_tree_starts = [start]
                min_path = height
            elif height == min_path:
                min_tree_starts.append(start)

        return min_tree_starts


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
output = [1]

# TS2
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
output = [3, 4]

print(Solution().findMinHeightTrees(n, edges))
