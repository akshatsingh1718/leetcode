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
    def maxDistance(self, s: str, k: int) -> int:
        # start at (0, 0)
        # Moving N: (0, 1)
        # Moving W: (-1, 0)
        # Moving S: (0, -1)
        # Moving E: (1, 0)
        directions = {
            "N": (0, 1),
            "W": (-1, 0),
            "S": (0, -1),
            "E": (1, 0),
        }

        curr_coords = (0, 0)

        def next_move(i: int, j: int, move: str):
            return (i + directions[move][0], j + directions[move][1])

        def next_move_dist(i: int, j: int):
            return abs(i) + abs(j)

        cache = dict()

        def find_max(
            i: int,
            j: int,
            k: int,
            si: int,
        ) -> int:
            nonlocal curr_coords, directions, s
            if si == len(s):
                return 0
            # move to next si
            max_move_dist = 0

            for direction in directions:
                if direction != s[si] and k == 0:
                    continue

                ni, nj = next_move(i, j, direction)

                # use k value if k > 0 or direction chosen is not same as given one
                if direction == s[si]:
                    new_k = k
                elif direction != s[si]:
                    new_k = k - 1

                max_move_dist = max(
                    max_move_dist,
                    find_max(ni, nj, new_k, si + 1),
                    next_move_dist(ni, nj),
                )
            return max_move_dist

        return find_max(0, 0, k, 0)


def main():
    obj = Solution()
    s = "NWSE"
    k = 1
    Output = 3

    # TS 2
    # s = "NSWWEW"
    # k = 3
    # Output = 6

    # TS 3
    # s = "SN"
    # k = 0
    # Output = 1
    print(obj.maxDistance(s, k))


if __name__ == "__main__":
    main()
