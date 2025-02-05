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
Problem: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(EV logV) ~ O(2E log V) ~ O(E logV)
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        prices = [float("inf")] * n
        prices[src] = 0

        # k at first place since we want to minimize k stops
        heap = [(0, 0, src)]  # k stops, price, destination
        # TC: O( E logV )
        while heap:

            # curr_p, u, curr_k = heappop(heap)
            curr_k, curr_p, u = heappop(heap)

            for v, p in adj[u]:
                # print(f"{u} -> {v} | {p=}")
                if prices[v] > curr_p + p:

                    if curr_k == k and v != dst:
                        continue
                    prices[v] = curr_p + p
                    # add to the heap
                    heappush(heap, (curr_k + 1, curr_p + p, v))

        return -1 if prices[dst] == float("inf") else prices[dst]


def main():
    obj = Solution()
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    output = 700

    # TS 2
    n = 5
    flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src = 0
    dst = 2
    k = 2
    output = 7

    # TS 3
    n = 11
    flights = [
        [0, 3, 3],
        [3, 4, 3],
        [4, 1, 3],
        [0, 5, 1],
        [5, 1, 100],
        [0, 6, 2],
        [6, 1, 100],
        [0, 7, 1],
        [7, 8, 1],
        [8, 9, 1],
        [9, 1, 1],
        [1, 10, 1],
        [10, 2, 1],
        [1, 2, 100],
    ]
    src = 0
    dst = 2
    k = 4
    output = 11

    # TS 4
    # n = 5
    # flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    # src = 2
    # dst = 1
    # k = 1
    # output = -1
    print(obj.findCheapestPrice(n, flights, src, dst, k))


if __name__ == "__main__":
    main()
