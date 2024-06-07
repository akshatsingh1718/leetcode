from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache

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
def create_adjacency_list(edges: List[tuple]):
    adjacency_list = {}

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
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
    (Greedy will not work)
    V = 11
    M = 4
    coins = [9, 6, 5, 1]
    output = 2

    Using greedy will take 9, 1, 1 = 3 steps
    Whereas 5,6 = 2 steps

    """

    def minCoins(self, coins, M, V):

        coins.sort()
        res = 0

        def find_idx(num: int):
            nonlocal coins

            low = 0
            high = len(coins) - 1
            while low < high:
                mid = low + (high - low) // 2

                if coins[mid] == num:
                    return mid
                elif coins[mid] < num:
                    low = mid + 1
                elif coins[mid] > num:
                    high = mid - 1

            return low

        while V > 0:
            idx = find_idx(V)
            V -= coins[idx]
            res += 1

        return res


class Solution:
    """
    TLE 
    ==========================
    Time and space complexity:
    ==========================
    TC: O(M^V)
    SC: O(V) [max recursion space]

    ==========================
    Algorithm:
    ==========================
    """

    def minCoins(self, coins, M, V):

        cache = dict()

        def find_coins_to_use(start: int, V_left: int, steps: int):
            nonlocal coins, M, cache

            if V_left == 0:
                return steps

            min_steps = float("inf")

            for i in range(start, M):
                if V_left - coins[i] >= 0:
                    min_steps = min(
                        min_steps, find_coins_to_use(V_left - coins[i], steps + 1)
                    )

            return min_steps

        min_coins = find_coins_to_use(0, V, 0)
        return -1 if (min_coins == float("inf")) else min_coins


def main():
    obj = Solution()
    V = 30
    M = 3
    coins = [25, 10, 5]
    output = 2

    # TS 2
    V = 11
    M = 4
    coins = [9, 6, 5, 1]
    output = 2

    print(obj.minCoins(coins, M, V))


if __name__ == "__main__":
    main()
