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

class Node():
    def __init__(self, freq: int = 0, _next=None, prv = None ) -> None:
        self.freq = freq
        self.next = _next 
        self.prv = prv
        self.store = set()

class AllOne:

    def __init__(self):
        self.dhead = Node(-1)
        self.dtail = Node(float("inf"))

        self.dhead.next = self.dtail
        self.dtail.prv = self.dhead

        self.store = set()


    def inc(self, key: str) -> None:
        # check if not already present
        if key not in self.store:
            freq_to_find = 1
        else:
            node = self.dhead
            while node is not None and key not in node.store:
                node = node.next



        node = self.dhead
        while node is not None and 

        self.store.add(key)

    def dec(self, key: str) -> None:
        if key not in self.store:
            return

        self.store[key] -= 1
        if self.store[key] == 0:
            del self.store[key]

    def getMaxKey(self) -> str:
        if len(self.store) == 0:
            return ""

        maxVal = max(self.store.values())
        resp = ""
        for key in self.store:
            if self.store[key] == maxVal:
                resp = key
                break
        return resp

    def getMinKey(self) -> str:
        if len(self.store) == 0:
            return ""

        maxVal = min(self.store.values())
        resp = ""
        for key in self.store:
            if self.store[key] == maxVal:
                resp = key
                break
        return resp


def main():
    obj = AllOne()


if __name__ == "__main__":
    main()
