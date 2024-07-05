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

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance, maxDistance = float("inf"), -1

        prev = head
        curr = head.next
        nxt = head.next.next
        idx = 1  # pointing to the head.next since we are moving from 1st index and 0th idx can never be a critical

        # first critical point and prv critical point
        first_crit_idx = 0
        prv_crit_idx = 0

        def critical(prv, curr, nxt):
            return (prv.val < curr.val > nxt.val) or (prv.val > curr.val < nxt.val)

        while nxt is not None:  # only move till the 2nd last node

            if critical(prev, curr, nxt):
                # if first idx is found already
                if first_crit_idx != 0:
                    maxDistance = idx - first_crit_idx
                    minDistance = min(minDistance, idx - prv_crit_idx)

                else:
                    first_crit_idx = idx

                prv_crit_idx = idx  # update the last crit idx we found

            prev, curr, nxt = curr, nxt, nxt.next

            idx += 1

        if minDistance == float("inf"):
            minDistance = -1

        return [minDistance, maxDistance]


def main():
    obj = Solution()
    head = list_to_ll([5, 3, 1, 2, 5, 1, 2])
    head = list_to_ll([2, 2, 1, 3])
    expected = [1, 3]
    print(obj.nodesBetweenCriticalPoints(head))


if __name__ == "__main__":
    main()
