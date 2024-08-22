from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
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
    TC: O(n) [remove dups] +  O(n) [for each index k] * O(n * (n+1) / 2) [substrings] ~ O(n^3)
    SC: O(n^2) [memo]

    ==========================
    Algorithm:
    ==========================
    """

    def strangePrinter(self, s: str) -> int:
        # remove consecutive characters to make problem input simples
        # "aabbca" -> "abca"
        new_s = "".join(char for char, _ in it.groupby(s))
        n = len(new_s)
        memo = [([-1] * n) for _ in range(n)]

        # helper to find the min no of printers needed between start -> end
        def find_min_prints(start: int, end: int):
            nonlocal new_s, memo
            if start > end:
                return 0

            if memo[start][end] != -1:
                return memo[start][end]

            # set the worst case scenario where we are assuming all the
            # characters are printed separately
            min_prints = 1 + find_min_prints(start + 1, end)

            # find out if there is a kth index that is same as start index
            for k in range(start + 1, end + 1):
                if new_s[start] == new_s[k]:  # found the match
                    min_prints_with_match = find_min_prints(
                        start, k - 1
                    ) + find_min_prints(k + 1, end)

                    min_prints = min(min_prints, min_prints_with_match)

            memo[start][end] = min_prints
            return min_prints

        return find_min_prints(start=0, end=n - 1)


def main():
    obj = Solution()
    s = "aaabbb"
    expected = 2
    print(obj.strangePrinter(s))


if __name__ == "__main__":
    main()
