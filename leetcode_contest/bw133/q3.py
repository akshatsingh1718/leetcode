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

    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)
        def flip(i):
            nonlocal n
            for j in range(i, n):
                nums[j] = abs(nums[j] - 1)

        i = 0
        ops = 0
        ones = 0
        bits_flipped = 0
        while i < n:
            # bit is not fipped
            if bits_flipped % 2 == 0:
                # skip 1 bit
                while i < n and nums[i] == 1:
                    ones += 1
                    i += 1
            else:
                # skip 1 bit
                while i < n and abs(nums[i] - 1) == 1:
                    ones += 1
                    i += 1

            if i < n:
                ops += 1
                bits_flipped += 1
            
            # when reached at bit 0
            # if i < n:
            #     ops += 1
            #     bits_flipped += 1

            #     while  i < n:
            #         # check if bit is 1 or not 
            #         # not flipped
            #         if bits_flipped % 2 == 0:
            #             if nums[i] == 0:
            #                 break
            #         # flipped
            #         else:
            #             if abs(nums[i] - 1) == 0:
            #                 break

            #         i += 1

                # # flip(i)
                # first_zero = n
                # for j in range(i, n):
                #     nums[j] = abs(nums[j] - 1)
                #     first_zero= min(first_zero, j if nums[j] == 0 else first_zero)
                # i = first_zero
        return ops if ones == n else -1


def main():
    obj = Solution()
    nums = [0,1,1,0,1]
    Output: 4

    # Ts 2
    nums = [1,0,0,0]

    Output: 1
    print(obj.minOperations(nums))


if __name__ == "__main__":
    main()
