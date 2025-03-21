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
    TC: O(n^2) + O(n^2) + O(n)
    SC: O(2n) ~ O(n)

    ==========================
    Algorithm:
    ==========================
    """

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        # find LIS (lowest increasing sub array)
        LIS = [1] * n  # every element is lowest on its own
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        # find LDS (lowest decreasing sub array)
        LDS = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)

        min_removals = n
        # find the min removals for each index
        for i in range(n):
            ith_removals = n + 1 - LDS[i] - LIS[i]
            # Both the LIS and LDS at the ith index should be greater than 1
            # since ith index include itself as well so we need +1 more to make a
            # mountain or negative slope on either side of the ith index
            if LDS[i] > 1 and LIS[i] > 1:
                min_removals = min(min_removals, ith_removals)

        return min_removals


def main():
    obj = Solution()
    nums = [2, 1, 1, 5, 6, 2, 3, 1]
    expected = 3

    # TS 2
    nums = [1, 3, 1]
    expected = 0
    print(obj.minimumMountainRemovals(nums))


if __name__ == "__main__":
    main()
