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

    m = nodes of tree
    h = height of tree
    n = nodes of list
    TC: O(m * n)
    SC: O(h) [recursive calls stack]

    ==========================
    Algorithm:
    ==========================
    """

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(root: TreeNode, l_root: ListNode):
            if l_root is None:
                return True
            if root is None or root.val != l_root.val:
                return False

            res = False
            res = res or dfs(root.right, l_root.next)

            res = res or dfs(root.left, l_root.next)

            return res

        queue = [root]

        while queue:

            node = queue.pop(0)

            if dfs(node, head):
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return False


def main():
    obj = Solution()
    head = list_to_ll([4, 2, 8])
    root = list_to_binary_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    )

    # TS 2
    # head = list_to_ll([1, 10])
    # root = list_to_binary_tree([1, None, 1, 10, 1, 9])
    # expected = True

    # TS 3
    head = list_to_ll([2, 2, 1])
    root = list_to_binary_tree([2, None, 2, None, 2, None, 1])
    expected = True
    print(obj.isSubPath(head, root))


if __name__ == "__main__":
    main()
