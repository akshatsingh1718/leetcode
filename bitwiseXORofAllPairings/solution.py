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
Problem: https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
Help: https://www.youtube.com/watch?v=19-Q_Krxj1w
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n1 = len(nums1)
    n2 = len(nums2)
    n3 = len(freq)

    TC: O(n1 + n2) + O(n3)
    SC: O(n3)

    ==========================
    Algorithm:
    ==========================
    """

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # find the freq of each elements and store in freq table
        # skip all the even occurrences as they will collapse to 0
        # for xor operation and take only a single count of odd # freq nums

        freq = defaultdict(int)
        n1 = len(nums1)
        n2 = len(nums2)

        for n in nums1:
            freq[n] += n2 
        for n in nums2:
            freq[n] += n1

        res = 0
        for num, occr in freq.items():
            if occr % 2 == 0:  # skip even counts
                continue

            res ^= num

        return res


def main():
    obj = Solution()
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    expected = 13
    print(obj.xorAllNums(nums1, nums2))


if __name__ == "__main__":
    main()
