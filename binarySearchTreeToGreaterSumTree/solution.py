from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil
from heapq import heapify, heappop, heappush

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
Problem: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/?envType=daily-question&envId=2024-06-25
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n = len(tree_nodes)
    TC: O(n) [traversal for arr] + O(n)[cum_arr_sum] + O(n * logn) [update + bisect] ~ O(n * logn)
    SC: O(n) [traversal for arr recursion stack] + O(n) [traversal for update rec stack]

    ==========================
    Algorithm:
    ==========================
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:


        def inorder_traversal(root: TreeNode):
            '''
            This will populate the arr with tree vals in sorted fashion
            '''
            nonlocal arr
            if root is None:
                return

            inorder_traversal(root.left)
            arr.append(root.val)
            inorder_traversal(root.right)

        def dfs_update_val(root: TreeNode):
            '''
            This will update the tree nodes vals in with the updated values
            '''
            nonlocal cum_arr_sum
            if root is None:
                return
            # find the next index for the root.val in arr
            # That will provide us the corresponding cum_arr_sum
            # holding the update value for the given node
            upper_bound = bisect_right_(root.val)
            # update the root.val with (upper_bound - 1) since
            # upper_bound is the next index of num which is gt root.val
            root.val = cum_arr_sum[upper_bound - 1]

            dfs_update_val(root.left)
            dfs_update_val(root.right)

        def bisect_right_(num: int):
            ''''
            Find right most index which is just greater than the num
            '''
            nonlocal arr
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] <= num:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        # arr to store the sorted numbers using inorder traversal
        arr = []


        # This will fill the array in sorted fashion
        inorder_traversal(root)

        n = len(arr)

        # cumulative sum from backwards 
        cum_arr_sum = arr.copy()
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            cum_arr_sum[i] += cum_arr_sum[i + 1]

        # update the value of all the nodes
        dfs_update_val(root)

        return root


def main():
    obj = Solution()
    root = list_to_binary_tree(
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    )
    expected = list_to_binary_tree(
        [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
    )

    output = obj.bstToGst(root)


if __name__ == "__main__":
    main()
