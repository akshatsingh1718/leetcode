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
Problem: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=daily-question&envId=2024-10-13
Help: https://www.youtube.com/watch?v=L_0aPFMgGpU
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(k) [k_heap] + O(k) [max] + O(n * logk)
    SC: O(k) [heap]

    ==========================
    Algorithm:
    ==========================
    """

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        k_heap = [(nums[i][0], i, 0) for i in range(k)]
        heapify(k_heap)
        # print(k_heap)

        largest_element = max(nums)[0]

        min_range = float("inf")
        _range = [float("inf"), float("inf")]

        while True:
            # get the smallest till now and increase it
            smallest_element, list_index, curr_item_index = heappop(k_heap)
            # print()
            # print(
            #     f"{largest_element=} {smallest_element=} diff={largest_element - smallest_element}"
            # )

            # If the new range is smaller than the min_range then simply update the new min range
            if largest_element - smallest_element < min_range:
                min_range = largest_element - smallest_element
                _range = [smallest_element, largest_element]
            # if range is equal then check for the smallest no amongst both
            elif (
                largest_element - smallest_element == min_range
                and smallest_element < _range[0]
            ):
                min_range = largest_element - smallest_element
                _range = [smallest_element, largest_element]

            next_item_index = curr_item_index + 1
            if next_item_index == len(nums[list_index]):
                return _range
            next_item = nums[list_index][next_item_index]

            # find largest element
            largest_element = max(largest_element, next_item)
            # add the item to the heap
            heappush(k_heap, (next_item, list_index, next_item_index))
            # print(k_heap)


def main():
    obj = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    expected = [20, 24]
    print(obj.smallestRange(nums))


if __name__ == "__main__":
    main()
