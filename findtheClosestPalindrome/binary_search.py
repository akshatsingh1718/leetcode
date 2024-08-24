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
    half_len (h) = len(n) // 2
    TC: O(n log(m))
    SC: O(n) [convert created list of string]

    ==========================
    Algorithm:
    ==========================
    1. find the next palindrome of n.
    2. find the prv palindrome of n.
    3. compare both of them
    """

    def convert(self, num: int):
        s_list = list(str(num))  # O(n) space
        n = len(s_list)
        l = (n - 1) // 2
        r = n // 2
        while l >= 0:
            s_list[r] = s_list[l]
            l -= 1
            r += 1

        return int("".join(s_list))

    def prv_palindrome(self, num: int):
        left = 0
        right = num
        res = float("inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin < num:
                res = palin
                left = mid + 1

            else:
                right = mid - 1
        return res

    def next_palindrome(self, num: int):
        left = num
        right = int(1e18)

        res = float("-inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin > num:
                res = palin
                right = mid - 1
            else:
                left = mid + 1
        return res

    def nearestPalindromic(self, n: str) -> str:
        n_int = int(n)
        next_p = self.next_palindrome(n_int)
        prv_p = self.prv_palindrome(n_int)

        if n_int - prv_p > next_p - n_int:
            return str(next_p)
        return str(prv_p)


def main():
    obj = Solution()
    n = "123"
    expected = "121"

    # TS 2
    # n = "1"
    # expected = "0"

    # TS 3
    n = "1213"
    expected = "1221"

    print(obj.nearestPalindromic(n))


if __name__ == "__main__":
    main()
