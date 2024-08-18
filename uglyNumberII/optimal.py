from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
import heapq
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
Problem: https://leetcode.com/problems/ugly-number-ii
Help: https://www.youtube.com/watch?v=jRacRh6x4go
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n log2 n) [base 2 because 2 will the worst case]
    SC: O(n) [res array]

    ==========================
    Algorithm:
    ==========================
    """

    def nthUglyNumber(self, n: int) -> int:
        res = [0] * (n + 1)
        res[1] = 1

        idx_for_2 = 1
        idx_for_3 = 1
        idx_for_5 = 1
        idx = 2

        while idx <= n:
            val_2 = res[idx_for_2] * 2
            val_3 = res[idx_for_3] * 3
            val_5 = res[idx_for_5] * 5
            next_ugly = min(val_2, val_3, val_5)

            res[idx] = next_ugly

            if val_2 == next_ugly:
                idx_for_2 += 1
            if val_3 == next_ugly:
                idx_for_3 += 1
            if val_5 == next_ugly:
                idx_for_5 += 1

            idx += 1
        return res[n]


def main():
    obj = Solution()
    n = 10
    expected = 12
    print(obj.nthUglyNumber(n))


if __name__ == "__main__":
    main()
