from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict


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
Problem: https://leetcode.com/problems/word-break-ii/solutions/5203992/simple-readable-python-solution-my-first-post/?envType=daily-question&envId=2024-05-25
Help: https://www.youtube.com/watch?v=QgLKdluDo08
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2^n)
    SC: O(2^n)

    ==========================
    Algorithm:
    ==========================
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        word_set = set(wordDict)
        cache = dict()

        def solve(t):
            nonlocal n, word_set
            result = []
            if not t:
                return [""]
            
            if cache.get(t, None) is None:

                # Iterate over word and take its subsequences
                # from starting till n
                for idx, _ in enumerate(t):
                    # get the subsequences
                    prefix = t[: idx + 1]
                    # check if subsequence in present in the wordset or not
                    if prefix in word_set: # only going ahead if we made it to the set of words
                        # check for other sub seqs after the selected sequences
                        suffixes = solve(t[idx + 1 :])
                        # if there are not subsequences made after the current seq then
                        # it means that we are unable to make the seq after the current seq
                        # and it should not be appended to the result
                        for suffix in suffixes:
                            # there are seq made later on then append it with the current prefix seq
                            if suffix:
                                result.append(f"{prefix} {suffix}")
                            # if the suffix are empty then add only suffix 
                            # this can also mean that we are at the last index 
                            else:
                                result.append(prefix)
                cache[t] = result
            return cache[t]

        return solve(s)

def main():
    obj = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    output = ["cats and dog", "cat sand dog"]
    print(obj.wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
