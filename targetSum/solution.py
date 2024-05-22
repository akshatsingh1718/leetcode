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
Problem:
Help:
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

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = dict()

        def findWays(nums: List[int], target: int, idx: int, curr_sum: int):
            nonlocal cache
            if idx == len(nums):
                if curr_sum == target:
                    return 1
                return 0

            ways = 0
            if cache.get((idx, curr_sum)) is None:
                ways += findWays(
                    nums, target, curr_sum=curr_sum + nums[idx], idx=idx + 1
                )
                ways += findWays(
                    nums, target, curr_sum=curr_sum - nums[idx], idx=idx + 1
                )

                cache[(idx, curr_sum)] = ways

            return cache[(idx, curr_sum)]

        return findWays(nums, target, 0, 0)


def main():
    obj = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    output = 5
    print(Solution().findTargetSumWays(nums, target))


if __name__ == "__main__":
    main()
