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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def dfs(
        self,
        i: int,
        parent: int,
        in_time: List[int],
        low_time: List[int],
        visited: List[int],
        adj: List[List[int]],
        result: List[Tuple[int, int]],
    ):
        # mark the i visit
        visited[i] = 1
        # in_time[i] = low_time[i] = self.timer
        # self.timer += 1
        # print(f"Visited {i}")

        for neig in adj[i]:
            # if parent then continue
            if neig == parent:
                continue

            # print(f"Move {i} --> {neig}")

            # if visited the its a cycle and cannot make a bridge
            if visited[neig] != 0:
                low_time[i] = min(low_time[neig], low_time[i])

            else:  # not visited yet
                # visit the neig first
                self.dfs(neig, i, in_time, low_time, visited, adj, result)
                # then check for the low time of the visited child and node itself.
                low_time[i] = min(low_time[neig], low_time[i])
                # check if this connection can be a bridge
                # If not a bridge edge then, in_time[node i] >= low_time[node neigh]
                # else if, a bridge edge then, in_time[node i] < low_time[node neigh]
                if in_time[i] < low_time[neig]:
                    result.append((i, neig))

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # create adj
        adj = [[] for _ in range(n)]
        self.timer = 1
        # Create undirected graph edges
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n
        in_time = list(range(1, n + 1))
        low_time = list(range(1, n + 1))
        # in_time = [0] * n
        # low_time = [0] * n
        result = []

        self.dfs(0, -1, in_time, low_time, visited, adj, result)
        return result


def main():
    obj = Solution()
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    Output = [[1, 3]]

    # TS 2
    print(obj.criticalConnections(n, connections))


if __name__ == "__main__":
    main()
