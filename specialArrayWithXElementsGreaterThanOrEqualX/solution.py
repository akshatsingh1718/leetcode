from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque


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
Problem: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/?envType=daily-question&envId=2024-05-27
Help: https://www.youtube.com/watch?v=pYqncHGUqh4
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(nlogn) [sorting] + O(n * logn) [for loop + binary search]
    SC: O(n) [if creating a different array for storing sorted array]

    ==========================
    Algorithm:
    ==========================
    1. sort the array.
    2. move the x from 0 -> len(nums) as the possible values can only lie between (0, len(nums))
    3. Find the lower bound in sorted nums for value x and check if from the length of [lower_bound -> len(nums)] is equal to the x.
    """

    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def lower_bound(num: int):
            nonlocal nums, n
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] >= num:
                    high = mid - 1
                else:
                    low = mid + 1

            return low

        for i in range(n + 1):

            idx = lower_bound(i)
            if n - idx == i:
                return i

        return -1
    

def main():
    obj = Solution()
    nums = [0, 4, 3, 0, 4]  # 0, 0, 3, 4, 4
    output = 3

    # TS 2
    # nums = [0,0]
    # output= -1

    # TS 3
    nums = [3, 5]
    output = 2

    print(obj.specialArray(nums))


if __name__ == "__main__":
    main()
