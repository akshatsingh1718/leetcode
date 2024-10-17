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
    very close to answer
    """

    def maximumSwap(self, num: int) -> int:

        lnum = [[-int(x), -i] for i, x in enumerate(str(num))]
        n = len(lnum)

        if n == 1:
            return num
        lnum_heap = lnum[:]

        heapify(lnum_heap)
        i = 0
        last_popped = heappop(lnum_heap)
        # pop until top(lnum).idx != its original index
        while i < n - 1 and -last_popped[1] == i:
            last_popped = heappop(lnum_heap)
            i += 1

        

        # print(f"{last_popped=}")
        # print(f"{lnum_heap=} {i=}")
        if i == n or last_popped is None:
            return num

        # swap the last popped with index i
        popped_idx = last_popped[1] * -1
        popped_num = last_popped[0] * -1

        # check if last popped has index same as original in 
        if lnum[popped_idx]


        lnum[i], lnum[popped_idx] = lnum[popped_idx], lnum[i]
        res = 0
        for n, idx in lnum:
            res = res * 10 + n * -1
        return res


def main():
    obj = Solution()
    num = 2736
    expected = 7236

    # TS 2
    # num = 714043
    # expected = 744013

    # TS 3
    # num = 79

    # ts 4
    # num = 10

    # Ts 5
    # num = 98368
    # expected = 98863

    # TS 6
    num = 9973
    expected = 9973
    print(obj.maximumSwap(num))


if __name__ == "__main__":
    main()
