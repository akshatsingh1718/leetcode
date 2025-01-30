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
Problem: https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def findTwoElement(self, arr):
        n = len(arr)

        def xor(nums: List[int], start: int, end: int):
            x = 0
            for i in range(start, end):
                x ^= nums[i]
            return x

        xor_res = xor(arr, 0, n) ^ xor(list(range(n + 1)), 0, n + 1)

        # find the differentiating bit
        i = 0
        while i < 32:
            if xor_res & (1 << i) > 0:
                break
            i += 1

        # Now make two batches of 0 and 1 for the ith bit
        zero_bits = 0
        one_bits = 0

        for j in range(n):

            # i + 1 is the num from 1 - > n
            # num[i] is the current num we are given

            if (j + 1) & (1 << i) > 0:
                one_bits ^= j + 1
            else:
                zero_bits ^= j + 1

            if arr[j] & (1 << i) > 0:
                one_bits ^= arr[j]
            else:
                zero_bits ^= arr[j]

        if one_bits in arr:
            return [one_bits, zero_bits]
        return [zero_bits, one_bits]


def main():
    obj = Solution()
    arr = [4, 3, 6, 2, 1, 1]
    print(obj.findTwoElement(arr))


if __name__ == "__main__":
    main()
