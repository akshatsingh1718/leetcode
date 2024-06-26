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
    TC: O(n) 
    SC: O(n) [queue]

    ==========================
    Algorithm:
    ==========================
    1. Traverse through the nums and check if the ith bit is 0 or 1.
    2. if 1 then its all good.
    """

    def minKBitFlips(self, nums: List[int], k: int) -> int:

        i = 0
        ones_count = 0
        flip_count = 0
        n = len(nums)
        flipped_queue = []

        while i < n:

            # move i till we get a 0
            while i < n and (nums[i] + len(flipped_queue)) % 2 != 0:

                i += 1
                ones_count += 1

                # pop all the visited indexes
                while len(flipped_queue) > 0 and i > flipped_queue[0]:
                    flipped_queue.pop(0)

            # here we have a 0 possibly
            # i should be less than n
            # and n - i <= k since we want to flip the bits
            if i < n and i + k <= n:
                # flip the bit
                flip_count += 1
                ones_count += 1

                # next bit flip range
                next_bit_flip_range = i + k - 1
                flipped_queue.append(next_bit_flip_range)

            i += 1

        return -1 if ones_count != n else flip_count


def main():
    obj = Solution()
    nums = [0, 0, 0, 1, 0, 1, 1, 0]
    k = 3
    output = 3

    # Ts 2
    # nums = [1,1,0]
    # k = 2
    # Output= -1

    # TS 3
    # nums = [0,1,0]
    # k = 1
    # Output= 2
    print(obj.minKBitFlips(nums, k))


if __name__ == "__main__":
    main()
