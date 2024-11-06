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
    TC: O(n) [loop]
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        min_of_segment = nums[0]
        max_of_segment = nums[0]
        no_of_bits = nums[0].bit_count()

        max_of_prv_segment = float("-inf")

        for i in range(1, n):
            # if the ith num is falling under the same no_of_bits segment
            # then just update the min and max if needed
            if nums[i].bit_count() == no_of_bits:
                min_of_segment = min(min_of_segment, nums[i])
                max_of_segment = max(max_of_segment, nums[i])
                continue

            # Start new segment

            # but before check if the curr segment min no is
            # smaller than max of prv segment then it means
            # sorting cannot be performed since the larger from the last
            # segment should be present after the min of curr segment and this
            # cannot be done because of change in no of set bits
            if min_of_segment < max_of_prv_segment:
                return False

            max_of_prv_segment = max_of_segment

            max_of_segment = nums[i]
            min_of_segment = nums[i]
            no_of_bits = nums[i].bit_count()

        # check for last segment if its min is smaller
        # than its prv max segment no
        return min_of_segment > max_of_prv_segment


def main():
    obj = Solution()
    nums = [8, 4, 2, 30, 15]
    expected = True

    # TS 2
    # nums = [3, 16, 8, 4, 2]
    # expected = False
    print(obj.canSortArray(nums))


if __name__ == "__main__":
    main()
