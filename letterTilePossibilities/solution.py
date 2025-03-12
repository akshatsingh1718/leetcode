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
Problem: https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================

    TC: O(n * n!)
    [n! since at each step we have atmost n picks and next stage n-1 and so on]
    [n because at each step we are performing string concatenation]

    SC: O(n⋅n!) [n! permutations of n sub sequences] + O(n) [recursion stack space]

    eg ABC
    ------
    when taking permutation of ABC (n=3):
    1. ABC
    2. ACB
    3. BAC
    4. BCA
    5. CAB
    6. CBA
    In total, there are 3!=3 x 2 x 1=6 permutations.

    When taking subset AB, BC, AC (n=2)
    1. (AB, BA)
    2. (BC, CB)
    3. (AC, CA)

    When taking subset A, B, C (n=1)
    1. A
    2. B
    3. C

    ==========================
    Algorithm:
    ==========================
    """

    def numTilePossibilities(self, tiles: str) -> int:

        def find(curr: str, visited: List[int], res: Set[str]):
            nonlocal tiles

            res.add(curr)

            for i in range(len(tiles)):
                if not visited[i]:
                    visited[i] = 1
                    find(curr + tiles[i], visited, res)
                    visited[i] = 0

        n = len(tiles)
        visited = [0] * n
        res = set()
        find("", visited, res)
        return len(res) - 1


def main():
    obj = Solution()
    tiles = "AAB"
    Output = 8
    print(obj.numTilePossibilities(tiles))


if __name__ == "__main__":
    main()
