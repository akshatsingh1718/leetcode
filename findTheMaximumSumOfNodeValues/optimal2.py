from typing import List, Optional, Union, Dict, Tuple


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
Problem: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/submissions/1262167432/?envType=daily-question&envId=2024-05-19
Help: https://www.youtube.com/watch?v=QIiQdsVvjNw
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

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        # calculate the orig sum of all the nums
        sums = sum(nums)

        # create new array with all nums xor with k
        xor_arr = list(map( lambda x: x ^ k, nums))

        # create a new array with difference between xor array and original nums
        diff = [xor - num for (xor, num) in zip(xor_arr, nums)]

        # sort the difference array with desc order
        diff.sort(reverse=True)

        # start creating pairs and check if pairs sums inc the original sum
        n = len(diff)
        i = 0

        while i + 1 < n:
            if sums > sums + diff[i] + diff[i + 1]:
                break
            sums += diff[i] + diff[i + 1]
            i += 2

        return sums


def main():
    obj = Solution()
    nums = [1, 2, 1]
    k = 3
    edges = [[0, 1], [0, 2]]
    Output = 6

    # TS2
    nums = [2, 3]
    k = 7
    edges = [[0, 1]]
    Output = 9

    # TS3
    nums = [7, 7, 7, 7, 7, 7]
    k = 3
    edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    Output = 42

    # TS4
    nums = [24, 78, 1, 97, 44]
    k = 6
    edges = [[0, 2], [1, 2], [4, 2], [3, 4]]

    print(obj.maximumValueSum(nums, k, edges))


if __name__ == "__main__":
    main()
