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
    1. Create a first_seen which will take care of when was the first time we saw the same mask first time. The mask act as a lookup dict for even odd occurrences of vowels. 0 means odd and 1 means even. We could have taken an array of 5 elements which will store the 0 or 1 for odd even but a bit will take lesser memory.

    2. vowels dict will tell us how many left shifts we need to make.

    3. Mask: It is just a table for telling vowels odd or even states.

    4. in code `if char in vowels` is because we need to only work with vowels.

    5. If the mask is already seen it means there is some occurrence already happened and removing it from the current mask will make the mask all zeros hence all even counts.
    """

    def findTheLongestSubstring(self, s: str) -> int:
        first_seen = dict()
        first_seen[0] = -1  # when all are seen even no of times or seen never
        mask = 0

        vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        max_length = 0

        for i, char in enumerate(s):

            if char in vowels:
                mask ^= 1 << vowels[char]

            # if already seen
            if mask in first_seen:
                max_length = max(max_length, i - first_seen[mask])
            # if the mask is seen for the first time
            else:
                first_seen[mask] = i
                # why are we not taking max_length here ?
                # Because these first timers are all the binary nums containing atleast 1
                # set bit and cannot be taken as a candidate for even vowels which are all zeros
        return max_length


def main():
    obj = Solution()
    s = "eleetminicoworoep"
    expected = 13
    print(obj.findTheLongestSubstring(s))


if __name__ == "__main__":
    main()
