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
    Algorithm:
    ==========================
    """

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # iterate over all the customer and check for the max customer which
        # are unsatisfied within a window
        max_unsatisfied = 0
        satisfied = 0
        n = len(customers)

        # find the max unsatisfied customers for 1st window
        for i in range(minutes):  # TC: O(n)
            max_unsatisfied += customers[i] * grumpy[i]

            # also find out the total already satisfied customers for the 1st window
            # abs(grumpy[i] - 1) is to make 0 a 1 and vice versa.
            satisfied += customers[i] * abs(grumpy[i] - 1)

        # i will take care of removing last minute data from the prv unsatisfied window
        i = 0
        # j will take care of adding new minute data to prv unsatisfied window
        j = minutes
        # keep track of prv unsatisfied window
        prv_window_unsatisfied = max_unsatisfied
        while i < j < n:  # TC: O(n)
            # along the way add up the satisfied customers
            satisfied += customers[j] * abs(grumpy[j] - 1)

            # remove the i the minute customers from the unsatisfied
            # and add the jth minute customers from the unsatisfied
            next_window_unsatisfied = (
                prv_window_unsatisfied
                + (customers[j] * grumpy[j])
                - (customers[i] * grumpy[i])
            )
            max_unsatisfied = max(max_unsatisfied, next_window_unsatisfied)
            prv_window_unsatisfied = next_window_unsatisfied

            i += 1
            j += 1

        return max_unsatisfied + satisfied


def main():
    obj = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    output = 16
    print(obj.maxSatisfied(customers, grumpy, minutes))


if __name__ == "__main__":
    main()
