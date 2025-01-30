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
    TC: O(n) [loop] * { o(n) [find connected nodes] + O(n) [longest path] } ~ O(n^2)
    SC: O(n) [adj] + O(n) [connected nodes set]

    ==========================
    Algorithm:
    ==========================
    1. Find the different connected components and save the connected nodes from each of them.
    2. Create groups variable.
    3. Iterate over all the different connected components and find the max/longest path you can have for each component and add it to the groups.
    4. While checking for the longest path check if we ran into the bipartite graph (cycle of len 3) which means we cannot assign them different groups.

    (A)  ->  (B)
       \    /
         (C)

     If we assign A = grp 1 and B = grp 2 and C = grp 2 then it violates the given condition as two adjacent groups difference should be 1 but B and C has a difference of 0.
    """

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create adj list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def find_connected_nodes(
            i: int, visited: Set[int], adj: List[List[int]]
        ) -> Set[int]:

            queue = deque([i])
            connected_nodes = set([i])

            while queue:
                node = queue.popleft()

                for neig in adj[node]:
                    if neig in connected_nodes:
                        continue

                    queue.append(neig)
                    connected_nodes.add(neig)
                    visited.add(neig)

            return connected_nodes

        def find_longest_path_len(i: int, adj: List[List[int]]) -> int:

            max_distance = 1
            queue = deque([i])
            distances = {i: 1}

            while queue:

                node = queue.popleft()
                for neig in adj[node]:
                    if neig in distances:
                        if distances[neig] == distances[node]:
                            return -1
                        continue

                    queue.append(neig)
                    distances[neig] = distances[node] + 1
                    max_distance = max(max_distance, distances[neig])

            return max_distance

        # find the different connected components
        res = 0
        visited: Set[int] = set()
        for i in range(1, n + 1):
            if i in visited:
                continue
            visited.add(i)

            connected_nodes = find_connected_nodes(i, visited, adj)

            max_length = 0
            for node in connected_nodes:
                length = find_longest_path_len(node, adj)
                if length == -1:
                    return -1

                max_length = max(max_length, length)

            res += max_length
        return res


def main():
    obj = Solution()
    n = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
    output = 4

    # TS 2
    edges = [
        [67, 29],
        [13, 29],
        [77, 29],
        [36, 29],
        [82, 29],
        [54, 29],
        [57, 29],
        [53, 29],
        [68, 29],
        [26, 29],
        [21, 29],
        [46, 29],
        [41, 29],
        [45, 29],
        [56, 29],
        [88, 29],
        [2, 29],
        [7, 29],
        [5, 29],
        [16, 29],
        [37, 29],
        [50, 29],
        [79, 29],
        [91, 29],
        [48, 29],
        [87, 29],
        [25, 29],
        [80, 29],
        [71, 29],
        [9, 29],
        [78, 29],
        [33, 29],
        [4, 29],
        [44, 29],
        [72, 29],
        [65, 29],
        [61, 29],
    ]
    n = 92
    output = 57

    print(obj.magnificentSets(n, edges))


if __name__ == "__main__":
    main()
