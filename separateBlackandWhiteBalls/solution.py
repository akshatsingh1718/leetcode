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
Problem: https://leetcode.com/problems/separate-black-and-white-balls/?envType=daily-question&envId=2024-10-15
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n)
    SC: O(1)

    ==========================
    Algorithm: `2-ptr`
    ==========================
    Move one_idx from starting idx = 0 to find all the ones indexes
    Then move zero_idx from ending idx = n - 1 to find all the zero indexes
    At this stage we have the index for zero (from ending) and one (from starting)
    Assuming we swap the current indices as question only wants the no of swaps and not the inplace swapping of the ones
    Calculating the indexes will take place using `zero_idx - one_index`.
    If the one_idx passes the zero_index we can break the loop
    """

    def minimumSteps(self, s: str) -> int:
        n = len(s)
        one_idx = 0
        zero_idx = n - 1

        steps = 0
        while one_idx < zero_idx and one_idx < n:
            # find one_idx from left to right
            while one_idx < zero_idx and one_idx < n and s[one_idx] != "1":
                one_idx += 1

            # find zero_idx from right to left
            while one_idx < zero_idx and s[zero_idx] != "0":
                zero_idx -= 1

            # swap
            # s[one_idx], s[zero_idx] = s[zero_idx], s[one_idx]
            steps += zero_idx - one_idx

            one_idx += 1
            zero_idx -= 1
        return steps


def main():
    obj = Solution()
    s = "101"
    expected = 1

    # # Ts 2
    s = "100"
    expected = 2

    # # TS 3
    s = "0111"
    expected = 0
    print(obj.minimumSteps(s))


if __name__ == "__main__":
    main()
