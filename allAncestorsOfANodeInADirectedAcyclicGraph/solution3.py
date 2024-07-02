from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
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
Problem:)
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(E) [adj list] + O(V * (V + V + E)) ~ O(V * (V + E))
    SC: O(E) [adj list] + O(E * E) [result; since worst case every E can have (E-1) ancestors]

    ==========================
    Algorithm: `graph-dfs`
    ==========================
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(currNode: int, visited: List[int]):
            nonlocal  adjacency_list

            for child in adjacency_list[currNode]:
                if visited[child] == 0: # not visited
                    visited[child] = 1
                    dfs(currNode=child, visited=visited)


        # create adj list and reverse the direction for the graph
        adjacency_list = defaultdict(lambda : [])
        for u, v in edges:
            adjacency_list[v].append(u) # connection is reversed

        result = [[] for _ in range(n)]  # O(V) or O(N)

        # start the dfs and append the reversed graph visited nodes to the result
        for node_i in range(n):  # O(V)
            visited = [0 for _ in range(n)]
            dfs(currNode=node_i, visited=visited)  # O(V+ E)

            for j in range(n):
                if visited[j] == 1:
                    result[node_i].append(j)

        return result


def main():
    obj = Solution()
    n = 8
    edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    expected = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

    # TS 2
    edgeList = [[7, 5], [2, 5], [0, 7], [0, 1], [6, 1], [2, 4], [3, 5]]
    n = 9
    print(obj.getAncestors(n, edgeList))


if __name__ == "__main__":
    main()
