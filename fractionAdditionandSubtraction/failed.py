from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
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

    def fractionAddition(self, expression: str) -> str:
        # split the expression on the basis of "+" and "-"
        separated = []
        i = 0
        expr = ""
        n = len(expression)
        while i < n:
            if expression[i] in ["+", "-"]:
                separated.append(expr)
                separated.append(expression[i])
                expr = ""
            else:
                expr += expression[i]

            i += 1
        separated.append(expr)
        if separated[0] == "":
            separated.pop(0)

        print(separated)
        res = 0
        multiplier = +1
        for exp in separated:
            if exp == "+":
                multiplier = 1
                continue
            elif exp == "-":
                multiplier = -1
                continue
            num, den = exp.split("/")
            num = int(num)
            den = int(den)

            res += round(multiplier * (num / den), 2)

        if res >= 1 or res == 0:
            return f"{int(res)}/1"

        decimal_mapping = dict()
        print(res)
        for i in range(2, 10):
            decimal_mapping[round(1 / i, 2)] = f"1/{i}"
            decimal_mapping[-round(1 / i, 2)] = f"-1/{i}"

        return decimal_mapping[round(res, 2)]


def main():
    obj = Solution()
    expression = "-1/2+1/2"
    expected = "0/1"

    # TS 2
    expression = "-1/2+1/2+1/3"
    expected = "1/3"
    print(obj.fractionAddition(expression))


if __name__ == "__main__":
    main()
