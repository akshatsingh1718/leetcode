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
    TC: O(n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def compressedString(self, word: str) -> str:

        comb = ""
        n = len(word)
        if n == 1:
            return f"1{word}"

        i = 0
        ch = word[0]
        streak = 0
        while i < n:
            ch = word[i]  # get the word

            # if the prv word is same then
            # streak will increase
            if i == 0 or word[i - 1] == word[i]:
                streak += 1
            # if the prv word is different
            else:
                # register the prv word streak
                if streak > 0:
                    comb += f"{streak}{word[i-1]}"
                streak = 1  # start new streak

            # if the streak has reached to 9
            # register to the comb and move on
            if streak == 9 or i == n - 1:
                comb += f"{streak}{ch}"
                streak = 0  # start new streak

            i += 1

        return comb


def main():
    obj = Solution()

    # TS 1
    word = "abcde"
    expected = "1a1b1c1d1e"

    # TS 2
    word = "aaaaaaaaaaaaaabb"
    expected = "9a5a2b"

    # TS 3
    word = "aaaaaaaaay"
    expected = "9a1y"
    print(obj.compressedString(word))


if __name__ == "__main__":
    main()
