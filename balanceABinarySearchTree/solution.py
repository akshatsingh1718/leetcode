from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
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
    n = # nodes
    TC: O(n) [inorder traversal] + O(n) [balance] ~ O(n)
    SC: O(n) [sorted_arr] + O(n) [inorder rec stack space] + O(n) [balance stack space] ~ O(n)

    ==========================
    Algorithm:
    ==========================
    """

    def balanceBST(self, root: TreeNode) -> TreeNode:

        # find the sorted array using inorder traversal
        sorted_arr = []

        def inorder_traversal(root: TreeNode):
            nonlocal sorted_arr
            if root is None:
                return

            inorder_traversal(root.left)
            sorted_arr.append(root.val)
            inorder_traversal(root.right)

        # create the binary tree from the mid of the sorted array
        # recursively break the sorted array from (start -> mid - 1) and (mid + 1 -> end).
        # the mid will be the parent node and (start -> mid - 1) will get the left node and
        # (mid + 1 -> end) will get the right child node
        def balance_bst(sorted_arr: List[int], start: int, end: int):
            # Base case: If start ptr exceeds end ptr then no mid can be found
            if start > end:
                return None

            mid = start + (end - start) // 2

            left_child = balance_bst(sorted_arr, start, mid - 1)
            right_child = balance_bst(sorted_arr, mid + 1, end)

            return TreeNode(val=sorted_arr[mid], left=left_child, right=right_child)

        inorder_traversal(root)
        return balance_bst(sorted_arr, 0, len(sorted_arr) - 1)


def main():
    obj = Solution()
    root = list_to_binary_tree([1, None, 2, None, 3, None, 4, None, None])
    expected = list_to_binary_tree([2, 1, 3, None, None, None, 4])
    obj.balanceBST(root)


if __name__ == "__main__":
    main()
