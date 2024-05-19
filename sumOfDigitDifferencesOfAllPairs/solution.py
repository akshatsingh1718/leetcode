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
Problem: https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/submissions/1262457347/
Help: https://www.youtube.com/watch?v=fhVU5K4n_-Y
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    k = len(nums[0]) [length of number]
    n = len(nums) [numbers in nums]
    TC: O(k * (n + k))
    SC: O(n * k)

    ==========================
    Algorithm:
    ==========================
    """

    def sumDigitDifferences(self, nums: List[int]) -> int:
        # find the freq of each digit places
        n = len(nums)
        k = len(str(nums[0]))

        i = 0
        diffs = 0
        while i < k:
            # get the ith place nums in collections counter
            freq = Counter([str(x)[i] for x in nums])  # TC: O(n)

            for no, no_freq in freq.items():
                diffs += no_freq * (n - no_freq)

            i += 1

        return diffs // 2


def main():
    obj = Solution()

    nums = [13, 23, 12]
    output = 4

    print(Solution().sumDigitDifferences(nums))


if __name__ == "__main__":
    main()
