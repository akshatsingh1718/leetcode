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
    TC: O(2^N) [recursion]
    SC: O(N)   [recursion stack]

    ==========================
    Algorithm:
    ==========================
    """

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def create_monotonic_subsequences(
            idx: int, subs: List[int], prev: int, result: List[Tuple[int]]
        ):
            nonlocal n, nums
            
            if idx == n:
                if len(subs) >= 2:
                    result.add(tuple(subs))
                return 

            if prev <= nums[idx]:
                create_monotonic_subsequences(idx=idx + 1, subs= subs + [nums[idx]], prev=nums[idx], result= result)
            
            create_monotonic_subsequences(idx=idx + 1, subs= subs, prev=prev, result= result)
        

        result = set()
        create_monotonic_subsequences(0, [], prev= float("-inf"),result=result)
        return result


def main():
    obj = Solution()

    nums = [4, 6, 7, 7]
    output = [
        [4, 6],
        [4, 6, 7],
        [4, 6, 7, 7],
        [4, 7],
        [4, 7, 7],
        [6, 7],
        [6, 7, 7],
        [7, 7],
    ]

    print(obj.findSubsequences(nums))


if __name__ == "__main__":
    main()
