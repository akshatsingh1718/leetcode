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
    m = len(sentence1)
    n = len(sentence2)

    TC: O(m + n) [split] + O(min(m, n))
    SC: O(m + n)

    ==========================
    Algorithm:
    ==========================
    """

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        def isSimilar_old(str1: str, str2: str):
            # check str2 in str1
            lstr1 = str1.split(" ")
            lstr2 = str2.split(" ")
            i = 0
            j = len(lstr1) - 1
            k = 0
            l = len(lstr2) - 1
            # flag to indicate from left or right
            flag = True

            while i <= j and k <= l:
                if flag:
                    if lstr1[i] == lstr2[k]:
                        i += 1
                        k += 1
                    else:
                        flag = False
                else:
                    if lstr1[j] == lstr2[l]:
                        j -= 1
                        l -= 1
                    else:
                        break

            return l < k

        def isSimilar(str1: str, str2: str):
            # check str2 in str1
            lstr1 = str1.split(" ")
            lstr2 = str2.split(" ")
            i = 0
            j = len(lstr1) - 1
            k = 0
            l = len(lstr2) - 1

            # find from left
            while i < len(lstr1) and k < len(lstr2) and lstr1[i] == lstr2[k]:
                i += 1
                k += 1

            while k <= l and lstr1[j] == lstr2[l]:
                l -= 1
                j -= 1

            return l < k

        if len(sentence1) > len(sentence2):
            return isSimilar(sentence1, sentence2)
        return isSimilar(sentence2, sentence1)


def main():
    obj = Solution()
    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    expected = True

    # TS 2
    sentence1 = "of"
    sentence2 = "A lot of words"
    expected = False

    # TS 3
    # sentence1 = "Eating right now"
    # sentence2 = "Eating"
    # expected = True

    # TS 4
    sentence1 = "CwFfRo regR"
    sentence2 = "CwFfRo H regR"
    expected = True
    print(obj.areSentencesSimilar(sentence1, sentence2))


if __name__ == "__main__":
    main()
