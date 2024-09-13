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
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    if head1 is not head2:
        return False

    return True


def printList(head: Optional[ListNode]):
    lstr: str = ""
    if head is None:
        return lstr
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
    m = len of queries
    n = len of arr
    TC: O(n) [prefix xor] + O(m) [queries] = O(m + n)
    SC: O(n) [prefix xor]

    ==========================
    Algorithm:
    ==========================
    Prefix xor
    """

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # calculate prefix xor
        prefix_xor = []
        xor = 0
        # This can also be change to inplace xor by
        # using arr for prefix xor values
        for num in arr:
            xor = xor ^ num
            prefix_xor.append(xor)

        res = []

        for start, end in queries:
            xor = prefix_xor[end]
            if start > 0:
                xor ^= prefix_xor[start - 1]
            res.append(xor)

        return res


def main():
    obj = Solution()
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    expected = [2, 7, 14, 8]
    print(obj.xorQueries(arr, queries))


if __name__ == "__main__":
    main()
