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
Problem: https://leetcode.com/problems/find-common-characters/submissions/1278143310/?envType=daily-question&envId=2024-06-05
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
    TC: O(k * (n - 1) * a) ~ O(k * n * k) ~ O(k^2 * n)
    SC: O(k)

    ==========================
    Algorithm:
    ==========================
    1. Iterate over all the characters of words[0].
    2. Maintain a frequency of the character and the frequency should be less than or equal to the frequency in other words such that it should account for the duplicates frequency as well.
    3. if there is sufficient frequency in all the list then add that char to the result.
    """

    def commonChars(self, words: List[str]) -> List[str]:

        if len(words) == 1:
            return list(words[0])

        res = []
        counter = defaultdict(int)

        for word_0 in words[0]:
            # check this many times in list
            counter[word_0] += 1

            found = True
            for word in words[1:]:
                temp_ctr = 0

                for char in word:
                    if char == word_0:
                        temp_ctr += 1

                if temp_ctr < counter[word_0]:  # freq not matched
                    found = False
                    break

            if not found:
                continue
            else:
                res.append(word_0)

        return res


def main():
    obj = Solution()
    words = ["bella", "label", "roller"]
    output = ["e", "l", "l"]

    # TS 2
    words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    output = []
    print(obj.commonChars(words))


if __name__ == "__main__":
    main()
