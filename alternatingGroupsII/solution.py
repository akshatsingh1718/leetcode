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

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # extend the colors to avoid % operation for circular traversal
        colors += colors[: k - 1]

        n = len(colors)

        # create equal and not equal
        next_not_equal = []
        for i in range(n):  # traversal on all colors + additional k colors for start
            if i != n - 1:
                next_not_equal.append(0 if colors[i] != colors[i + 1] else 1)
            else:
                next_not_equal.append(0)

            if i > 0 and i < n - 1:
                # along the way find the cumulative sum as well
                next_not_equal[i] += next_not_equal[i - 1]

        next_not_equal[n - 1] += next_not_equal[n - 2]
        print(colors)
        print(next_not_equal)
        # find the alternating groups
        groups = 0
        for start in range(n - k + 1):
            end = start + k - 1
            if next_not_equal[end] - next_not_equal[start + 1] == 0:
                print(f"{start=} ; end={end -1}")
                groups += 1

        return groups


def main():
    obj = Solution()
    colors = [0, 1, 0, 1, 0]
    k = 3
    expected = 3
    # TS 2
    colors = [0, 1, 0, 0, 1, 0, 1]
    k = 6
    expected = 2
    print(obj.numberOfAlternatingGroups(colors, k))


if __name__ == "__main__":
    main()
