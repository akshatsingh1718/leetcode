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


class Solution: # improvement over sol 1
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) + O(n) ~ O(n)
    SC: O(n) [frequency]

    ==========================
    Algorithm: (binary search)
    ==========================
    1. create an array `counts` of length n.
    2. Traverse over nums and set the value counts[nums[i]] += 1 as we need to set the count of elements for those indexes and if the nums[i] > len(counts) then add 1 to the counts[-1].
    3. Transform the counts array to cumulative array by moving from right to left since we need how many elements are greater than the current index of the `count` array.
    4. if the index matches the count it means that index value has elements counts in array nums greater than or equal to.
    """

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        # frequency of each nums
        counts = [0 for _ in range(n)] # O(n) space
        
        # set the freq of nums in count
        for num in nums: # O(n) loop
            if num == 0: continue
            counts[min(num - 1, n - 1)] += 1

        # find the cumulative sum from right to left
        for i in range(n-1, -1, -1): # O(n) loop
            counts[i] += counts[i+1] if i + 1 < n  else 0
            if i + 1 == counts[i]:
                return i + 1

        return -1


def main():
    obj = Solution()
    nums = [0, 4, 3, 0, 4]  # 0, 0, 3, 4, 4
    output = 3

    # TS 2
    # nums = [0,0]
    # output= -1

    # TS 3
    # nums = [3, 5]
    # output = 2

    # TS 4
    # nums = [3,6,7,7,0]
    # output = -1

    print(obj.specialArray(nums))


if __name__ == "__main__":
    main()
