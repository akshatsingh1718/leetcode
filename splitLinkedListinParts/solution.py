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
    TC: O(n) [find len] + O(n) [split] ~ O(n)
    SC: O(k) [size of res]

    ==========================
    Algorithm:
    ==========================
    """

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        res = [None] * k
        if head is None:
            return res

        # find the length of the arr list
        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next

        # CASE: k > n: if k is greater than the length of the list then
        # each item will have only 1 list node
        b = 1
        extra_size = 0
        if k > n:
            b = 1
        else:
            b = n // k
            extra_size = n % k
        curr = head
        i = 0
        while i < k and curr is not None:
            temp_b = b
            if extra_size > 0:
                temp_b += 1
                extra_size -= 1
            temp_curr = curr
            prv = None
            while temp_curr is not None and temp_b > 0:
                prv = temp_curr
                temp_curr = temp_curr.next
                temp_b -= 1
            res[i] = curr
            prv.next = None
            curr = temp_curr

            i += 1

        return res


def main():
    obj = Solution()
    head = list_to_ll([1, 2, 3])
    k = 5
    expected = [[1], [2], [3], [], []]

    # TS 2
    head = list_to_ll([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

    # TS 3
    head = list_to_ll([1, 2, 3])
    k = 2
    print(obj.splitListToParts(head, k))


if __name__ == "__main__":
    main()
