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

    def _is_prime(self, num: int):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def _binary_search(self, arr: List[int], target: int) -> int:
        # arr is sorted primes array
        # target is the num we want to find the less than prime from primes
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] >= target:
                # if the prime we are looking at is gte the target
                # then we want to lower it
                high = mid - 1
            else:
                low = mid + 1

        return high

    def primeSubOperation(self, nums: List[int]) -> bool:
        # Create list of all the primes from 1 - 1000
        primes = [i for i in range(2, 1001) if self._is_prime(i)]
        print(primes)

        # loop over nums and check if a negation using prime can
        # make the nums strictly sorted
        for i in range(len(nums)):
            # get the index of the prime less than nums[i]
            idx = self._binary_search(primes, nums[i])
            p = primes[idx] if idx >= 0 else 0

            # check if we can subtract the num and it is still fine
            # then we subtract
            print(f"{p=} {idx=} {nums[i]=}")
            if i == 0 or nums[i - 1] < nums[i] - p or nums[i - 1] < nums[i]:
                nums[i] -= p
            # if subtraction is messing up the order and we have already sorted
            # i-1 and ith then leave it as it is
            else:
                return False
        print(nums)
        return True


def main():
    obj = Solution()
    nums = [4, 9, 6, 10]
    expected = True

    # TS 2
    # nums = [5, 8, 3]
    # expected = False

    # TS 3
    # nums = [6, 8, 11, 12]
    # expected = True

    # TS 4
    # nums = [998, 2]
    # expected = True

    # TS 5
    # nums = [2, 2]
    # expected = False

    print(obj.primeSubOperation(nums))


if __name__ == "__main__":
    main()
