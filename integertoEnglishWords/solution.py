from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
import heapq
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

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        str_num = str(num)
        res = []
        table_of_one = [
            "Ten",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        table_of_ten = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        eleven_to_nineteen = [
            "",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        append_str = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion"]

        def to_words(n: int) -> list:
            res = []
            if n >= 100:
                hundreds_digit = n // 100
                res.append(table_of_one[hundreds_digit] + " Hundred")
                n %= 100

            digit = n

            if 0 < digit <= 10:
                res.append(table_of_one[digit % 10])
            if 11 <= digit <= 19:
                res.append(eleven_to_nineteen[digit % 10])
            if digit > 19:
                tens_digit = digit // 10
                ones_digit = digit % 10
                res.append(table_of_ten[tens_digit])
                if ones_digit > 0:
                    res.append(table_of_one[ones_digit])

            return res

        append_idx = 0
        while str_num:
            partial_num = int(str_num[-3:])

            if partial_num > 0:
                res = to_words(partial_num) + [append_str[append_idx]] + res
            append_idx += 1
            str_num = str_num[:-3]

        return " ".join(res).strip()


def main():
    obj = Solution()
    num = 1234567
    # num = 12
    num = 110456
    num = 20
    num = 100
    print(obj.numberToWords(num))


if __name__ == "__main__":
    main()