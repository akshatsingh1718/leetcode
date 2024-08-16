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
    (TLE)
    n arrays
    n2 avg len of a single arr
    TC: O(n * n2) [min max] + O(n^2)
    SC: O(n)

    ==========================
    Algorithm:
    ==========================
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_dis = float("-inf")
        n = len(arrays)

        temp_min = arrays[0][0]
        temp_max = arrays[0][-1]

        # find max and min number pairs
        for i in range(1, n):
            arr = arrays[i]
            curr_min, curr_max = arr[0], arr[-1]

            max_dis = max(max_dis, abs(curr_min - temp_max), abs(curr_max - temp_min))
            # update the new max and min
            temp_max = max(temp_max, curr_max)
            temp_min = min(temp_min, curr_min)
        return max_dis


def main():
    obj = Solution()
    arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
    expected = 4
    # TS 2
    arrays = [[1, 4], [0, 5]]
    expected = 4
    print(obj.maxDistance(arrays))


if __name__ == "__main__":
    main()
