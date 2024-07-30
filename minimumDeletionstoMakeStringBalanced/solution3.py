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
Problem:
Help:
"""


class Solution:
    """(Improvement on solution2.py)
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) [left_b_counts] + O(n) [right_a_counts] + O(n) [find min sum] ~ O(n)
    SC: O(n) [right_a_counts] ~ O(n)

    ==========================
    Algorithm:
    ==========================
    1. create an array for storing no of b's sitting on left side of any given index.
    2. Sum the each index left b and right a values which will tell us that how many a and b should we remove from any given index to make the string balanced and the min sum will give us the min operations.
    """

    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        # create right a count
        right_a_counts = [0 for _ in range(n)]
        a_count = 0
        i = n - 1
        while i > -1:
            right_a_counts[i] = a_count
            if s[i] == "a":
                a_count += 1
            i -= 1

        min_operations = float("inf")
        left_b = 0
        for i, char in enumerate(s):

            min_operations = min(min_operations, left_b + right_a_counts[i])
            left_b += 1 if char == "b" else 0

        return min_operations


def main():
    obj = Solution()
    s = "aababbab"
    expected = 2

    # TS 2
    s = "bbaaaaabb"
    expected = 2
    print(obj.minimumDeletions(s))


if __name__ == "__main__":
    main()
