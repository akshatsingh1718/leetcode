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
    k = len(words[0])
    n = len(words)
    a = avg word length
    TC: O(n * k)
    SC: O(k) [hashmap] ~ O(1) [since at most 26 chars]

    ==========================
    Algorithm:
    ==========================
    1. Find the freq of each char in words[0].
    2. iterate over all the words and get the min frequency  from each words.
    3. then one more for loop for adding the no of frequency of character that are found in all the words to add in res.
    """

    def commonChars(self, words: List[str]) -> List[str]:

        if len(words) == 1:
            return list(words[0])

        res = []
        # get the freq of 1st word
        counter = Counter(words[0])

        for word in words:
            temp_counter = Counter(word)

            for c in counter:
                counter[c] = min(counter[c], temp_counter[c])


        for c in counter:
            for i in range(counter[c]):
                res.append(c)

        return res


def main():
    obj = Solution()
    words = ["bella", "label", "roller"]
    output = ["e", "l", "l"]

    # TS 2
    # words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    # output = []
    print(obj.commonChars(words))


if __name__ == "__main__":
    main()
