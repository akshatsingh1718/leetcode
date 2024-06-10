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
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        n = len(skills)
        k = k if k <= n else n

        # if k == n
        if k == n:
            # find max
            max_skill = -1
            max_skill_idx = -1
            for i, num in enumerate(skills):
                if num > max_skill:
                    max_skill = num
                    max_skill_idx = i

            return max_skill_idx

        # if k < n
        curr_max= skills[0]
        curr_max_idx = 0
        count = 0
        for i in range(1, n):
            if curr_max > skills[i]:
                count += 1
            else:
                count = 1
                curr_max = skills[i]
                curr_max_idx = i

            if count == k:
                return curr_max_idx

        return curr_max_idx





def main():
    obj = Solution()
    skills = [4,2,6,3,9]
    k = 2
    output= 2

    # Ts 2
    # skills = [2,5,4]
    # k = 3
    # Output: 1

    # TS 3
    # skills =[16,4,7,17]
    # k = 562084119

    # TS 4
    # skills = [11,13]
    # k = 164383266
    # output = 1

    # TS 5
    # skills = [4,8,9,7]
    # k = 717834084
    # output = 2
    print(obj.findWinningPlayer(skills, k))

if __name__ == "__main__":
    main()
