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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # crate adj list
        adj_list = defaultdict(lambda: [])
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        connecting_cities = []
        # res = float("inf")
        # city_and_neigh = []
        cities_visited  = defaultdict(lambda: [])
        for city_no in range(n):
            # move to the cities 
            queue = [city_no]
            visited= {city_no}
            current_cities_visited = 0
            while queue:
                from_city = queue.pop(0)
                for neigh_city, w in adj_list[from_city]:
                    if w <= distanceThreshold and neigh_city not in visited:
                        queue.append(neigh_city)
                        visited.add(neigh_city
                        visited.add(neigh_city))
                        current_cities_visited += 1

            cities_visited[current_cities_visited].append(city_no)

        print(cities_visited)
        lowest_city = min(list(cities_visited.keys()))
        return max(cities_visited[lowest_city])
            

def main():
    obj = Solution()
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold = 4
    expected= 3

    # TS 2
    # n = 5
    # edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    # distanceThreshold = 2
    # expected= 0
    print(obj.findTheCity(n, edges, distanceThreshold))

if __name__ == "__main__":
    main()
