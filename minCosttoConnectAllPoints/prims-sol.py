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
Problem: https://leetcode.com/problems/min-cost-to-connect-all-points/description/
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    1 <= V <= 1000
    TC: O(V*V) [to create adj] + O(E * logE)
    SC: O(V) [in_mst] + O(E) [heap] + O(V*E) [adj]

    ==========================
    Algorithm: `prims-algo`
    ==========================
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # find the distances of each point from every other point
        V = len(points)
        adj = [[] for _ in range(V)]

        # In optimal loop
        # for i, (x1, y1) in enumerate(points):
        #     for j, (x2, y2) in enumerate(points):
        #         if i == j:
        #             continue
        #         adj[i].append((j, abs(x1 - x2) + abs(y1 - y2)))

        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, V):
                (x2, y2) = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        in_mst = [False] * V
        heap = [(0, 0)]
        cost = 0

        while heap:  # TC: O(E) [for all edges]
            # pop the top
            wt, node = heappop(heap)  # TC: O(logE)

            # check visited status
            if in_mst[node]:
                continue

            # add the cost
            cost += wt

            # make as visited
            in_mst[node] = True

            # explore its neighbors
            for neig, neig_wt in adj[node]:
                heappush(heap, (neig_wt, neig))  # TC: O(logE)

        # return the min cost to make all the points connected
        return cost


def main():
    obj = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    Output = 20
    print(obj.minCostConnectPoints(points))


if __name__ == "__main__":
    main()
