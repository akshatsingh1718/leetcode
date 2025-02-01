from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil, gcd
import heapq
from heapq import heapify, heappop, heappush
import itertools as it
import sys
from enum import Enum

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

    def orangesRotting(self, grid: List[List[int]]) -> int:

        class Orange(Enum):
            EMPTY = 0
            HEALTHY = 1
            ROTTEN = 2

        ROWS, COLS = len(grid), len(grid[0])

        # find out all the rotten oranges
        rotten_oranges = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == Orange.ROTTEN.value:
                    rotten_oranges.append((i, j))

        time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set(rotten_oranges)
        while rotten_oranges:

            next_rotten_oranges = []
            while rotten_oranges:
                # take the rotten orange coordinates
                x, y = rotten_oranges.pop()
                # make its neighbors rotten as well
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < ROWS
                        and 0 <= ny < COLS
                        and (nx, ny) not in visited
                        and grid[nx][ny] == Orange.HEALTHY.value
                    ):
                        next_rotten_oranges.append((nx, ny))  # orange is rotten
                        visited.add((nx, ny))  # make it as visited

            if next_rotten_oranges:
                rotten_oranges.extend(next_rotten_oranges)
                time += 1

        # check if any orange is left and not rotten
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == Orange.HEALTHY.value:
                    return -1

        return time


def main():
    obj = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    output = 4
    # TS 2
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    output = -1
    print(obj.orangesRotting(grid))


if __name__ == "__main__":
    main()
