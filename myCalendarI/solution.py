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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def __init__(self):
        self.data = []
        # self.max = float("inf")

    def book(self, start: int, end: int) -> bool:

        for s, e in self.data:
            if not (end <= s or e <= start):
                return False

        self.data.append((start, end))
        return True

        # idx = self._upperBound(start)
        # last_end_for_curr_start = self.data[idx]
        # if last_end_for_curr_start < start + 1: # if curr start time is greater than
        #     res = True
        #     if self.data[idx]

        # if len(self.data) > 0:
        #     if self.data[-1] < start + 1:
        #         res = True

        #     else:  # collision happening
        #         res = False

        # else:  # first meeting will always be true
        #     res = True

        return res

    # def _upperBound(self, x: int) -> int:
    #     n = len(self.data)
    #     low = 0
    #     high = n - 1
    #     ans = n

    #     while low <= high:
    #         mid = (low + high) // 2
    #         # maybe an answer
    #         if self.data[mid] > x:
    #             ans = mid
    #             # look for smaller index on the left
    #             high = mid - 1
    #         else:
    #             low = mid + 1  # look on the right

    #     return ans


"""
[5, 6, 6, 20]
# new 

"""


def main():
    obj = Solution()

    inp = [
        [47, 50],
        [33, 41],
        [39, 45],
        [33, 42],
        [25, 32],
        [26, 35],
        [19, 25],
        [3, 8],
        [8, 13],
        [18, 27],
    ]
    inp = [
        [97, 100],
        [33, 51],
        [89, 100],
        [83, 100],
        [75, 92],
        [76, 95],
        [19, 30],
        [53, 63],
        [8, 23],
        [18, 37],
        [87, 100],
        [83, 100],
        [54, 67],
        [35, 48],
        [58, 75],
        [70, 89],
        [13, 32],
        [44, 63],
        [51, 62],
        [2, 15],
    ]

    res = []
    for s, e in inp:
        res.append(obj.book(s, e))

    print(res)


if __name__ == "__main__":
    main()
