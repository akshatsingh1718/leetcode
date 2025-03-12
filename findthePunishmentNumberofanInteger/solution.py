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
Problem: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) * O(2 ^ log(n))
    SC: O(n log(n)) [n times * memo] + O(log(n)) [stack space when each num is treated individually]

    ==========================
    Algorithm: `dp`
    ==========================
    """

    def punishmentNumber(self, n: int) -> int:

        def find_partition(
            start_idx: int, curr_sum: int, num: str, target: int, memo: List[List[int]]
        ) -> bool:
            # check if start_idx index is equal to
            if start_idx == len(num):
                return curr_sum == target

            if curr_sum > target:
                return False

            if memo[curr_sum][start_idx] != -1:
                return memo[curr_sum][start_idx] == 1

            # from from start index to len of curr_num
            is_possible = False

            for j in range(start_idx, len(num)):
                temp_num = int(num[start_idx : j + 1])

                is_possible |= find_partition(
                    j + 1, curr_sum + temp_num, num, target, memo
                )
                if is_possible:
                    break

            memo[curr_sum][start_idx] = int(is_possible)

            return is_possible

        # since square of 1 is always eq to itself
        res = 1

        for i in range(2, n + 1):

            square = i * i
            str_square = str(square)
            # create a memo for handling repetitive cases
            # 1st dim: from 0 -> (i+1) since gt i+1 are not acceptable and will return false immediately
            # 2nd dim: from 0 -> len(square) since its index for the square
            memo = [([-1] * len(str_square)) for _ in range(i + 1)]
            # check if any partition can make i again
            if find_partition(0, 0, str_square, i, memo):
                res += square
        return res


def main():
    obj = Solution()
    n = 10
    Output = 182
    print(obj.punishmentNumber(n))


if __name__ == "__main__":
    main()
