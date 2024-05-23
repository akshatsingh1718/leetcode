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
Problem: https://leetcode.com/problems/house-robber/description/
Help:
"""


class SolutionSlow:
    """
    ==========================
    Time and space complexity:
    ==========================
    (TLE)
    TC: O(2 ^ N)
    SC: O(N) [max recursion stack]

    ==========================
    Algorithm:
    ==========================
    """

    def rob(self, nums: List[int]) -> int:

        def robbery(idx: int):
            nonlocal nums

            if idx < 0:
                return 0

            max_robbery = max(nums[idx] + robbery(idx - 2), robbery(idx - 1))
            return max_robbery

        return robbery(len(nums) - 1)



class Solution: # optimized using dp
    """
    ==========================
    Time and space complexity:
    ==========================
    (TLE)
    TC: O(N) [only visiting one time for a house]
    SC: O(N) [max recursion stack] + O(N) [memo] ~ O(N)

    ==========================
    Algorithm:
    ==========================
    """

    def rob(self, nums: List[int]) -> int:

        memo = dict()

        def robbery(idx: int):
            nonlocal nums, memo
            if idx in memo:
                return memo[idx]
            if idx < 0:
                return 0

            memo[idx] = max(nums[idx] + robbery(idx - 2), robbery(idx - 1))
            return memo[idx]

        return robbery(len(nums) - 1)

def main():
    obj = Solution()
    # TS 1
    nums = [1, 2, 3, 1]
    output = 4

    # TS 2
    nums = [2, 7, 9, 3, 1]
    output = 12

    # TS 3
    nums = [1, 2]
    output = 2

    # TS 4
    # nums = [1]
    # output = 1

    # TS 5
    # nums = [1,2,1,1]
    # output = 3

    print(Solution().rob(nums))


if __name__ == "__main__":
    main()
