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
Problem: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
Help: https://www.youtube.com/watch?v=o17MBWparrI
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n)
    SC: O(32) [first_seen can only have 32 values since we are dealing with vowels so the possible states cannot be more than 2^5]

    ==========================
    Algorithm:
    ==========================
    """

    def findTheLongestSubstring(self, s: str) -> int:

        mask = 0

        # vowels showing bits set in decimal
        vowels = {
            "a": 1,  # 00001
            "e": 2,  # 00010
            "i": 4,  # 00100
            "o": 8,  # 01000
            "u": 16,  # 10000
        }

        max_length = 0
        # We could have used all the alphabets and need to store 2**26 elements
        # To optimize further we can only store till u (which is at 21 position) thus needing only 2**21 elements
        # But further we could optimize since we only need vowels so 2**5 will be sufficient
        first_seen = [
            -1
        ] * 32  # Till b00000 (0) -> b11111 (31) we could have seen values

        for i, char in enumerate(s):
            # for consonants we will use 0 for xor which will not change the mask
            mask ^= vowels.get(char, 0)

            # seeing for the first time
            # or
            # if the mask is zero it means take the length from the starting and we
            # dont want to change it from idx = 0 since it will remain always -1 and should not change
            if first_seen[mask] != -1 or mask == 0:
                max_length = max(max_length, i - first_seen[mask])

            else:  # already seen
                first_seen[mask] = i
        return max_length


def main():
    obj = Solution()
    s = "eleetminicoworoep"
    expected = 13
    print(obj.findTheLongestSubstring(s))


if __name__ == "__main__":
    main()
