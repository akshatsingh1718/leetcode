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
Problem: https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13
Help: https://www.youtube.com/watch?v=8xHewtmPULs
https://www.youtube.com/watch?v=ZHNVmtm08WY
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O( LogQ * (Q + N) )
    SC: O(N)

    ==========================
    Algorithm:
    ==========================
    """

    def if_all_zeros(self, nums: List[int]) -> bool:
        for num in nums:
            if num != 0:
                return False
        return True

    def checkWithDifferenceArrayTechnique(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        difference_array = [0] * len(nums)

        # fill values in difference array
        for i in range(k + 1):  # TC: O(Q)
            l, r, atmost = queries[i]
            difference_array[l] += atmost
            if r + 1 < len(nums):
                difference_array[r + 1] -= atmost

        # find the cumulative array and check if its values is same as
        # nums or not
        last_val = 0
        for i in range(len(nums)):  # TC: O(N)
            last_val += difference_array[i]
            # make the i'th val cumulative
            difference_array[i] = last_val
            if nums[i] - difference_array[i] > 0:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        Q = len(queries)

        # check if already nums is zeros vec
        if self.if_all_zeros(nums):
            return 0

        low = 0
        high = Q - 1
        res = -1
        while low <= high:  # TC: O(Log Q)
            # TC: O(Q + N)
            k = low + (high - low) // 2
            if self.checkWithDifferenceArrayTechnique(nums, queries, k):
                res = k + 1
                # we got the ans but lets shrink our k val to check if there is
                # another smaller res
                high = k - 1
            else:
                low = k + 1

        return res


def main():
    obj = Solution()
    nums = [2, 0, 2]
    queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    Output = 2
    print(obj.minZeroArray(nums, queries))


if __name__ == "__main__":
    main()
