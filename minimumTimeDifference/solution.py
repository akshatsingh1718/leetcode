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
    TC: O(n) [convert to int] + O(nlogn) [sorting] + O(n) [find min]
    SC: O(n) [new_time_points]

    ==========================
    Algorithm:
    ==========================
    """

    def findMinDifference(self, timePoints: List[str]) -> int:

        new_time_points = []

        def str_time_to_int_time(time):
            hr, mins = time.split(":")
            hr = int(hr)
            mins = int(mins)
            if hr == 0:
                hr = 24
            return (hr, mins)

        def get_time_diff(t1: Tuple[int, int], t2: Tuple[int, int]):
            t2_hr, t2_min = t2
            t1_hr, t1_min = t1
            return (t1_hr - t2_hr) * 60 + (t1_min - t2_min)

        for time in timePoints:
            new_time_points.append(str_time_to_int_time(time))

        min_diff: int = float("inf")
        new_time_points.sort()

        for i in range(1, len(new_time_points)):
            min_diff = min(
                min_diff,
                get_time_diff(t1=new_time_points[i], t2=new_time_points[i - 1]),
            )

        # for last and first time difference
        min_diff = min(
            min_diff,
            24 * 60 - get_time_diff(t1=new_time_points[-1], t2=new_time_points[0]),
        )

        return min_diff


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
