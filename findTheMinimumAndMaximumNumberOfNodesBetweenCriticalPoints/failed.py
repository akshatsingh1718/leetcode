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

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        critical_min = [float("-inf"), float("inf")]  # [max, min]
        critical_max = [float("-inf"), float("inf")]
        idx = 1

        prv = None
        while head is not None:
            if prv is not None and head.next is not None:
                if prv.val < head.val and head.next.val < head.val:
                    critical_max[0] = max(idx, critical_max[0])
                    critical_max[1] = min(idx, critical_max[1])
                if prv.val > head.val and head.next.val > head.val:
                    critical_min[0] = max(critical_min[0], idx)
                    critical_min[1] = min(critical_min[1], idx)

            idx += 1
            prv = head
            head = head.next
        # print(critical_max)
        # print(critical_min)
        # # [minDistance, maxDistance]
        # print(float("inf") in critical_max, float("inf") in critical_max)
        if float("inf") in critical_max or float("inf") in critical_min:
            return [-1, -1]

        critical_points = []
        print(critical_min)
        print(critical_max)
        for num in [*critical_min, *critical_max]:
            if num not in [float("inf"), float("-inf")]:
                critical_points.append(num)
        largest2 = heapq.nlargest(2, critical_points)
        minDistance = largest2[0] - largest2[1]
        maxDistance = abs(max(critical_points) - min(critical_points))
        return [minDistance, maxDistance]


def main():
    obj = Solution()
    head = list_to_ll([5, 3, 1, 2, 5, 1, 2])
    head = list_to_ll([2, 2, 1, 3])
    expected = [1, 3]
    print(obj.nodesBetweenCriticalPoints(head))


if __name__ == "__main__":
    main()
