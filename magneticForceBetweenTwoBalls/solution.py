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
Problem: https://leetcode.com/problems/magnetic-force-between-two-balls/submissions/1294422461/?envType=daily-question&envId=2024-06-20
Help: https://www.youtube.com/watch?v=CSXkcvH8V-c&t=682s
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) [sort] + O(logn * n) [bs * can_fit] ~ O(n logn) or (n lon(position[-1] - position[0]) )
    SC: O(n) [tim sort]

    ==========================
    Algorithm: (bs-on-answer)
    ==========================
    1. sort the positions.
    2. create a low and high for lowest and highest max force which we can achieve. low is 1 for the case where we have n adj positions and n balls. High is for the highest max force where we have only 2 balls for n positions.
    3. Start the binary search and calculate the mid and check if mid distance can fit m balls on n positions with greater or equal distance than calculated mid distance.
    4. Update the max_distance we achieved by increasing the low since increasing the low will increase the max distance.
    """

    def maxDistance(self, position: List[int], m: int) -> int:

        def can_fit(distance: int):  # TC: O(n)
            nonlocal position, m
            n = len(position)
            i = 1
            last_pos = 0
            balls_placed = 1
            while i < n:
                if abs(position[last_pos] - position[i]) >= distance:
                    balls_placed += 1
                    last_pos = i
                if balls_placed == m:
                    break
                i += 1
            return balls_placed == m

        # try out different max distance using binary search
        position.sort()
        low = 1  # set the lowest magnetic force
        high = position[-1] - position[0]  # set the largest magnetic force
        max_distance = 1

        while low <= high:
            mid = low + (high - low) // 2  # mid force to check for distance

            if can_fit(distance=mid):
                max_distance = mid
                low = mid + 1
            else:
                high = mid - 1

        return max_distance


def main():
    obj = Solution()
    position = [1, 2, 3, 4, 7]
    m = 3
    output = 3

    # TS 2
    # position = [5, 4, 3, 2, 1, 1000000000]
    # m = 2
    # output = 999999999

    # TS #
    # position = [1,2,3,4,5,6,7,8,9,10]
    # m = 4
    # output = 3
    print(obj.maxDistance(position, m))


if __name__ == "__main__":
    main()
