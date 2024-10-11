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
Problem: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/submissions/1418850707/?envType=daily-question&envId=2024-10-11
Help: https://www.youtube.com/watch?v=NePJRPCuOwg
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(nlogn)[sorting] + O(n * logn) [loop + heappush]
    SC: O(2 * n) [2 heap]

    ==========================
    Algorithm: `min-heap`
    ==========================
    """

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetArrivalTime = times[targetFriend][0]
        times.sort()  # sort by arrival time
        n = len(times)

        occupied_chairs = []  # (departure_time, occupied_chair_no) : min heap
        free_chairs = []  # (free_chair_no) : min_heap
        next_chair_no = 0

        for i in range(n):
            curr_arrival = times[i][0]
            curr_dept = times[i][1]
            free_chair_no = -1

            # check if we can free some occupied chairs
            while occupied_chairs and occupied_chairs[0][0] <= curr_arrival:
                free_chair_no = heappop(occupied_chairs)[1]
                heappush(free_chairs, free_chair_no)

            # check if out free_chairs is non empty
            if free_chairs:
                free_chair_no = heappop(free_chairs)  # get the min chair no we can have
            else:
                # if no chairs are free in free_chairs heap then use next_chair_no
                free_chair_no = next_chair_no
                next_chair_no += 1

            heappush(occupied_chairs, (curr_dept, free_chair_no))

            if targetArrivalTime == curr_arrival:
                return free_chair_no

        return -1


def main():
    obj = Solution()
    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    expected = 1

    # TS 2
    # times = [[3, 10], [1, 5], [2, 6]]
    # targetFriend = 0
    # expected = 2

    # TS 3
    times = [
        [33889, 98676],
        [80071, 89737],
        [44118, 52565],
        [52992, 84310],
        [78492, 88209],
        [21695, 67063],
        [84622, 95452],
        [98048, 98856],
        [98411, 99433],
        [55333, 56548],
        [65375, 88566],
        [55011, 62821],
        [48548, 48656],
        [87396, 94825],
        [55273, 81868],
        [75629, 91467],
    ]
    targetFriend = 6

    print(obj.smallestChair(times, targetFriend))


if __name__ == "__main__":
    main()
