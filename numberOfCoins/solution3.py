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
    TC: O(M * V)
    SC:

    ==========================
    Algorithm:
    ==========================
    """
    def minCoins(self, coins, M, V):

        # create table for V coins from 0->V and find
        # the no of coins required to for each table[i]
        table = [float("inf") for _ in range(V + 1)]

        # since 0 coin required 0 no of coins
        table[0] = 0

        # Find out the coins required for V = 1 -> V
        for coin_to_make in range(1, V + 1):

            # check for coins we have in coins
            for j in range(M):

                # if coin[j] is eligible to contribute for reaching to coin_to_make
                if coins[j] <= coin_to_make:

                    # this is how much coins we will be needing if we dont use coins[j]
                    # for reaching to coin_to_make.
                    # coins_needed_wo_using_coinsJ will get us the coins needed without coins[j]
                    # and by negating coins[j] we can assume that be removing one coin contribution
                    # how much coins are we needing and if the how much coins are we needing + 1 gets
                    # us the lower coins count than previously we were using then we have the new min coins usage
                    coins_needed_wo_using_coinsJ = table[coin_to_make - coins[j]]

                    if (
                        coins_needed_wo_using_coinsJ != float("inf")
                        and coins_needed_wo_using_coinsJ + 1 < table[coin_to_make]
                    ):
                        table[coin_to_make] = coins_needed_wo_using_coinsJ + 1

        if table[V] == float("inf"): return -1

        return table[V]


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
