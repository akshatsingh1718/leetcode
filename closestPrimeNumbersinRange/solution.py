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
Problem: https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(R-L * sqrt(L))
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def closestPrimes(self, left: int, right: int) -> List[int]:

        def is_prime(num: int):
            if num <= 1:
                return False
            elif num <= 3:
                return True

            # check if mod by 2 and 3
            if num % 2 == 0 or num % 3 == 0:
                return False

            # Any integer can be written in one of these forms: 
            # 6k,6k+1,6k+2,6k+3,6k+4,6k+5 
            for i in range(5, int(num**0.5) + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    return False

            return True

        last_prime_found = -1
        min_dist = float("inf")
        res = [-1, -1]

        for i in range(left, right + 1):
            if not is_prime(i):
                continue
            if last_prime_found > 0 and min_dist > i - last_prime_found:
                res = [last_prime_found, i]
                min_dist = i - last_prime_found
            last_prime_found = i

        return res


def main():
    obj = Solution()
    left = 10
    right = 19
    Output = [11, 13]

    # TS 2
    # left = 4
    # right = 6
    # Output = [-1, -1]
    print(obj.closestPrimes(left, right))


if __name__ == "__main__":
    main()
