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
    TC: O(2^n * n)
    SC: O(n) [seen set]

    ==========================
    Algorithm:
    ==========================
    """

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        max_count: int = 0

        def solve(i: int, seen: Set[str], curr: int) -> None:
            nonlocal max_count

            # prune a recursion call if we find out the
            # the curr count + all the next chars is still
            # less than or equal to the max so we cant make
            # another max for this branch
            if curr + n - i <= max_count:
                return None

            if i >= n:
                max_count = max(max_count, curr)
                return None

            for j in range(i, n):  # O(n)
                sub = s[i : j + 1]  # O(n)
                if sub not in seen:  # O(1)
                    seen.add(sub)  # add
                    solve(j + 1, seen, curr + 1)
                    seen.remove(sub)  # remove

        solve(0, set(), 0)
        return max_count


def main():
    obj = Solution()
    s = "ababccc"
    expected = 5

    # TS 2
    s = "aa"
    expected = 1

    # TS 3
    s = "aba"
    expected = 2

    # TS 4 (failed)
    s = "wwwzfvedwfvhsww"
    expected = 11
    print(obj.maxUniqueSplit(s))


if __name__ == "__main__":
    main()
