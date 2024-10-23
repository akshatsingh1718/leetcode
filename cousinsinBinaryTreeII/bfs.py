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
Problem: https://leetcode.com/problems/cousins-in-binary-tree-ii/?envType=daily-question&envId=2024-10-23
Help: https://www.youtube.com/watch?v=xvwTd19SncE
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2n) ~ O(n)
    SC: O(n) [depth sum]

    ==========================
    Algorithm:
    ==========================
    """

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        # get the depth sums
        depth_sum = []
        queue = [root]
        while queue:
            depth_sum.append(0)
            for _ in range(len(queue)):
                node = queue.pop(0)
                depth_sum[-1] += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        # set the sum
        queue = [(root, root.val)]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node, self_nd_sibling_val = queue.pop(0)
                node.val = depth_sum[depth] - self_nd_sibling_val

                child_self_nd_sibling_val = (node.left.val if node.left else 0) + (
                    node.right.val if node.right else 0
                )

                if node.left:
                    queue.append((node.left, child_self_nd_sibling_val))

                if node.right:
                    queue.append((node.right, child_self_nd_sibling_val))

            depth += 1

        return root


def main():
    obj = Solution()
    root = [5, 4, 9, 1, 10, None, 7]
    expected = [0, 0, 0, 7, 7, None, 11]


if __name__ == "__main__":
    main()
