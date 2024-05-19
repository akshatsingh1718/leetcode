from typing import List, Optional, Union, Dict, Tuple
from bisect import bisect


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
    n = len(nums)
    q = len(queries)
    TC: O(n) [for prefix array] + O(q)
    SC: O(n) [for prefix array]

    ==========================
    Algorithm:
    ==========================
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # make the index for which the index and its prv cannot make special array
        pre = [0 for _ in range(n)]

        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]

        res = []

        for start, end in queries:
            if pre[end] - pre[start] == 0:
                res.append(True)
            else:
                res.append(False)
        return res


def main():
    obj = Solution()

    nums = [3, 4, 1, 2, 6]
    queries = [[0, 4]]

    # TS2
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]

    # TS3
    # nums = [1,4]
    # queries = [[0, 1]]

    # TS4
    # nums = [1, 3, 5, 6, 7, 8, 10, 12]
    # queries = [[2, 5]]
    print(obj.isArraySpecial(nums, queries))


if __name__ == "__main__":
    main()
