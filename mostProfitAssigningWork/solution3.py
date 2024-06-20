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
Problem: https://leetcode.com/problems/most-profit-assigning-work/description/?envType=daily-question&envId=2024-06-18
Help: https://www.youtube.com/watch?v=_HptwlLP8sI&t=1630s
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n = len(difficulty)
    m = len(worker)
    TC: O(n) [diff_prof] + O(nlogn) [sort] + O(mlogm) [worker sort] + O(m+n) [for loop + while]
    SC:

    ==========================
    Algorithm:
    ==========================
    1. create diff_profit array and sort on the basis of difficulty.
    2. Assign the max profit a job can be rewarded by looking at the rewards for lower difficulty jobs.
    3. Iterate over all the workers and start a binary search for each worker to get the max profit it can have.
    """

    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Create a difficulty profit array
        diff_profit = [[di, pr] for di, pr in zip(difficulty, profit)]
        # sort the array with lowest to highest difficulty
        diff_profit.sort(key=lambda x: x[0])

        n = len(worker)
        m = len(difficulty)

        # sort worker to get the last profit thing to work
        worker.sort()

        total_profit = 0
        max_profit = 0
        j = 0

        for i in range(n):
            # calculate the last difficulty a worker can do and find the max profit it can have
            while j < m and diff_profit[j][0] <= worker[i]:
                max_profit = max(max_profit, diff_profit[j][1])
                j += 1

            # if any worker didnt get any temp_profit then it is sure that
            # it can at least have the profit made by last worker since we have
            # sorted the workers.

            total_profit += max_profit

        return total_profit


def main():
    obj = Solution()
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    output = 100

    # TS 2
    # difficulty = [85, 47, 57]
    # profit = [24, 66, 99]
    # worker = [40, 25, 25]
    # output = 0

    # TS 3
    # profit = [67, 17, 1, 81, 3]
    # difficulty = [68, 35, 52, 47, 86]
    # worker = [92, 10, 85, 84, 82]
    # output = 324

    # TS 4
    difficulty = [23, 30, 35, 35, 43, 46, 47, 81, 83, 98]
    profit = [8, 11, 11, 20, 33, 37, 60, 72, 87, 95]
    worker = [95, 46, 47, 97, 11, 35, 99, 56, 41, 92]
    output = 553
    print(obj.maxProfitAssignment(difficulty, profit, worker))


if __name__ == "__main__":
    main()
