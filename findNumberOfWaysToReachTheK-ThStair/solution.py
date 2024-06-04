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
    TLE (See below sol for acceptance)
    ==========================
    Time and space complexity:
    ==========================
    TC: O(log2(k))
    Let's suppose we want to reach at k = x.
    And we are starting at i = 1.
    If we only take the jump operation to reach at x
    1 + 2**0, 2 + 2**1, ...... till reaching at x
    for simplification we neglect 1 at each stage
    Let us assume it will take 2**c to reach at x
    then, 2**c = k or c = log2(k)

    SC: O(log2(k)) [recursion depth]

    ==========================
    Algorithm:
    ==========================
    """

    def waysToReachStair(self, k: int) -> int:

        def findWays(i: int, jump: int, last_is_op1: bool):
            nonlocal k

            # if we fount the k but still explore more ways to reach k
            if i == k:
                # if the last was operation 1
                #   OR
                # we are at the 0th staircase and cannot go back more
                # Then we can only use operation 2
                if last_is_op1 == True or i == 0:
                    return 1 + findWays(i + 2**jump, jump + 1, last_is_op1=False)
                # otherwise we are free to use operation 1 and 2
                else:
                    return (
                        1
                        + findWays(i - 1, jump, last_is_op1=True)
                        + findWays(i + 2**jump, jump + 1, last_is_op1=False)
                    )

            # i gt k and we cannot use operation 1 then there is no
            # way we can go back to k since we will only move above because of op2
            if i > k and last_is_op1:
                return 0
            # or if we are more than k + 1 then there will be no chance we are getting
            # back to k since op1 can only decrement i by 1 and will get back to k + 1 then
            # surely we will be doing op2 again so there will be no point of return
            if i - 1 > k:
                return 0

            # if we are reached to our goal k then check again for same
            if i == 0 or last_is_op1 == True:
                return findWays(i + 2**jump, jump + 1, last_is_op1=False)
            else:
                return findWays(i - 1, jump, True) + findWays(
                    i + 2**jump, jump + 1, False
                )

        return findWays(1, 0, last_is_op1=False)


class Solution:  # concise way of solution
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(log2(k))
    SC: O(log2(k))

    ==========================
    Algorithm:
    ==========================
    """

    def waysToReachStair(self, k: int) -> int:

        cache = dict()

        def findWays(i: int, jump: int, last_is_op1: bool):
            nonlocal k, cache

            if (i > k and last_is_op1) or (i - 1 > k):
            # if i - 1 > k:
                return 0

            if cache.get((i, jump, last_is_op1), None) is None:
                # determine if we reached at k
                ways = 1 if i == k else 0
                # jump operation can always be performed
                ways += findWays(i + 2**jump, jump + 1, last_is_op1=False)
                # move back operation can only be done when the last operation
                # is not the same and we are > 0 staircase
                if last_is_op1 == False or i > 0:
                    ways += findWays(i - 1, jump, True)

                cache[(i, jump, last_is_op1)] = ways

            return cache[(i, jump, last_is_op1)]

        return findWays(1, 0, last_is_op1=False)


def main():
    obj = Solution()

    k = 0
    output = 2

    # TS 2
    k = 5
    print(obj.waysToReachStair(k))


if __name__ == "__main__":
    main()
