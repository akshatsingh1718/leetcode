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
    TC: O(n*n) + O(n*n) ~ O(2 * n * n)
    SC: O(n*n) [visited] + O(n*n) [deque]

    ==========================
    Algorithm:
    ==========================
    """

    def findMaxFish(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i: int, j: int, visited: Set[Tuple[int, int]]) -> int:
            nonlocal ROWS, COLS, grid
            count = grid[i][j]

            queue = deque([(i, j)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    print(f"== > Trying {nx, ny}")

                    if (
                        (nx, ny) not in visited
                        and 0 <= nx < ROWS
                        and 0 <= ny < COLS
                        and grid[nx][ny] != 0
                    ):
                        visited.add((nx, ny))
                        count += grid[nx][ny]
                        queue.append((nx, ny))

            return count

        max_count = 0
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] > 0:
                    visited.add((i, j))
                    max_count = max(max_count, bfs(i, j, visited))

        return max_count


def main():
    obj = Solution()
    grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
    Output = 7

    # TS 2
    grid = [[6, 1, 10]]
    output = 17
    print(obj.findMaxFish(grid))


if __name__ == "__main__":
    main()
