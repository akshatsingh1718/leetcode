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
    [NOTE: See lc editorial this is too complicated]
    (optimized version of loop.py)
    """

    def isCircularSentence(self, sentence: str) -> bool:
        i = 0
        n = len(sentence)

        while i < n:
            # take word 1
            char1 = ""
            temp_i = i
            while temp_i < n and sentence[temp_i] != " ":
                char1 = sentence[temp_i]
                temp_i += 1

            # take word 2
            char2 = ""
            temp_i2 = 0 if (temp_i == n) else temp_i + 1
            while temp_i2 < n and sentence[temp_i2] != " ":
                if char2 == "":
                    char2 = sentence[temp_i2]
                temp_i2 += 1

            if char1 != char2:
                return False

            i = temp_i + 1

        return True


def main():
    obj = Solution()
    sentence = "leetcode exercises sound delightful"
    expected = True

    # TS 2
    sentence = "leetcode"
    expected = False

    # TS 3
    sentence = "OijvB BGPOXoJfEiYoghRcuOMJTeYPCpnMDVMvLwKfhNoXFTPArVFwjCkCVYBjqgtWfZYOmZBRfmztVwNShHayXzlfhbwEdWCaeTIPDjxTTlRw wlDurKQbfOtdacamikjewLDLGAOlXDfoJwoOdfxWQgkQzRuAlOffJmWdlpdYDmRjrBEFmgBxcuxSzRNzKUDdtdygHvXUmONPTekQgvKQHLazSREAOCKQSQSDgaEeIXAZvuqrbralKNmdkZxyJXEnKMowGAkRZklgvSadAYRBcmPVNBCKsKLUkvLFTHfLEgmHIweJi iDSzzphtFGTDCVrWsFtUnewZAWhne eniIozsaHYuzLoNiDymUxPMPiQORuMU UJRxN NNIbSgSZXKfqIH HrmpohKeCUMRnUhFQymdiYrxtyMlfayY YnLjeSnmMDqbZezTVFT TeOSX XUloFimWQxuaylfvJAUSPbLmAmVIdIHAjjfmNYPwYvOywUiWO"

    print(obj.isCircularSentence(sentence))


if __name__ == "__main__":
    main()
