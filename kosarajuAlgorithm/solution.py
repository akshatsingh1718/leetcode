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
Problem: https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

Given an adjacency list, adj of Directed Graph, Find the number of strongly connected components in the graph.
Examples :
Input: adj[][] = [[2, 3], [0], [1], [4], []]

Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(V+E) [toposort] + O(V+E) [reverse adj] + O(V+E) [toposort for rev edg]
    SC: O(V) [visited nodes] + O(V) [stack]

    ==========================
    Algorithm:
    ==========================
    """

    def topoSortDFS(self, i: int, adj: List, visited: Set, stack: List):
        visited.add(i)

        for neig in adj[i]:
            if neig not in visited:
                self.topoSortDFS(neig, adj, visited, stack)

        # add to the stack
        stack.append(i)

    def kosaraju(self, adj):
        # start khan's algo / topological sort

        V = len(adj)
        visited = set()
        stack = []
        for i in range(V):  # TC: O(V+ E)
            if i not in visited:
                self.topoSortDFS(i, adj, visited, stack)

        # reverse all the edges and start the dfs in topological order from stack order
        reversed_adj = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                # u -> v reverse this to v -> u
                reversed_adj[v].append(u)

        components = 0
        visited = set()
        while stack:  # TC: O(V+ E)
            start_node = stack.pop()
            if start_node not in visited:
                components += 1
                self.topoSortDFS(start_node, reversed_adj, visited, [])

        return components


def main():
    obj = Solution()
    adj = [[2, 3], [0], [1], [4], []]
    output = 3
    print(obj.kosaraju(adj))


if __name__ == "__main__":
    main()
