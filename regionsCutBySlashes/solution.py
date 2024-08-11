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
    N = len(grid)
    TC: O(N^2)[created grid2] + O(N^2) [fill out blocked cells] + O(N^2)[visit each cell] ~ O(N^2)
    SC: O(3 * N^2) + O(3 * N^2)[visited] ~ O(N^2)

    ==========================
    Algorithm:
    ==========================
    """

    def regionsBySlashes(self, grid: List[str]) -> int:
        # create a new grid2 with 3x size
        # denote 0 for empty space and 1 for a partition
        ROW, COL = len(grid), len(grid[0])
        ROW2, COL2 = ROW * 3, COL * 3
        grid2 = [[0] * COL2 for _ in range(ROW2)]

        # Filling the blocked cells
        for r in range(ROW):
            for c in range(COL):
                r2_start, c2_start = r * 3, c * 3

                if grid[r][c] == "\\":
                    grid2[r2_start][c2_start] = 1
                    grid2[r2_start + 1][c2_start + 1] = 1
                    grid2[r2_start + 2][c2_start + 2] = 1

                elif grid[r][c] == "/":
                    grid2[r2_start][c2_start + 2] = 1
                    grid2[r2_start + 1][c2_start + 1] = 1
                    grid2[r2_start + 2][c2_start] = 1

        def dfs(r: int, c: int, visited: set):
            if (
                r < 0
                or c < 0
                or (r, c) in visited
                or r == ROW2
                or c == COL2
                or grid2[r][c] != 0
            ):
                return

            visited.add((r, c))
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in directions:
                dfs(dr, dc, visited)

        # Move to each cell and start a dfs for area it is covering (like count island)
        visited = set()
        res = 0
        for r in range(ROW2):
            for c in range(COL2):
                if (r, c) not in visited and grid2[r][c] == 0:
                    dfs(r, c, visited)
                    res += 1

        return res


def main():
    obj = Solution()
    grid = ["/\\", "\\/"]
    expected = 5
    print(obj.regionsBySlashes(grid))


if __name__ == "__main__":
    main()
