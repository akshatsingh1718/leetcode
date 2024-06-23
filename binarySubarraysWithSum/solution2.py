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
    SC: O(1)

    ==========================
    Algorithm: (sliding-window)
    ==========================
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        window_sum = 0
        result = 0
        zeros_count = 0

        while j < n:

            # increase the window sum
            window_sum += nums[j]

            # check for leading zeros till the next 1
            # if our window_sum == goal then this will
            # be helpful for how many subsets we can create
            # since removing 0's from the start of the subset
            # will change the subset but not the sum

            # And

            # This will move till j because our window is ending at j
            # There are two conditions till where this loop will run
            # 1. when window sum is greater than goal
            # 2. nums[i] is 0.

            while i < j and (window_sum > goal or nums[i] == 0):
                if nums[i] == 0:
                    zeros_count += 1
                else:
                    zeros_count = 0

                window_sum -= nums[i]
                i += 1

            # check if we got the goal
            if window_sum == goal:
                result += 1 + zeros_count
            #     print(f"{j=} {i=} {window_sum=} {zeros_count=} +1 ")
            # else:
            #     print(f"{j=} {i=} {window_sum=} {zeros_count=}")

            # increase window size
            j += 1

        return result



def main():
    obj = Solution()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    output = 4

    # TS 2
    nums = [0, 0, 0, 1, 0, 0, 1, 0, 1]
    goal = 2
    output = 0
    print(obj.numSubarraysWithSum(nums, goal))


if __name__ == "__main__":
    main()
