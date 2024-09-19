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
    TC: O(n) * O(n^2) [at each stage we are splitting two sides] ~ O(n * 2^n)
    SC: O(2^n)

    ==========================
    Algorithm:
    ==========================
    1. Move from left to right and check for operator +, - or *.
    2. From the operator's index call the function again two times for left and right side of the halves.
    3. The left side will be evaluated from (left -> i - 1) since ith index is the operator and from (i + 1 -> right).
    4. The two parts will give us all the possible ways we can evaluate the expressions.
    5. Move forward to the next operator and follow step 2.
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def dfs(left: int, right: int):
            nonlocal expression, n

            res: List[int] = []

            for i in range(left, right + 1):
                # if the ith expression is an operator
                op = expression[i]
                if op in operations:

                    left_nums = dfs(left, i - 1)
                    right_nums = dfs(i + 1, right)

                    # calculate the result by doing operation on left nums with right nums
                    # using the current operation we have
                    for lnum in left_nums:
                        for rnum in right_nums:
                            res.append(operations[op](lnum, rnum))

            if len(res) == 0:
                res.append(int(expression[left : right + 1]))

            return res

        return dfs(0, n - 1)


def main():
    obj = Solution()
    expression = "2*3-4*5"
    expected = [-34, -14, -10, -10, 10]
    print(obj.diffWaysToCompute(expression))


if __name__ == "__main__":
    main()
