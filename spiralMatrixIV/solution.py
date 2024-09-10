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
    TC: O( m * n )
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # create matrix
        res = [([-1] * n) for _ in range(m)]

        m_s, n_s = -1, -1
        m_e, n_e = m, n
        m_i, n_i = 0, 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_i = 0

        while head is not None:

            while head and (m_s < m_i < m_e) and (n_s < n_i < n_e):
                res[m_i][n_i] = head.val
                head = head.next
                m_i += directions[dir_i][0]
                n_i += directions[dir_i][1]

            m_i -= directions[dir_i][0]
            n_i -= directions[dir_i][1]

            if directions[dir_i][0] == 1:  # going down -> shrink from right
                n_e -= 1
            elif directions[dir_i][0] == -1:  # going up -> shrink from left
                n_s += 1
            elif directions[dir_i][1] == 1:  # going right -> shrink from top
                m_s += 1
            elif directions[dir_i][1] == -1:  # going left -> shrink from bottom
                m_e -= 1

            dir_i = (dir_i + 1) % len(directions)

            m_i += directions[dir_i][0]
            n_i += directions[dir_i][1]

        return res


def main():
    obj = Solution()
    m = 3
    n = 5
    head = list_to_ll([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    expected = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
    print(obj.spiralMatrix(m, n, head))


if __name__ == "__main__":
    main()
