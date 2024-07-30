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
    TC: O(n) [main for loop] * O(n) ~ O(n^2)
    SC: O(n) [cache]

    ==========================
    Algorithm:
    ==========================
    """

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        # [-1] * 4 because there are atmost 3 soldiers in a team
        # we can also have a 3 size array and use cache[startIdx][teamSize-1]
        inc_teams = [[0] * 4 for _ in range(n)]
        dec_teams = [[0] * 4 for _ in range(n)]

        # Fill the base cases. (Each soldier is a sequence of length 1)
        for i in range(n):
            inc_teams[i][1] = 1
            dec_teams[i][1] = 1

        # fill the tables
        for count in range(2, 4):  # for finding 2 and 3rd soldier
            for i in range(n):  # find the second soldier
                for j in range(i + 1, n):  # find the 3rd soldier
                    if rating[i] > rating[j]:
                        dec_teams[j][count] += dec_teams[i][count - 1]
                    if rating[i] < rating[j]:
                        inc_teams[j][count] += inc_teams[i][count - 1]

        for i in range(n):
            res += inc_teams[i][3] + dec_teams[i][3]
        return res


def main():
    obj = Solution()
    rating = [2, 5, 3, 4, 1]
    expected = 3
    print(obj.numTeams(rating))


if __name__ == "__main__":
    main()
