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
Problem: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    # write find method
    def find(self, x: int, parent: List[int]) -> int:
        parent_of_x = parent[x]
        if x == parent_of_x:
            return x

        parent[x] = self.find(parent_of_x, parent)
        return parent[x]

    # Write union method
    def union(self, x: int, y: int, parent: List[int], rank: List[int]) -> None:
        x_parent = self.find(x, parent)
        y_parent = self.find(y, parent)

        if x_parent == y_parent:
            return None

        if rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
        elif rank[x_parent] < rank[y_parent]:
            parent[x_parent] = y_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        rank = [1] * V
        parent = list(range(V))

        for u in range(V):
            for v in adj[u]:

                if u > v:
                    continue

                parent_u = self.find(u, parent)
                parent_v = self.find(v, parent)

                if parent_u == parent_v:
                    return True

                self.union(u, v, parent, rank)
        return False


def main():
    obj = Solution()
    adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    V = len(adj)
    print(obj.isCycle(V, adj))


if __name__ == "__main__":
    main()
