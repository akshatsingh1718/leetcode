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
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key= lambda x: x[0])
        res = 0
        starting = 0
        max_day = 0

        for start, end in meetings:
            diff = start - starting - 1
            if diff > 0:
                # print(f"{start=} {starting=} {diff=}")
                res += diff
            max_day = max(max_day, end)
            starting = max_day

        # for last day
        diff = days - starting
        if diff > 0:
            # print(f"{days=} {start=} {starting=} {diff=}")

            res += diff

        return res


def main():

    obj = Solution()
    days = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    output = 2

    # TS 2
    # days = 5
    # meetings = [[2,4],[1,3]]
    # output = 1

    # TS 3
    # days = 6
    # meetings = [[1,6]]
    # output = 0

    # TS 4
    # days = 8
    # meetings = [[3,4],[4,8],[2,5],[3,8]]
    # output = 1

    # TS 5
    # days = 57
    # meetings = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]
    # output =1

    print(obj.countDays(days, meetings))


if __name__ == "__main__":
    main()
