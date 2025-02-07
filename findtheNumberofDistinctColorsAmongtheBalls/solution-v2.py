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
Problem: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n = len(queries)
    TC: O(n)
    SC: O(m + 1) [dict] + O(n) [balls_color]

    ==========================
    Algorithm:
    ==========================
    (Memory error) Since limit <= 10^9 and we need to do it in 10^5
    """

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_color = [0] * (limit + 1)
        color_count = defaultdict(int)
        res = []

        for idx, color in queries:

            if balls_color[idx] == 0:  # first time color change
                color_count[color] += 1
                balls_color[idx] = color
            elif (
                balls_color[idx] != color
            ):  # color is already changed and new color should not be same as prv color
                # save the old color
                old_color = balls_color[idx]
                # decrement the count of the prv color
                color_count[old_color] -= 1

                # remove color if its count is 0
                if color_count[old_color] == 0:
                    del color_count[old_color]

                # add the new color
                color_count[color] += 1

                # change the color
                balls_color[idx] = color

            res.append(len(color_count))

        return res


def main():
    obj = Solution()
    limit = 4
    queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
    output = [1, 2, 2, 3]

    # TS 2
    queries = [[0, 1], [0, 4], [0, 4], [0, 1], [1, 2]]
    limit = 1
    print(obj.queryResults(limit, queries))


if __name__ == "__main__":
    main()
