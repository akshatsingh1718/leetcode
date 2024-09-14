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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(i, j, h, d) -> bool:
            nonlocal visited, grid

            print(f"{'>' * d}{i, j} |  h={h}")
            # if health is down or already visited location
            if h < 1 or (i, j) in visited:
                return False

            if i == ROWS - 1 and j == COLS - 1:
                print(h)
                return True

            visited.add((i, j))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            can_reach = False
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj

                # out of bounds
                if not (0 <= new_i < ROWS) or not (0 <= new_j < COLS):
                    continue

                new_h = h - grid[new_i][new_j]

                can_reach |= dfs(new_i, new_j, new_h, d + 1)

            return can_reach

        return dfs(0, 0, health - grid[0][0], 0)


def main():
    obj = Solution()
    grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
    health = 1
    expected = True

    # TS 2
    # grid = [
    #     [0, 1, 1, 0, 0, 0],
    #     [1, 0, 1, 0, 0, 0],
    #     [0, 1, 1, 1, 0, 1],
    #     [0, 0, 1, 0, 1, 0],
    # ]
    # health = 3
    # expected = False

    # TS 3
    # grid = [[1, 1, 1, 1]]
    # health = 4
    # expected = False

    # TS 4
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    health = 5
    expected = True
    print(obj.findSafeWalk(grid, health))


if __name__ == "__main__":
    main()
