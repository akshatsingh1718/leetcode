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
Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters/solutions/5200011/easy-solutions-dp-python/?envType=daily-question&envId=2024-05-24
Help: https://www.youtube.com/watch?v=Vn2eno9OIpc
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    l = len(words[i])
    TC: O(2^n) [subsets] * O(l)
    SC: O(26) [freq] ~ O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:

        def find_score(word: str, freq: Dict):
            nonlocal score

            copy_freq = freq.copy()
            curr_score = 0
            for char in word:
                if freq.get(char, 0) == 0:
                    freq = copy_freq
                    curr_score = 0
                    break
                curr_score += score[ord(char) - ord("a")]
                freq[char] -= 1
            return curr_score

        words_len = len(words)
        max_score = 0
        for i in range(1, 1 << words_len):
            curr_score = 0
            freq = Counter(letters)
            for j in range(words_len):
                if i & (1 << j):
                    curr_score += find_score(words[j], freq)
            max_score = max(max_score, curr_score)

        return max_score


class Solution2:
    """
    ==========================
    Time and space complexity:
    ==========================
    l = len(words[i])
    TC: O(2^n) [subsets] * O(l)
    SC: O(n) [recursion stack] * O(26) [freq] ~ O(n)

    ==========================
    Algorithm:
    ==========================
    """

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:

        def find_score(idx: int, curr_score: int, freq: Dict):
            nonlocal score, max_score

            if idx == words_len:
                max_score = max(max_score, curr_score)
                return

            prv_freq = freq.copy()
            temp_score = 0
            # check if we can take the word
            for ch in words[idx]:
                if freq.get(ch, 0) == 0:
                    freq = prv_freq
                    temp_score = 0
                    break

                freq[ch] -= 1
                temp_score += score[ord(ch) - ord("a")]

            else:
                find_score(idx + 1, curr_score + temp_score, freq)

            find_score(idx + 1, curr_score, prv_freq)

        words_len = len(words)
        max_score = 0

        find_score(0, 0, Counter(letters))
        return max_score


def main():
    obj = Solution2()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [
        1,
        0,
        9,
        5,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    output = 23

    # TS 2
    words = ["xxxz", "ax", "bx", "cx"]
    letters = ["z", "a", "b", "c", "x", "x", "x"]
    score = [
        4,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        0,
        10,
    ]
    output = 27

    # TS 3
    words = ["leetcode"]
    letters = ["l", "e", "t", "c", "o", "d"]
    score = [
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    output = 0

    # TS 4
    words = ["ac", "abd", "db", "ba", "dddd", "bca"]
    letters = ["a", "a", "a", "b", "b", "b", "c", "c", "d", "d", "d", "d"]
    score = [
        6,
        4,
        4,
        7,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    output = 62

    print(obj.maxScoreWords(words, letters, score))


if __name__ == "__main__":
    main()
