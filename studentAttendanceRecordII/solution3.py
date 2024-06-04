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
Problem:
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n * 2 * 3) => (n)[n length string] * [2 * 3](2 times for A and 3 times for late)
    We can have 2 values for absent where 1 is permissible and 2 will not
    Same for late, 2 consecutive late and 3rd will be a rule violation.
    SC: O(n * 2 * 3) [memo]

    ==========================
    Algorithm:
    ==========================
    """
    def checkRecord(self, n: int) -> int:
        M = 1000000007
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def dfs(left: int, absent_count: int, late_count: int):

            if absent_count >= 2 or late_count >= 3:
                return 0
            if left == 0:  # string created successfully
                return 1
            
            if memo[left][absent_count][late_count] != -1:
                return memo[left][absent_count][late_count]


            # present today
            P = dfs(left - 1, absent_count=absent_count, late_count=0) % M
            # absent today
            A = dfs(left - 1, absent_count=absent_count + 1, late_count=0) % M
            # late today
            L = dfs(left - 1, absent_count=absent_count, late_count=late_count + 1) % M

            memo[left][absent_count][late_count] = ((L + P)  % M + A) % M

            return memo[left][absent_count][late_count]

        return dfs(n, 0, 0)


def main():
    obj = Solution()
    n = 1
    # TS 2
    # n = 10101
    # output = 183236316
    print(Solution().checkRecord(n))


if __name__ == "__main__":
    main()
