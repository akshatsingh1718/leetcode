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
Problem: https://leetcode.com/problems/house-robber-iv/?envType=daily-question&envId=2025-03-15
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(Log max(nums) * n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def minCapability(self, nums: List[int], k: int) -> int:

        def ispossible(capability: int):
            nonlocal k
            houses_robbed = 0

            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    houses_robbed += 1
                    i += 1
                i += 1
            return houses_robbed >= k

        low = min(nums)
        high = max(nums)
        res = high
        while low <= high:  # TC: Log( max (nums))

            mid = low + (high - low) // 2

            # check if we can create a robbing pattern using max of mid (capability)
            if ispossible(mid):  # TC: O(n)
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res


def main():
    obj = Solution()
    nums = [2, 3, 5, 9]
    k = 2
    Output = 5
    print(obj.minCapability(nums, k))


if __name__ == "__main__":
    main()
