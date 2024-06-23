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
def create_adjacency_list(edges: List[tuple]):
    adjacency_list = {}

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
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
    Algorithm:
    ==========================
    """

    def minimumArea(self, grid: List[List[int]]) -> int:

        min_row = None
        max_row = None

        min_col = None
        max_col = None

        for row_idx, row in enumerate(grid):
            for col_idx, col_val in enumerate(row):
                if col_val == 1:
                    # check for min col
                    if min_col is None or min_col > col_idx:
                        min_col = col_idx
                    # check for min row
                    if min_row is None or min_row > row_idx:
                        min_row = row_idx
                    # check for max col
                    if max_col is None or max_col < col_idx:
                        max_col = col_idx
                    # check for max row
                    if max_row is None or max_row < row_idx:
                        max_row = row_idx

        # calculate area of rectangle
        # upper_left = (min_row, min_col)
        # lower_right = (max_row, max_col)
        # print(f"{min_row =}")
        # print(f"{min_col =}")
        # print(f"{max_row =}")
        # print(f"{max_col =}")
        # area = (lower_right[0] - upper_left[0] + 1) * (
        #     lower_right[1] - upper_left[1] + 1
        # )

        area = 0
        if min_col is not None:
            area = (max_row - min_row + 1) * (max_col - min_col + 1)
        return area


def main():
    obj = Solution()
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
    ]
    output = 6

    # TS 2
    grid = [[0, 0], [1, 0]]

    Output: 1

    print(obj.minimumArea(grid))


if __name__ == "__main__":
    main()
