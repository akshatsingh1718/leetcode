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

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        # find out the no of ones
        total_ones = sum(nums)
        if total_ones < 1:
            return 0

        # start a window of size no of ones and find the max
        # no of ones appearing in the window
        res = 0
        nums = nums + nums
        i = 0
        j = 0
        # calculate the first window ones occurrences
        ones_count = 0
        max_ones_count = 0
        while j < total_ones:
            ones_count += nums[j]
            j += 1

        # find the max ones for next windows
        max_ones_count = ones_count
        while i < n:
            ones_count = ones_count - nums[i] + nums[j]
            max_ones_count = max(max_ones_count, ones_count)
            i += 1
            j += 1

        return total_ones - max_ones_count


def main():
    obj = Solution()
    nums = [0, 1, 0, 1, 1, 0, 0]
    expected = 1

    # TS 2
    # nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    # expected = 2

    # TS 3
    # nums = [1, 1, 0, 0, 1]
    # expected = 0

    # TS 4
    # nums = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    # expected = 1
    print(obj.minSwaps(nums))


if __name__ == "__main__":
    main()
