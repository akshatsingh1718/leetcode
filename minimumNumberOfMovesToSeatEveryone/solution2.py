from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil

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
Problem: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/submissions/1286845557/?envType=daily-question&envId=2024-06-13
Help: https://www.youtube.com/watch?v=sU-yjrJTnYs
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) + O(n) + O(n) ~ O(n)
    SC: O(n) + O(n) ~ O(n)

    ==========================
    Algorithm: (counting-sort)
    ==========================
    """

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # find max from students and seats
        k = max(max(students), max(seats))

        # from 0 -> k seats places where seat may or may not present
        sorted_seats = [0] * (k + 1)
        # from 0 -> k students places where student may or may not present
        sorted_students = [0] * (k + 1)

        # set how many seats preset at certain place
        for st in seats:
            sorted_seats[st] += 1

        # set how many students preset at certain place
        for st in students:
            sorted_students[st] += 1

        i, j = 0, 0
        moves = 0
        # move till we reach at k
        while i <= k and j <= k:

            # move till where at least a single student is present
            while i <= k and sorted_students[i] == 0:
                i += 1
            # move till where at least a single seat is present
            while j <= k and sorted_seats[j] == 0:
                j += 1

            # if the student idx and seat present is in our allowed space
            # then we got a seat for a student
            if i <= k and j <= k:
                moves += abs(i - j)
                # decrement the count of student and seat for certain place
                sorted_students[i] -= 1
                sorted_seats[j] -= 1

        return moves


def main():
    obj = Solution()
    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    output = 4
    print(obj.minMovesToSeat(seats, students))


if __name__ == "__main__":
    main()
