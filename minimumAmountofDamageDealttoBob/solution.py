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
    ​​1,2,4 easy this time. 3 doesnt seem hard until you get to implementation. -damage / (health / power) is crucial for fourth!

    """

    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        damage_per_hit = []
        ceil = lambda x, y: -(-x // y)

        for i in range(len(damage)):
            di = damage[i]
            hi = health[i]
            # first check how many times we need to hit the ith enemy to kill him
            # this will act as a new health for each enemy since bob power is fixed
            # ex: power=4; health= [4, 5, 7]
            # hits_to_kill= [4/4, 5/4, 7/4] = [1, 2, 2]
            # for 5, 7 their new hp is same
            # this new hp will be used to divide each damage causing by an enemy
            hits_to_kill = ceil(x=hi, y=power)
            # then we need to check what will be the cost to kil the ith person doing damage[i]
            # its the ratio of damage and how many times it will take to kill the ith person
            # the biggest ratio should be the most powerful person and killed first
            damage_per_hit.append((di / hits_to_kill, i))

        damage_per_hit.sort(key=lambda x: x[0], reverse=True)

        d_per_sec = sum(damage)
        res = 0

        i = 0
        while i < len(damage_per_hit):
            idx = damage_per_hit[i][1]
            _damage = damage[idx]
            _health = health[idx]
            res += d_per_sec * ceil(_health, power)
            d_per_sec -= _damage
            i += 1

        return res
