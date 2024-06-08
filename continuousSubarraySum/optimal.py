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
Problem: https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-06-08
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n)
    SC: O(n) [hash map]

    ==========================
    Algorithm:
    ==========================

    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr_sum = 0

        hash_map = {0: -1}

        for i, num in enumerate(nums):
            # add the num to curr_sum
            curr_sum += num
            modulo_res = curr_sum % k
            # check if the curr_sum modulo is seen already
            if hash_map.get(modulo_res, None) is not None:
                # curr_sum - Num at hash_map[curr_sum % k] == num_diff
                # num_diff will be a multiple of k
                if i - hash_map[modulo_res] >= 2:
                    return True
            else:
                hash_map[modulo_res] = i

        return False


def main():
    obj = Solution()
    nums = [23, 2, 4, 6, 7]
    k = 6
    output = True

    # TS 2
    nums = [5, 0, 0, 0]
    k = 3
    output = True

    # Ts 3
    nums = [0, 1, 0, 3, 0, 4, 0, 4, 0]
    k = 5
    output = False
    print(obj.checkSubarraySum(nums, k))


if __name__ == "__main__":
    main()
