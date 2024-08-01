from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
import heapq
from heapq import heapify, heappop, heappush

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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # meme = [ [area of shelf can be used] * for every books]
        # Here meme is only holding area of shelf can be used and total no of books since
        # at max/worst every book can have separate shelf and every shelf can have atmost shelfWidth space
        # height can be derived from at what shelf we at with remaining shelf width.
        # height is also the answer we are storing in memo
        memo = [[-1 for _ in range(shelfWidth + 1)] for _ in range(n)]

        def find_min_height(i: int, remaining_shelf: int, maxHeight: int):
            nonlocal books, shelfWidth
            if i >= n:
                return maxHeight

            if memo[i][remaining_shelf] != -1:
                return memo[i][remaining_shelf]

            bookH = books[i][1]
            bookW = books[i][0]
            keep = float("inf")
            skip = float("inf")
            # If keep
            if remaining_shelf - bookW >= 0:
                keep = find_min_height(
                    i + 1, remaining_shelf - bookW, max(maxHeight, bookH)
                )

            # skip shelf - Add the prv shelf height + next shelf height
            skip = maxHeight + find_min_height(i + 1, shelfWidth - bookW, bookH)

            memo[i][remaining_shelf] = min(keep, skip)
            return memo[i][remaining_shelf]

        return find_min_height(0, shelfWidth, 0)


def main():
    obj = Solution()
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelfWidth = 4
    expected = 6
    print(obj.minHeightShelves(books, shelfWidth))


if __name__ == "__main__":
    main()
