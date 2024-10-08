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
    TC: O(n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    (Change the stack to open_brackets count)
    1. If char is "[" then append directly.
    2. If char is "]" and stack is empty then it means there is no bracket to balance it. In this case increment the unbalanced by 1 and do not append "]" to the stack since it will not contribute to any case.
    3. If char is "]" and stack is non empty then pop the top element since a pair has been made and non empty means we have "[" opening bracket for sure because stack only contains opening brackets.
    4. return (unbalanced + 1)//2 since one swapping will get rid of 2 unmatched brackets and + 1 is just for odd number.
    """

    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        open_brackets = 0

        for char in s:
            if char == "[":
                open_brackets += 1
            elif char == "]" and open_brackets > 0:
                open_brackets -= 1
            elif char == "]" and open_brackets == 0:
                # increment unbalanced
                # do not append this to the stack since it will not contribute to any case
                unbalanced += 1
        return (unbalanced + 1) // 2


def main():
    obj = Solution()
    s = "][]["
    expected = 1

    # TS 2
    s = "]]][[["
    expected = 2
    print(obj.minSwaps(s))


if __name__ == "__main__":
    main()
