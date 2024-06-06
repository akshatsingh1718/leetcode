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
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        n = len(s)

        def dfs(start: int, end: int, curr_res: List[str]):
            nonlocal n, s, wordDict, result

            if end == n + 1:
                if len(curr_res) > 0 and start == n:
                    result.append(" ".join(curr_res))
                return

            if s[start:end] in wordDict:
                dfs(end, end + 1, curr_res=curr_res + [s[start:end]])

            dfs(start, end + 1, curr_res=curr_res)

        dfs(0, 1, [])
        return result


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
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        n = len(s)
        wordDict_set = set(wordDict)

        def dfs(start: int, curr_res: str):
            nonlocal n, s, wordDict_set, result

            if start == n:
                result.append(curr_res.lstrip())
                return

            for end in range(start + 1, n + 1):
                if s[start:end] in wordDict_set:
                    dfs(end, curr_res= curr_res + " " + s[start:end])

        dfs(0, "")
        return result


def main():
    obj = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    output = ["cats and dog", "cat sand dog"]
    print(obj.wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
