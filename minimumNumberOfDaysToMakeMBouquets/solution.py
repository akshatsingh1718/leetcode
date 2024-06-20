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

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def can_find_m_adj_bouquet_2(day: int):
            nonlocal bloomDay, m, k
            n = len(bloomDay)

            i = 0
            total_groups = 0
            while i < n:
                group_size = 0

                while i < n and bloomDay[i] <= day:
                    group_size += 1
                    i += 1

                if group_size // k > 0:  # group created
                    total_groups += group_size // k

                # This i will have a value which is not bloomed
                # so we increase it by 1 to check for the next pass
                # whether it can make a bouquet or not
                i += 1

            return total_groups >= m

        def can_find_m_adj_bouquet(day: int):
            nonlocal bloomDay, m, k
            n = len(bloomDay)
            i = 0
            total_groups = 0
            consecutive_count = 0

            while i < n:
                if bloomDay[i] <= day:
                    consecutive_count += 1
                else:
                    consecutive_count = 0

                if consecutive_count == k:
                    total_groups += 1
                    consecutive_count = 0

                i += 1

            return total_groups >= m

        # start binary search from day 1 -> max bloom day
        # and check the lowest day we can find all the m bloom
        # with k adjacent blooms

        min_days = -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = low + (high - low) // 2

            if can_find_m_adj_bouquet(mid):
                min_days = mid
                high = (
                    mid - 1
                )  # go lower and check if there is some other min day as well to bloom
            else:
                low = mid + 1

        return min_days


def main():
    obj = Solution()
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    output = 3
    print(obj.minDays(bloomDay, m, k))


if __name__ == "__main__":
    main()
