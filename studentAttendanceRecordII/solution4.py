from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache

import sys

# Check the current recursion limit
current_limit = sys.getrecursionlimit()
print(f"Current recursion limit: {current_limit}")

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
def create_adjacency_list(edges: List[tuple]):
    adjacency_list = {}

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
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
    TC: O(3^n) [3 possibilities at each stage]
    SC: O(n) [stack space]
    ==========================
    Algorithm: (Bottom up)
    ==========================
    """

    def checkRecord(self, n: int) -> int:
        # store the possible values at each stage of recursion like
        # (N, A, L)
        # N = length = n + 1
        # A = absent possible values = 2
        # L = late possible values = 3

        memo = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        print(memo)
        M = 1e9 + 7
        # base case
        for A in range(2):
            for L in range(3):
                print(A, L)
                memo[0][A][L] = 1

        # find other stages value
        for i in range(1, n + 1):
            for A in range(2):
                for L in range(3):
                    # Case: When student is present
                    res = memo[i - 1][A][L]
                    # Case: When student is absent
                    res += memo[i - 1][A + 1][0] if (A + 1 <= 1) else 0
                    # Case: When student is late
                    res += memo[i - 1][A][L + 1] if (L + 1 <= 2) else 0
                    memo[i][A][L] = res % M

        return memo[n][0][0]


def main():
    obj = Solution()
    n = 1
    # TS 2
    # n = 10101
    # output = 183236316
    print(Solution().checkRecord(n))

if __name__ == "__main__":
    main()
