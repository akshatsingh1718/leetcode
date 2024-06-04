from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache

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
Problem: https://leetcode.com/problems/get-equal-substrings-within-budget/solutions/5218554/sliding-window-vs-prefix-sum-binary-search-0ms-beats-100/?envType=daily-question&envId=2024-05-28
Help: https://www.youtube.com/watch?v=MF2MgJQuFhA
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2*n) [since our i and j pointer is only visiting each element one time]
    SC: O(1)

    ==========================
    Algorithm: (sliding window)
    ==========================
    """

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0

        diff = lambda a, b: abs(ord(a) - ord(b))
        n = len(s)
        i = 0
        j = 0

        cost = 0

        while i <= j < n:
            cost += diff(s[j], t[j])

            while i < n and cost > maxCost:
                cost -= diff(s[i], t[i])
                i += 1

            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length



class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2*n) [since our i and j pointer is only visiting each element one time]
    SC: O(1)

    ==========================
    Algorithm: (sliding window)
    ==========================
    """

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0

        diff = lambda a, b: abs(ord(a) - ord(b))
        n = len(s)
        i = 0
        j = 0

        cost = 0

        while i <= j < n:
            cost += diff(s[j], t[j]) 

            if cost > maxCost:
                cost -= diff(s[i], t[i])
                i += 1

            max_length = max(max_length, j - i + 1)
            j += 1

        return max_length


def main():
    obj = Solution()
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    output = 3

    # TS 2
    # s = "abcd"
    # t = "cdef"
    # maxCost = 3
    # output= 1

    # TS 3
    s = "a"
    t = "a"
    maxCost = 1
    print(obj.equalSubstring(s, t, maxCost))


if __name__ == "__main__":
    main()
