from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
from heapq import heapify, heappop, heappush

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
Problem:
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
    Algorithm: `graph-dfs` `kahns-algo`
    ==========================
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # create adj list
        adj = create_adjacency_list(edges, directed=True)

        # create in-degreee
        indegree = [0 for _ in range(n)]

        # fill the indegrees
        for node in range(n):
            for child in adj[node]:
                indegree[child] += 1

        # find out the 0 indegree nodes
        queue = []
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        topo_sort = []
        # start the traversal
        while queue:
            node = queue.pop(0)
            topo_sort.append(node)

            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        # find the ancestor
        res = [set() for _ in range(n)]
        for node in topo_sort:
            for child in adj[node]:
                res[child].add(node)  # add node to ancestor of child
                res[child].update(res[node])  # add the ancestor of node as well

        # convert set to list and sort
        for node in range(n):
            res[node] = list(res[node])
            res[node].sort()

        return res


def main():
    obj = Solution()
    n = 8
    edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    expected = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

    # TS 2
    # edgeList = [[7, 5], [2, 5], [0, 7], [0, 1], [6, 1], [2, 4], [3, 5]]
    # n = 9
    print(obj.getAncestors(n, edgeList))


if __name__ == "__main__":
    main()
