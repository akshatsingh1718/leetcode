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
    l = avg len of string
    TC: O(n * l) [create trie] + O(n * l) [check in trie]
    SC: O(n * l) [l nodes in trie * n is depth of path]

    ==========================
    Algorithm:
    ==========================
    """

    class Trie:
        def __init__(self):
            self.children = dict()
            self.is_end_of_folder = False

    def __init__(self):
        self.root = self.Trie()

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # Add all the folders to trie
        for f in folder:

            folders = f.split("/")
            curr_node = self.root

            for folder_name in folders:

                if folder_name == "":
                    continue

                # if we havent started creating a node with the letter
                # then create tha node
                if folder_name not in curr_node.children:
                    curr_node.children[folder_name] = self.Trie()
                # move to the child of the node we just created or if we have
                # already the child then its all good we are at the right stage
                # of node
                curr_node = curr_node.children[folder_name]

            # the last folder will have end of folder as true
            curr_node.is_end_of_folder = True

        # move over all the folders and check if their is a path
        # same as its starting and not ending (meaning its still left to explore) and it will be our subfolder
        res = []

        for f in folder:

            curr_node = self.root
            folders = f.split("/")
            for i, folder_name in enumerate(folders):
                if folder_name == "":
                    continue
                next_node = curr_node.children[folder_name]

                if next_node.is_end_of_folder and i != len(folders) - 1:
                    break
                curr_node = next_node
            else:
                # if the for loop is fully ran and we didnt break out of it
                # then we can append this as out parent folder
                res.append(f)

        return res


def main():
    obj = Solution()
    # folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    # expected = ["/a", "/c/d", "/c/f"]

    # TS 2
    folder = ["/a", "/a/b/c", "/a/b"]
    expected = ["/a"]

    # TS 3
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]

    print(obj.removeSubfolders(folder))


if __name__ == "__main__":
    main()
