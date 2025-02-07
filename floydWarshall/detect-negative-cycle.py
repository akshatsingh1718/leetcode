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
Problem: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
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

    Question:
    The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix. mat[i][j] denotes the weight of the edge from i to j. If mat[i][j] = -1, it means there is no edge from i to j.
    Note: Modify the distances for every pair in place.

    Examples :

    Input: mat = [[0, 25], [-1, 0]]

    Output: [[0, 25], [-1, 0]]

    Explanation: The shortest distance between every pair is already given(if it exists).
    """

    def shortest_distance(self, matrix) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for via in range(ROWS):
            for i in range(ROWS):
                for j in range(COLS):

                    i_to_via = matrix[i][via] if matrix[i][via] != -1 else float("inf")
                    via_to_j = matrix[via][j] if matrix[via][j] != -1 else float("inf")
                    i_to_j = matrix[i][j] if matrix[i][j] != -1 else float("inf")

                    if i_to_j > i_to_via + via_to_j:
                        matrix[i][j] = i_to_via + via_to_j

        for r in matrix:
            print(r)
        # if the matrix[i][i] < 0 it means we have a cycle
        for i in range(ROWS):
            if matrix[i][i] < 0:
                return True

        return False


def main():
    obj = Solution()
    mat = [[0, 4, -1], [-1, 0, -3], [-4, -1, 0]]
    output = True
    print(obj.shortest_distance(mat))


if __name__ == "__main__":
    main()
