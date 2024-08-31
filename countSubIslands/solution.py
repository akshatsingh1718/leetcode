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
Problem:
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n*m) [visit each cell] + O(n+m) [worst case visit all neighbors]
    SC: O(nxm) [if considering visited set]

    ==========================
    Algorithm:
    ==========================
    """

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        ROWS = len(grid2)
        COLS = len(grid2[0])

        def explore(i: int, j: int):
            nonlocal ROWS, COLS, grid2, grid1
            all_collides = True
            # skip non valid places
            if not (0 <= i < ROWS) or not (0 <= j < COLS) or grid2[i][j] == 0:
                return True

            # if land on grid2 is not present on grid1
            if grid2[i][j] != grid1[i][j]:
                all_collides = False

            grid2[i][j] = 0  # set visited as water
            directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for ix, jx in directions:
                all_collides &= explore(ix, jx)

            return all_collides

        no_of_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:  # land found
                    if explore(i, j):
                        no_of_islands += 1

        return no_of_islands


def main():
    obj = Solution()
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]

    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    expected = 3
    print(obj.countSubIslands(grid1, grid2))


if __name__ == "__main__":
    main()
