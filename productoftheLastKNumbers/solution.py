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
Problem: https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14
Help:
"""


class ProductOfNumbers:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n)
    SC: o(n)

    ==========================
    Algorithm:
    ==========================
    """

    def __init__(self):
        self.products = []
        self.last_zero = -1

    def add(self, num: int) -> None:
        prv = 1
        n = len(self.products)
        if n > 0:
            prv = self.products[-1]

        if num == 0:
            self.last_zero = n  # index
            num = 1
        self.products.append(num * prv)

    def getProduct(self, k: int) -> int:
        n = len(self.products)
        # print(">", self.products)
        kth_from_start_idx = n - k
        if self.last_zero >= kth_from_start_idx:
            return 0

        if k == len(self.products):
            return self.products[-1]

        last_num = self.products[-1]
        kth_last_num = 1 if self.products[-k - 1] == 0 else self.products[-k - 1]
        return last_num // kth_last_num


def main():
    obj = ProductOfNumbers()
    operations = [
        "add",
        "add",
        "add",
        "add",
        "add",
        "getProduct",
        "getProduct",
        "getProduct",
        "add",
        "getProduct",
    ]

    operation_input = [[3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
    opr_map = {
        "add": obj.add,
        "getProduct": obj.getProduct,
    }
    output = [None, None, None, None, None, None, 20, 40, 0, None, 32]
    for opr, inp in zip(operations, operation_input):
        print(opr_map[opr](*inp))


if __name__ == "__main__":
    main()
