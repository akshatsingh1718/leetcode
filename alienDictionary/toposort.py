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

    Problem Statement: Given a sorted dictionary of an alien language having N words and k starting alphabets of a standard dictionary. Find the order of characters in the alien language.

    Note: Many orders may be possible for a particular test case, thus you may return any valid order.

    Examples:

    Example 1:
    Input: N = 5, K = 4
    dict = {"baa","abcd","abca","cab","cad"}
    Output: b d a c
    Explanation:
    We will analyze every consecutive pair to find out the order of the characters.
    The pair “baa” and “abcd” suggests ‘b’ appears before ‘a’ in the alien dictionary.
    The pair “abcd” and “abca” suggests ‘d’ appears before ‘a’ in the alien dictionary.
    The pair “abca” and “cab” suggests ‘a’ appears before ‘c’ in the alien dictionary.
    The pair “cab” and “cad” suggests ‘b’ appears before ‘d’ in the alien dictionary.
    So, [‘b’, ‘d’, ‘a’, ‘c’] is a valid ordering.

    Example 2:
    Input: N = 3, K = 3
    dict = {"caa","aaa","aab"}
    Output: c a b
    Explanation: Similarly, if we analyze the consecutive pair
    for this example, we will figure out [‘c’, ‘a’, ‘b’] is
    a valid ordering.
    """

    def findOrder(self, alien_dict: List[str]):
        # topological order
        adj = defaultdict(set)
        indegree = dict()
        n = len(alien_dict)

        for i in range(1, n):
            # ignore the first j chars which are same in both
            # ith and i-1th idx
            curr_word = alien_dict[i]
            prev_word = alien_dict[i - 1]

            j = 0
            while (
                j < min(len(curr_word), len(prev_word)) and curr_word[j] == prev_word[j]
            ):
                j += 1

            # if j is out of bounds then we cannot why curr_word is bigger then prev_word
            if j == min(len(curr_word), len(prev_word)):
                """
                Example 1:
                curr_word: abcd
                prev_word: abcd

                Example 2:
                curr_word: abcd
                prev_word: abcde
                """
                continue

            # The (jth char of curr_word) > (jth char of prev_word)
            curr_char = curr_word[j]
            prev_char = prev_word[j]
            # check if previously curr_char was present before prev_char
            if prev_char in adj[curr_char]:
                return ""
            adj[prev_char].add(curr_char)

            if indegree.get(curr_char, 0) == 0:
                indegree[curr_char] = 0
            if indegree.get(prev_char, 0) == 0:
                indegree[prev_char] = 0
            indegree[curr_char] += 1

        # find the 0 indegree chars
        print(adj)
        print(indegree)
        res = ""
        nodes = deque([])
        for char, deg in indegree.items():
            if deg == 0:
                nodes.append(char)

        while nodes:
            node = nodes.popleft()
            res += node

            # move to its neighbors
            for neig in adj[node]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    nodes.append(neig)

        return res


def main():
    obj = Solution()
    # TS 1
    alien_dict = ["cb", "cba", "a", "bc"]
    output = "cab"

    # TS 2
    alien_dict = ["ab", "aa", "a"]
    output = ""
    print(obj.findOrder(alien_dict))


if __name__ == "__main__":
    main()
