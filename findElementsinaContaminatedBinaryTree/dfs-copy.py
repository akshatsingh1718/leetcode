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
Problem: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2025-02-21
Help:
"""


class FindElements:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) [create tree] + O(logn) [find]
    SC: O(n) [creating same tree again]

    ==========================
    Algorithm:
    ==========================
    """

    def dfs_recover(self, root: TreeNode):
        if not root:
            return

        # update the left child value
        if root.left:
            root.left.val = root.val * 2 + 1
            self.dfs_recover(root.left)

        # update the right child value
        if root.right:
            root.right.val = root.val * 2 + 2
            self.dfs_recover(root.right)

    def dfs_find(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        if root.val == target:
            return True

        found = False
        # update the left child value
        if root.left:
            found |= self.dfs_find(root.left, target)

        # update the right child value
        if root.right:
            found |= self.dfs_find(root.right, target)

        return found

    def __init__(self, root: Optional[TreeNode]):
        if not root:
            return

        self.root = root
        self.root.val = 0
        self.dfs_recover(self.root)

    def find(self, target: int) -> bool:
        return self.dfs_find(self.root, target)


def main():
    root = list_to_binary_tree([-1, -1, -1, -1, -1])
    obj = FindElements(root)
    inputs = [1, 3, 5]
    for inp in inputs:
        print(obj.find(inp))


if __name__ == "__main__":
    main()
