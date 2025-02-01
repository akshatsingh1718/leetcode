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
    TC: O(n^2) [assign id and get area] + O(n^2) [get max area island]
    SC: O(n^2) [new grid if not inplace] + O(n) [visited] O(n) [deque]

    ==========================
    Algorithm:
    ==========================
    """

    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i: int, j: int, island_id: int, visited: Set[Tuple[int, int]]) -> int:
            nonlocal grid, directions

            queue = deque([(i, j)])
            area = 1

            while queue:
                (x, y) = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if (
                        0 <= nx < ROWS
                        and 0 <= ny < COLS
                        and (nx, ny) not in visited
                        and grid[nx][ny] == 1
                    ):
                        grid[nx][ny] = island_id
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        area += 1

            return area

        id_to_area = {}
        visited: Set[Tuple[int, int]] = set()
        curr_id = 2
        max_island_area = 0

        # find the area of each islands
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:

                    visited.add((i, j))
                    grid[i][j] = curr_id
                    id_to_area[curr_id] = bfs(i, j, curr_id, visited)
                    max_island_area = max(max_island_area, id_to_area[curr_id])
                    curr_id += 1

        # check by assigning a "0" -> "1" can we make a new bigger island
        for i in range(ROWS):
            for j in range(COLS):
                if not (grid[i][j] == 0):  # only "0" allowed to go further
                    continue

                unique_ids = set()
                for dx, dy in directions:
                    nx, ny = dx + i, dy + j
                    # id coords are valid and they should have their id's (which are always gt 1)
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] > 1:
                        unique_ids.add(grid[nx][ny])

                island_area = 1
                for uid in unique_ids:
                    island_area += id_to_area[uid]

                max_island_area = max(max_island_area, island_area)

        return max_island_area


def main():
    obj = Solution()
    grid = [[1, 0], [0, 1]]
    Output = 3
    print(obj.largestIsland(grid))


if __name__ == "__main__":
    main()
