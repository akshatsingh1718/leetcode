from typing import List, Optional, Union, Dict, Tuple
from bisect import bisect, bisect_left, bisect_right
from collections import Counter


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
Problem: https://leetcode.com/problems/palindrome-partitioning/submissions/1264658505/?envType=daily-question&envId=2024-05-22
Help: 
    1. https://www.youtube.com/watch?v=WBgsABoClE0
    2. https://www.youtube.com/watch?v=jHR7KUAAEzw
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2^n)
    SC: O(n) [recursion stack]

    ==========================
    Algorithm:
    ==========================
    1. For the partition we are starting with index 0.
    2. Move from left to right and check if their partition is palindrome or not. Example from idx to n check which
        partition is palindrome.
        s = "aab"
        At 1st stage idx = 0 and move i from idx -> n and check which partition is creating a palindrome. Lets suppose
        current i == 0 it means s[0 -> 0] = "a" and it is palindrome. Now move down into recursion and make the next starting
        point as `idx =i + 1` and from that pos start we will make palindrome. 

        When i = 1, s[idx -> i] or s[0 -> 1] = "aa" which is also a palindrome.
        When i = 2, s[idx -> i] or s[0 -> 2] = "aab" which is not a palindrome.

        The above will be the different branches created by for loops
    """

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        n = len(s)
        result = []

        def part(idx: int, curr_res: List[str]):
            nonlocal s, n
            if idx == n:
                result.append(curr_res[:])
                return

            for i in range(idx, n):
                if is_palindrome(s, idx, i):
                    curr_res.append(s[idx : i + 1])
                    part(idx=i + 1, curr_res=curr_res)
                    curr_res.pop()

        part(idx=0, curr_res=[])
        return result


def main():
    obj = Solution()
    s = "aab"
    # s = "aabb"
    print(obj.partition(s))


if __name__ == "__main__":
    main()
