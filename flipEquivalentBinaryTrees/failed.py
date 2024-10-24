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
    TC: O(n) [while]
    SC: O(2n) [counts] + O(2n) [dqueue]

    ==========================
    Algorithm: `bfs` `count-frequency`
    ==========================
    I thought we want to compare the frequency of elements of every depth
    """

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False

        dqueue1, dqueue2 = [root1], [root2]

        while dqueue1 and dqueue2:

            if len(dqueue1) != len(dqueue2):
                return False

            n = len(dqueue1)
            count1 = defaultdict(int)
            count2 = defaultdict(int)
            for _ in range(n):
                # print(f"========================")
                # print(f"{[r.val for r in dqueue1]}")
                # print(f"{[r.val for r in dqueue2]}")
                node1, node2 = dqueue1.pop(0), dqueue2.pop(0)

                count1[node1.val] += 1
                count2[node2.val] += 1

                # add nodes in dqueue1
                if node1.left:
                    dqueue1.append(node1.left)
                if node1.right:
                    dqueue1.append(node1.right)

                # add nodes in dqueue2
                if node2.right:
                    dqueue2.append(node2.right)
                if node2.left:
                    dqueue2.append(node2.left)

            for key in count1.keys():
                if count1[key] != count2[key]:
                    return False

        if dqueue2 or dqueue1:
            return False

        return True


def main():
    obj = Solution()
    root1 = list_to_binary_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8])
    root2 = list_to_binary_tree([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])
    expected = True

    # TS 2
    root1 = list_to_binary_tree([0, 3, 1, None, None, None, 2])
    root2 = list_to_binary_tree([0, 3, 1, 2])
    expected = False
    print(obj.flipEquiv(root1, root2))


if __name__ == "__main__":
    main()
