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
Problem: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
Help: https://www.youtube.com/watch?v=aO-QbJ5eZwU
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O( (N*M)^2 ) [case 2]
    SC: O(N*M) [visited]

    ==========================
    Algorithm:
    ==========================
    (There must be only 0 or >1 islands in the gird)
    There can be only 3 cases
        - Remove 0 island: if there are 0 or more than 1 island present then no need to remove island
        - Remove 1 island: Check if removing a single land can increase the islands count (>1).
        - Remove 2 islands: If neither of the above 2 cases passed then the answer is 2.

    Q. Why only 3 cases ?
    A. Take example of the below grid
        0 0 0 0 0
        0 1 1 1 0
        0 1 1 1 0
        0 1 1 1 0
        0 0 0 0 0

        It looks like remove any 3 linear ones will make the single island into 2 island's but we only
        need to remove 2 lands to make 2 islands. The property of island is that the land present only
        in the vertical and horizontal directions counts for the island and not the diagonal ones. So
        removing any 2 corner diagonal lands will form 2 islands out of 1 island.

        0 0 0 0 0
        0 1 x 1 0
        0 1 1 x 0
        0 1 1 1 0
        0 0 0 0 0
    """

    def minDays(self, grid: List[List[int]]) -> int:
        ROW, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int, visited: Set):
            nonlocal ROW, COLS, grid
            if (
                not (0 <= r < ROW)
                or not (0 <= c < COLS)
                or grid[r][c] != 1
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in directions:
                dfs(dr, dc, visited)

        def count_islands():
            nonlocal ROW, COLS, grid
            count = 0
            visited = set()
            for r in range(ROW):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c, visited)
                        count += 1
            return count

        # CASE 1: check if there are already 0 or more than 1 islands
        if count_islands() != 1:
            return 0

        # CASE 2: Now we know for sure there is only 1 island
        # check if removing 1 land will make the islands 0 or > 1.
        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 0:  # if water
                    continue

                grid[r][c] = 0  # make the land water
                # count islands
                if count_islands() != 1:
                    return 1

                grid[r][c] = 1

        # CASE 3: Till this point we are unable to make the islands break
        # by removing 1 land so definitely its 2 land removal to make
        # the island more than 1
        return 2


def main():
    obj = Solution()
    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    expected = 2
    print(obj.minDays(grid))


if __name__ == "__main__":
    main()
