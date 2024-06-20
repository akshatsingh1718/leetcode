from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
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
    n = len(profit)
    m = len(worker)

    TC: O(nlogn) [heappush] + O(m logm) [sort] + O(m logm) [m times heap pop] ~ O(n long) + O(m logm)
    SC: O(n) [heap]

    ==========================
    Algorithm: (Heap)
    ==========================
    """

    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # 1. create a max heap of profit
        heap = []
        for p, d in zip(profit, difficulty):
            heappush(heap, (-p, d))

        # 2. sort the workers in descending order
        worker.sort(reverse=True)

        # 3. Iterate over workers and pop elements from the heap and if the
        # difficulty is greater then reject the profit since worker cannot
        # perform the task and we no longer need to store the task (difficulty/profit)
        # since our workers has already been sorted in descending order so any
        # other worker will also not able to do the same task
        i = 0
        max_profit = 0
        while i < len(worker) and heap:

            if heap[0][1] > worker[i]:
                heappop(heap)
            else:
                max_profit += -heap[0][0]
                i += 1

        return max_profit


def main():
    obj = Solution()
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    output = 100

    # TS 2
    difficulty = [85, 47, 57]
    profit = [24, 66, 99]
    worker = [40, 25, 25]
    output = 0

    # TS 3
    difficulty = [68, 35, 52, 47, 86]
    profit = [67, 17, 1, 81, 3]
    worker = [92, 10, 85, 84, 82]
    output = 324
    print(obj.maxProfitAssignment(difficulty, profit, worker))


if __name__ == "__main__":
    main()
