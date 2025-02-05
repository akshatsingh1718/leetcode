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
    Version 2

    A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

    Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

    However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

    A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

    Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.


    Input: words[] = ["cb", "cba", "a", "bc"]
    Output: true
    Explanation: You need to return "cab" as the correct order of letters in the alien dictionary.
    Input: words[] = ["ab", "aa", "a"]
    Output: ""
    Explanation: You need to return "" because "aa" is lexicographically larger than "a", making the order invalid.
    Input: words[] = ["ab", "cd", "ef", "ad"]
    Output: ""
    Explanation: You need to return "" because "a" appears before "e", but then "e" appears before "a", which contradicts the ordering rules.
    """

    def findOrder(self, alien_dict: List[str]):
        # topological order
        adj = defaultdict(set)
        indegree = dict()
        for word in alien_dict:
            for ch in word:
                indegree[ch] = 0
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

            # print(f"{prev_word=}; {curr_word=} {j=}")

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
                # if j got out of bounds meaning upto j chars both prev and curr
                # words are equal. And the curr word should not have a length gt prev
                # print("j got oob")
                if len(prev_word) > len(curr_word):
                    return ""
                continue

            # The (jth char of curr_word) > (jth char of prev_word)
            curr_char = curr_word[j]
            prev_char = prev_word[j]

            # check if the connection already exist
            # if curr_char in adj[prev_char]:
            #     continue

            # make a connection between pc -> cc
            adj[prev_char].add(curr_char)

            indegree[curr_char] += 1

            # find the 0 indegree chars
            # print(adj)
            # print(indegree)
            # print("===============")
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

        # check if a cycle is detected
        if len(indegree) != len(res):
            return ""
        # print(indegree)
        # print(res)

        return res


def main():
    obj = Solution()
    # TS 1
    alien_dict = ["cb", "cba", "a", "bc"]
    output = "cab"

    # TS 2
    # alien_dict = ["ab", "aa", "a"]
    # output = ""

    # TS 3
    alien_dict = ["aa", "aab", "ab", "b", "babbb"]
    output = ""
    # aa aab ab b babbb
    print("Ans->", obj.findOrder(alien_dict))


if __name__ == "__main__":
    main()
