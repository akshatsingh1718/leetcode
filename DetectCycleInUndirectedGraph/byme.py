from typing import List

"""
Every queue item will have a tuple of (src, parent)
src: will be used for traversing his neighbors
parent: will be used to check where src came from

if any adj node of the src has been visited and its not the
parent of src it means that someone has already visited
the adj node of the src meaning a cyclic graph 
"""


class Solution:
    """ """

    # Function to detect cycle in an undirected graph.
    def detect(self, src: int, adj: List[List[int]], visited: List[int]) -> bool:
        q = list()
        q.append((src, -1))  # src, parent
        visited[src] = 1

        while len(q) > 0:
            node, parent = q.pop(0)

            for i in adj[node]:
                if not visited[i]:
                    q.append((i, node))
                    visited[i] = 1
                elif i != parent:
                    return True
        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V

        for i in range(V):
            if not visited[i]:
                if self.detect(i, adj, visited):
                    return True
        return False


def main():
    s = Solution()

    adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    V = 5

    #########

    V = 4
    adj = [[], [2], [1, 3], [2]]

    res = s.isCycle(V, adj)
    print(res)


if __name__ == "__main__":
    main()
