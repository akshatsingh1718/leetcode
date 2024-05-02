"""
References:
1. https://www.youtube.com/watch?v=b6DrMMHFiL0
"""

from typing import List


class Solution:
    """
    TC: O(n^2) [finding distances separately for each node]
    SC: O(n) [for res] + O(n) [for adj list] + O(n) [for visited] + o(n) [for stack]
    """

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create Adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS 1
        ## 1. find the result for root = 0
        ## 2. find the no of children of each node

        children = [0 for _ in range(n)]
        result_of_root = 0

        def dfs_count_child(curr_node: int, parent_node: int, current_depth: int):
            """
            1. Find the children of each node
            2. Find the result of root node = 0
            """
            nonlocal adj, children, result_of_root, n

            # no of children for the current node
            no_of_children = 0
            # append the current depth for the root node
            result_of_root += current_depth

            for node in adj[curr_node]:
                if node != parent_node:

                    # go deeper and find the depth for other child nodes as well
                    no_of_children += dfs_count_child(
                        curr_node=node,
                        parent_node=curr_node,
                        current_depth=current_depth + 1,
                    )

            children[curr_node] = no_of_children + 1  # count itself as well

            return children[curr_node]

        dfs_count_child(0, parent_node=-1, current_depth=0)
        # create a result array to return and assign the computed root value
        result = [0 for _ in range(n)]
        result[0] = result_of_root

        # DFS 2
        ## iterate over each node and use formula to find their distances from each node
        ## Formula = (Distance of parent from all nodes)
        ##           - [No of children + 1 (for node itself)]
        ##           - [Remaining nodes = (no of all nodes) - (No of children + 1) ]
        def dfs_find_distances(curr_node: int, parent_node: int):
            nonlocal adj, children, result

            for child in adj[curr_node]:
                if child != parent_node:
                    result[child] = (
                        result[curr_node] - children[child] + (n - children[child])
                    )
                    dfs_find_distances(curr_node=child, parent_node=curr_node)

        dfs_find_distances(curr_node=0, parent_node=-1)

        return result


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
output = [8, 12, 6, 10, 10, 10]
print(Solution().sumOfDistancesInTree(n, edges))
