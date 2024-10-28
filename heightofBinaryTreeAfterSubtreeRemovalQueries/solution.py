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
    TC: O(4n) []
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        # create height, level, levelMaxHeight and levelSecondMaxHeight
        N = 100001
        height = [0] * N
        level = [0] * N
        levelMaxHeight = [0] * N
        levelSecondMaxHeight = [0] * N

        def find_height(root: Optional[TreeNode], l: int) -> int:
            if root is None:
                return 0

            # Assign the level
            level[root.val] = l

            # Get the height
            height[root.val] = (
                max(find_height(root.left, l + 1), find_height(root.right, l + 1))
            ) + 1

            # compare the height with the max and second max
            if height[root.val] > levelMaxHeight[l]:

                levelSecondMaxHeight[l] = levelMaxHeight[l]
                levelMaxHeight[l] = height[root.val]
            elif height[root.val] > levelSecondMaxHeight[l]:
                levelSecondMaxHeight[l] = height[root.val]

            return height[root.val]

        find_height(root, 0)
        result = []
        # star iterating over queries
        for q in queries:

            # find the level of the query
            l = level[q]
            h = height[q]

            # if the height is same as max height of the level then
            # it can be possible that its the height of the deleted q node
            # so we take the 2nd max height
            if h != levelMaxHeight[l]:
                h = levelMaxHeight[l]
            else:
                h = levelSecondMaxHeight[l]

            result.append(l + h - 1)

        return result


def main():
    obj = Solution()
    root = list_to_binary_tree([5, 8, 9, 2, 1, 3, 7, 4, 6])
    queries = [3, 2, 4, 8]
    expected = [3, 2, 3, 2]
    print(obj.treeQueries(root, queries))


if __name__ == "__main__":
    main()
