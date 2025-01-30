from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil, gcd
import heapq
from heapq import heapify, heappop, heappush
import itertools as it
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
def create_adjacency_list(edges: List[tuple], directed=False):
    # When n nodes is told but graph does not have all the nodes present
    # this will prevent it from keyerror
    adjacency_list = defaultdict(lambda: [])

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []

        adjacency_list[u].append(v)
        if not directed:
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

    def turnOffK(self, n, k):

        # k must be greater than 0
        if k <= 0:
            return n

        # Do & of n with a number
        # with all set bits except
        # the k'th bit
        return n & ~(1 << (k - 1))

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        curr_xor = 0
        for num in nums:
            curr_xor ^= num

        k_upper_limit = 2**maximumBit - 1

        n = len(nums)
        res = []
        i = n - 1
        while i >= 0:

            lock_for_one = True

            # find the largest number we can form
            # curr_xor is the number we want to use for
            k = k_upper_limit
            kstr = ""
            can_start = False
            for b in range(23, -1, -1):

                # get the bth bit of curr_xor and k
                # if curr_xor bth bit is 0 and k bth bit is 0 = Cannot change to bth bit of k to 1 since k will exceed its number limit
                # if curr_xor bth bit is 0 and k bth bit is 1 = OK
                # if curr_xor bth bit is 1 and k bth bit is 0 = OK
                # if curr_xor bth bit is 1 and k bth bit is 1 = Change to zero (0)

                curr_xor_bth_bit = curr_xor & (1 << b)
                k_bth_bit = k_upper_limit & (1 << b)

                if curr_xor_bth_bit > 0:
                    can_start = True

                if not can_start:
                    continue

                if curr_xor_bth_bit == 0 and k_bth_bit == 0 and not lock_for_one:
                    # change the k bth bit to 1
                    k |= 1 << b
                    kstr += "1"
                elif curr_xor == 0 and k_bth_bit > 0:
                    kstr += "1"
                elif curr_xor > 0 and k_bth_bit == 0:
                    kstr += "0"
                else:
                    # elif curr_xor > 0 and k_bth_bit > 0:
                    # change k bth bit to zero
                    lock_for_one = False
                    kstr += "0"
            kstr = kstr.lstrip("0")
            print(kstr)
            if kstr == "":
                res.append(0)
            else:
                res.append(int(kstr, 2))
            # pop out the element from curr_xor
            curr_xor ^= nums[i]
            i -= 1

        return res


def main():
    obj = Solution()
    nums = [0, 1, 1, 3]
    maximumBit = 2
    expected = [0, 3, 2, 3]
    print(obj.getMaximumXor(nums, maximumBit))


if __name__ == "__main__":
    main()
