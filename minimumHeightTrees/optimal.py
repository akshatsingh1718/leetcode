from typing import List
from collections import deque


class Solution:
    """
    TC:
    SC: 
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # if there is no neighbours then simply return [0] as starting of min height tree
        if n == 1:
            return [0]

        # neighbours count
        neighbours_count = dict()

        # create adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            neighbours_count[u] = neighbours_count.get(u, 0) + 1
            neighbours_count[v] = neighbours_count.get(v, 0) + 1

        # add the leave nodes to queue
        leaves = deque([node for node, count in neighbours_count.items() if count == 1])

        # While there are leaves
        while leaves:

            # if there is less than two depth left it means we found the min tree starting
            # we found the middle of the tree which will hold the starting of min tree
            if n <= 2:
                return list(leaves)

            # Iterate over all the leaves
            for _ in range(len(leaves)):
                # get the first leaf node to detach it from its neighbours
                leaf = leaves.popleft()

                # decrement n as we will detach the leaf node from its neighbours
                n -= 1
                # Iterate over all the neighbours of the leaf node and remove 1 from their's
                # neighbour nodes count as the leaf is now detached from them
                for leaf_neighbours in adj[leaf]:
                    neighbours_count[
                        leaf_neighbours
                    ] -= 1  # decrement the neighbour nodes count
                    # if the neigbours after detaching also becomes leaf then add them also to the leaves storage
                    if neighbours_count[leaf_neighbours] == 1:
                        leaves.append(leaf_neighbours)


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
output = [1]

# TS2
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
output = [3, 4]

# TS3
n = 1
edges = []
output = [0]

print(Solution().findMinHeightTrees(n, edges))
