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
    TC: O(m * n) [while loop] * O( log(m*n) ) [heap push] ~ O( mn * log(mn) )
    SC: O(m * n)

    ==========================
    Algorithm:
    ==========================
    """

    def minimumTime_old(self, grid: List[List[int]]) -> int:
        # does not consider re walking
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(i: int, j: int, t: int) -> int:
            nonlocal ROWS, COLS, directions, visited
            if i == ROWS - 1 and j == COLS - 1:
                return 0

            visited.add((i, j))

            steps = float("inf")
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if (
                    0 <= new_i < ROWS
                    and 0 <= new_j < COLS
                    and grid[new_i][new_j] <= t + 1
                    and (new_i, new_j) not in visited
                ):
                    steps = min(steps, dfs(new_i, new_j, t + 1) + 1)

            return steps

        res = dfs(0, 0, 0)
        return -1 if res == float("inf") else res

    def minimumTime(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pq = [(0, 0, grid[0][0])]  # i, j, t
        visited = set()

        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        while pq:
            i, j, t = heappop(pq)

            if i == ROWS - 1 and j == COLS - 1:
                return t

            if (i, j) in visited:
                continue

            visited.add((i, j))

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if not (
                    0 <= new_i < ROWS
                    and 0 <= new_j < COLS
                    and (new_i, new_j) not in visited
                ):
                    continue

                wait_time = 1 if (grid[new_i][new_j] - t) % 2 == 0 else 0
                next_time = max(t + 1, wait_time + grid[new_i][new_j])

                heappush(pq, (new_i, new_j, next_time))

        return -1


def main():
    obj = Solution()
    grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
    expected = 7

    # TS 2
    # grid = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
    # expected = -1
    print(obj.minimumTime(grid))


if __name__ == "__main__":
    main()
