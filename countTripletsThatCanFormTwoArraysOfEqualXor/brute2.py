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
Problem: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n^3) [3 for loops] * n (for xor values) ~ O(n^4)
    SC:

    ==========================
    Algorithm: (brute force)
    ==========================
    """

    def countTriplets(self, arr: List[int]) -> int:

        triplets = 0

        def xor(start, end):
            nonlocal arr, n
            res = 0
            for i in range(start, end):
                res ^= arr[i]
            return res

        n = len(arr)
        for i in range(n):
            a = xor(start=i, end=j)  # excluding j so j-1
            
            for j in range(i + 1, n):
                b = 0

                # for k in range(j, n):

                b ^= arr[]

                # find the xor
                if a == b:
                    triplets += 1

        return triplets


def main():
    obj = Solution()
    arr = [2, 3, 1, 6, 7]
    output = 4

    arr = [1, 1, 1, 1, 1]
    output = 10

    print(obj.countTriplets(arr))


if __name__ == "__main__":
    main()
