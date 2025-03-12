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
Problem: https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n = len(pattern)
    we need n+1 size permutation
    TC: O(9^n) [9 choices at each step and n depth will go]
    SC: O(n) [n stack space]

    ==========================
    Algorithm:
    ==========================
    """

    def smallestNumber(self, pattern: str) -> str:
        # Create all the permutations

        def find_smallest(
            curr_num: int, curr_pos: int, used_mask: int, pattern: str
        ) -> int:

            # Base case: Check if curr_pos > len(pattern)
            if len(pattern) < curr_pos:
                return curr_num

            # get the last digit we have
            last_digit = curr_num % 10

            # The next digit increase condition should be
            # 1. If the pos is 0 (not added any number yet)
            # 2. If the last pattern is saying to increase or I
            should_increase = (curr_pos == 0) or (pattern[curr_pos - 1] == "I")

            # take the res as inf since we want the smallest num or smallest lexographically
            res = float("inf")

            # Move from 1 - 9
            for nxt_digit in range(1, 10):
                # check if the digit is already visited meaning
                # check for the bit index in used mask is not 0
                # 0 means the slot is empty hence not visited
                if used_mask & (1 << nxt_digit) != 0:
                    continue

                # check if the next digit should increase or not
                # if we want to increase and nxt_digit is not increase then continue
                is_nxt_digit_inc = last_digit < nxt_digit
                if is_nxt_digit_inc != should_increase:
                    continue

                # we are all good to go and accept the nxt_digit
                res = min(
                    res,
                    find_smallest(
                        curr_num * 10 + nxt_digit,
                        curr_pos + 1,
                        used_mask | (1 << nxt_digit),
                        pattern,
                    ),
                )
            return res

        return str(find_smallest(0, 0, 0, pattern))


def main():
    obj = Solution()
    pattern = "IIIDIDDD"
    output = "123549876"
    print(obj.smallestNumber(pattern))


if __name__ == "__main__":
    main()
