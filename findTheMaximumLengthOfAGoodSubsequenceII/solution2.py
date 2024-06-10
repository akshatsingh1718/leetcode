from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil

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

    def maximumLength(self, nums: List[int], k: int) -> int:
        # create array of max length we can create from 0 -> k

        N = len(nums)
        dp = [0] * N
        # Max of dp till ith index
        mx = [0] * N

        last_index = defaultdict(int)

        # for k = 0
        for i in range(N):
            num = nums[i]
            # if already seen
            if num in last_index:
                dp[i] = dp[last_index[num]] + 1
            # if not visited num yet
            else:
                dp[i] = 1

            if i < N - 1:
                mx[i + 1] = max(mx[i], dp[i])

            last_index[num] = i

        dp2 = dp
        mx2 = mx
        for r in range(k):
            last_index = defaultdict(int)
            dp = [0] * N
            mx = [0] * N

            for i in range(N):
                num = nums[i]
                # extend
                if num in last_index:
                    dp[i] = dp[last_index[num]] + 1
                else:
                    dp[i] = 1

                # Switch
                # can i use the previous max ?
                if mx2[i] + 1 > dp[i]:
                    dp[i] = mx2[i] + 1
                if i < N - 1:
                    mx[i + 1] = max(mx[i], dp[i])

                last_index[num] = i
            print("=" * 40)
            print(f"{dp = }")
            print(f"{mx = }")

            dp2 = dp
            mx2 = mx

        return max(dp[-1], mx[-1])


def main():
    obj = Solution()
    nums = [1, 2, 1, 1, 3]
    k = 2
    output = 4

    # TS 2
    # nums = [1, 2, 3, 4, 5, 1]
    # k = 0
    # output = 2

    # TS 3
    # nums = [2, 5]
    # k = 1
    # output = 2

    # TS 4
    # nums = [28,28,29]
    # k = 2
    # output = 3

    # TS 5
    # nums = [29, 28, 28]
    # k = 2
    # output = 3

    # TS 6
    nums = [15, 6, 26, 32, 6]
    k = 1
    output = 3

    print(obj.maximumLength(nums, k))


if __name__ == "__main__":
    main()
