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
    TC: O(n^3)
    SC: O(n) [set]

    ==========================
    Algorithm:
    ==========================

    TLE
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        # create map
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                prod_a_b = nums[i] * nums[j]
                nums_set = set()
                for k in range(0, n):
                    if k in (i, j):
                        continue
                    d = prod_a_b / nums[k]
                    if d in nums_set:
                        # print(nums[i], nums[j], nums[k], d)
                        res += 1
                        # if i got the d num then i will not get any other d so break
                    if k > i:
                        nums_set.add(nums[k])

        return res * 8


def main():
    obj = Solution()
    nums = [2, 3, 4, 6]
    Output = 8

    # TS 2
    # nums = [1, 2, 4, 5, 10]
    # Output = 16

    # TS 3
    nums = [20, 10, 6, 24, 15, 5, 4, 30]
    output = 48
    print(obj.tupleSameProduct(nums))


if __name__ == "__main__":
    main()

"""
20 6 5 24.0
20 6 30 4.0
20 15 30 10.0
10 6 4 15.0
=> 10 15 30 5.0
10 30 15 20.0
24 5 6 20.0
24 5 30 4.0
15 4 6 10.0
=> 5 30 15 10.0
4 30 6 20.0
4 30 5 24.0
"""
