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
Problem: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/submissions/1433177138/?envType=daily-question&envId=2024-10-25
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) [create set] + O(n * 100) [n folders * remove "/" till empty] ~ O(n)
    SC: O(n) [folder set]

    ==========================
    Algorithm:
    ==========================
    """

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []  # accepted candidates
        folder_set = set(folder)

        for f in folder:

            prefix = f

            # remove the last folder of the prefix and check if its
            # present in the folder set or not
            # Eg. set = {"/a", "/a/c", "/a/b/c"}
            # when at "/a/b/c" we will first remove the /c to get "/a/b/" which
            # is not present in the set then we move again to remove the "/b"
            # and get "/a" which is present in our solution
            while prefix:
                # find the last occurrence of /
                idx = prefix.rfind("/")

                prefix = prefix[:idx]

                if prefix in folder_set:
                    # subfolder is found
                    break
            else:
                # if the prefix value gets to the empty str = ""
                # it means we didnt find f to be subfolder
                res.append(f)

        return res


def main():
    obj = Solution()
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    expected = ["/a", "/c/d", "/c/f"]
    print(obj.removeSubfolders(folder))


if __name__ == "__main__":
    main()