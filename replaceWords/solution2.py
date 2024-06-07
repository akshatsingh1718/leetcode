from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache

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
def create_adjacency_list(edges: List[tuple]):
    adjacency_list = {}

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
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
    m = len(dictionary)
    TC: O(n) [while loop]
    SC: O(m) [set dictionary]

    ==========================
    Algorithm:
    ==========================
    """

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        i = 0
        res = ""
        n = len(sentence)
        dictionary = set(dictionary)
        while i < n:

            # 1. check in dict if the current visited partial word is in the dict.
            starting_i = i
            while i < n and sentence[i] != " ":
                if sentence[starting_i : i + 1] in dictionary:
                    break
                i += 1

            # 2. add the new word
            new_word = sentence[starting_i : i + 1].strip()
            res += new_word if len(res) == 0 else f" {new_word}"

            # 3. skip all the remaining characters
            while i < n and sentence[i] != " ":
                i += 1

            i += 1

        return res


def main():
    obj = Solution()
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    output = "the cat was rat by the bat"

    # TS 2
    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    output = "the catt was rat by the bat"
    print(obj.replaceWords(dictionary, sentence))


if __name__ == "__main__":
    main()
