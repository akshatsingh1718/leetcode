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
    n =
    TC: O(E) [adj] + O(V) [find zeros indegree] + O(E + V) [topo while]
    SC: O(V) [indegrees] + O(V) [indegrees]

    ==========================
    Algorithm:
    ==========================
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            # to take course `u` we should first do `v`. so v -> u
            adj[v].append(u)
            indegrees[u] += 1

        # get all the indegrees of 0
        zero_indegrees = deque([])

        for i in range(numCourses):
            if indegrees[i] == 0:
                zero_indegrees.append(i)

        res = []
        while zero_indegrees:

            node = zero_indegrees.popleft()
            res.append(node)

            for neig in adj[node]:
                indegrees[neig] -= 1
                if indegrees[neig] == 0:
                    zero_indegrees.append(neig)

        return res if len(res) == numCourses else []


def main():
    obj = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    output = [0, 2, 1, 3]
    # TS 2
    # numCourses = 3
    # prerequisites = [[1, 0], [1, 2], [0, 1]]
    # output = []

    # TS 3
    # numCourses = 4
    # prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    # output = []
    print(obj.findOrder(numCourses, prerequisites))


if __name__ == "__main__":
    main()
