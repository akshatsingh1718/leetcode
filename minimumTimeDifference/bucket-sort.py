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
    TC: O(n) [fill minutes] + O(60*24) [min difference] ~ O(n)
    SC: O(60 * 24) ~ O(1440)

    ==========================
    Algorithm: `bucket-sort`
    ==========================
    1. Fill the minutes bucket.
    2. Calculate the differences between adjacent minutes.

    """

    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = [False] * (60 * 24)
        # Mark true for time values we have
        for time in timePoints:
            hr, mins = map(int, time.split(":"))
            mins_time = hr * 60 + mins

            # if time already exists then min time will be 0
            if minutes[mins_time]:
                return 0

            minutes[mins_time] = True

        # find out the min time
        first_time = prv_time = last_time = min_time = float("inf")

        for t in range(24 * 60):
            if not minutes[t]:
                continue

            if prv_time != float("inf"):
                min_time = min(min_time, t - prv_time)

            if first_time == float("inf"):
                first_time = t

            prv_time = t
            last_time = t

        # This will remove the last index which is the largest time we have from the total time
        # and then we add the first time the smallest time to the result to get the total time
        min_time = min(min_time, 24 * 60 - last_time + first_time)
        return min_time


def main():
    obj = Solution()
    timePoints = ["23:59", "00:00"]
    expected = 1

    # TS 2
    # timePoints = ["00:00", "23:59", "00:00"]
    # expected = 0

    # TS 3
    timePoints = ["12:12", "00:13"]
    expected = 719

    # TS 4
    timePoints = ["01:01", "02:02"]
    expected = 61
    print(obj.findMinDifference(timePoints))


if __name__ == "__main__":
    main()
