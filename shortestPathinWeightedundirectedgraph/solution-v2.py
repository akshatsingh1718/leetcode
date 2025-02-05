from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil, gcd
import heapq
from heapq import heapify, heappop, heappush
import itertools as it
import sys

# Check the current recursion limit
current_limit = sys.getrecursionlimit()

# Set a new recursion limit
new_limit = 10**5  # Set this to the desired limit
sys.setrecursionlimit(new_limit)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isListsSame(list1: ListNode, list2: ListNode):
    head1, head2 = list1, list2
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def printList(head: ListNode):
    lstr: str = ""
    while head is not None:
        lstr += str(head.val) + ", "
        head = head.next

    print(lstr)


# Graph utils
def create_adjacency_list(edges: List[tuple], directed=False):
    # When n nodes is told but graph does not have all the nodes present
    # this will prevent it from keyerror
    adjacency_list = defaultdict(lambda: [])

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []

        adjacency_list[u].append(v)
        if not directed:
            adjacency_list[v].append(u)

    return adjacency_list


# List utils


def list_to_ll(vector: List[int]):
    prv_node = None
    for i, val in enumerate(vector[::-1]):
        prv_node = ListNode(val, prv_node)
    return prv_node


# Tree Utils
def list_to_binary_tree(lst: List[int]):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current_node = queue.pop(0)

        if lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)

        i += 1

    return root


###################################################
################# Code Goes Here ##################
###################################################
"""
Problem: https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(V) * O( logV + E * logV )
    => O( V logV + EV logV )
    => O( V logV * (1 + E ~ E) )
    => O( EV logV )

    SC:

    ==========================
    Algorithm:
    ==========================
    In this question i only printed the path and not returned the
    shortest path value/weight
    """

    # def dijkstra2(self, adj: List[List[Tuple[int, int]]], src: int, dist: int, distances: List[int]) -> List[int]:

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        V = n
        src = 1
        dest = n

        adj = defaultdict(list)
        for u, v, w in edges:
            # undirected graph
            adj[u].append((v, w))
            adj[v].append((u, w))

        # create distances list
        distances = [float("inf")] * (V + 1)

        parent = list(range(V + 1))

        # make the source distance 0
        distances[src] = 0

        # create min heap
        heap = [(0, src)]  # (distance, node)

        while heap:  # TC: O(V)

            # pop the node
            curr_dist, u = heappop(heap)  # TC: O(log V)

            for v, dist in adj[u]:  # TC: O(E)
                # check if the new dist is smaller than the current dist in distances
                if distances[v] > dist + curr_dist:
                    distances[v] = dist + curr_dist
                    # add the new path to the heap
                    heappush(heap, (dist + curr_dist, v))  # TC: O(log V)

                    # change the parent
                    parent[v] = u

        res = []
        node = dest
        while node != src:
            res.append(node)
            node = parent[node]

        res.append(src)

        return res[::-1]


def main():
    obj = Solution()
    n = 5
    m = 6
    edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    print(obj.shortestPath(n, m, edges))


if __name__ == "__main__":
    main()
