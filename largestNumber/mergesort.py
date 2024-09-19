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
    TC: O(nlogn)
    SC: O(log n) [recursion depth]

    ==========================
    Algorithm:
    ==========================
    """

    def _mergesort(self, left: int, right: int, nums: List[int]) -> List[int]:
        # single number is already sorted
        if left >= right:
            return [nums[left]]

        mid = left + (right - left) // 2

        # get the left and right halves
        left_nums = self._mergesort(left, mid, nums)
        right_nums = self._mergesort(mid + 1, right, nums)

        return self._merge(left_nums, right_nums)

    def _merge(self, left_half: List[int], right_half: List[int]) -> List[int]:

        res = []

        left_i = 0
        right_i = 0

        while left_i < len(left_half) and right_i < len(right_half):
            left_n = left_half[left_i]
            right_n = right_half[right_i]
            if f"{left_n}{right_n}" > f"{right_n}{left_n}":
                res.append(left_n)
                left_i += 1
            else:
                res.append(right_n)
                right_i += 1

        # extend the remaining nums from left_half
        res.extend(left_half[left_i:])

        res.extend(right_half[right_i:])

        return res

    def largestNumber(self, nums: List[int]) -> str:
        res = self._mergesort(0, len(nums) - 1, nums)
        res = "".join(map(str, res))
        if res[0] == "0":
            return "0"
        return res


def main():
    obj = Solution()
    nums = [3, 30, 34, 5, 9]
    expected = "9534330"

    # TS 2
    # nums = [10, 2]
    # expected = "210"
    print(obj.largestNumber(nums))


if __name__ == "__main__":
    main()
