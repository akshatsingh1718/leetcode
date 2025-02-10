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
Problem: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(E+V) + O(ElogE) + O(4 * alpha)
    SC: O(2V) [parent + rank] + O(E) [edges_list]
    ==========================
    Algorithm: `kruskal-algo`
    ==========================
    """

    def union(self, u: int, v: int, parent: List[int], rank: List[int]) -> None:
        parent_u = parent[u]
        parent_v = parent[v]

        if parent_u == parent_v:
            return

        if rank[parent_u] > rank[parent_v]:
            parent[parent_v] = parent_u
        elif rank[parent_u] < rank[parent_v]:
            parent[parent_u] = parent_v
        else:
            # rank will only increase if both components have same rank
            rank[parent_v] += 1
            parent[parent_u] = parent_v

    def find(self, x: int, parent: List[int]) -> int:
        x_parent = parent[x]
        if x_parent == x:
            return x

        parent[x] = self.find(x_parent, parent)
        return parent[x]

    def kruskal(self, V: int, edges_list: List[List[int]]) -> int:

        # create parent and rank list
        parent = list(range(V))
        rank = [0] * V

        path_sum = 0
        # move over edges and check if they are connected or not
        for w, u, v in edges_list:  # TC: O(4 * alpha)
            # if the parent is same then u and v are connected
            if self.find(u, parent) == self.find(v, parent):
                continue

            path_sum += w
            # union of both u and v
            self.union(u, v, parent, rank)
        return path_sum

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:

        # add the adj to a edges list to apply sorting
        edges_list = []
        for u in range(V):  # TC: O(V + E)
            for v, w in adj[u]:
                # avoid duplicate edges
                if u < v:
                    edges_list.append((w, u, v))

        # sort the edges_list
        edges_list.sort()  # TC: O(E logE)

        # start kruskal algo
        return self.kruskal(V, edges_list)


def main():
    obj = Solution()
    adj = [
        [[1, 5], [2, 1]],
        [[2, 3], [0, 5]],
        [[0, 1], [1, 3]],
    ]
    V = 3
    output = 4
    print(obj.spanningTree(V, adj))


if __name__ == "__main__":
    main()
