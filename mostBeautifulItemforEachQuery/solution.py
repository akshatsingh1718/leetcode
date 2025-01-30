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

    def _find_lower_price_idx(self, price: int, items: List[List[int]]) -> int:
        low = 0
        high = len(items) - 1
        while low <= high:

            mid = low + (high - low) // 2

            curr_p, curr_b = items[mid]
            if curr_p == price:
                return mid

            elif curr_p > price:
                high = mid - 1
            else:  # curr_p < price
                low = mid + 1
        # print("min ", low, len(items) - 1)
        # print(f"{low=} {high=}")
        return low

    def _find_beauty(
        self, price_beauty_list: List[List[int]], target_price: int
    ) -> int:
        # Binary search setup
        left, right = 0, len(price_beauty_list) - 1
        closest_idx = -1

        while left <= right:
            mid = (left + right) // 2
            price, beauty = price_beauty_list[mid]

            if price == target_price:
                return beauty  # Exact match found
            elif price < target_price:
                closest_idx = mid  # Keep track of the closest lower price index
                left = mid + 1
            else:
                right = mid - 1

        # If no exact match, return beauty of closest lower price if it exists
        if closest_idx != -1:
            return price_beauty_list[closest_idx][1]
        else:
            return 0  # No price <= target found

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        # sort the items on the basis of price
        items.sort(key=lambda x: (x[0], -x[1]))  # price, beauty
        n = len(items)
        max_beauty = items[0][1]

        # set the max beauty for each prices
        for i in range(1, n):
            # print(f"{[items[i]]=}, {max_beauty=}")
            if items[i][1] > max_beauty:
                max_beauty = items[i][1]
            elif items[i][1] < max_beauty:
                items[i][1] = max_beauty

        max_loot: List[int] = []
        # print(items)

        # loop over queries and find the lower bound of each number
        for j in range(len(queries)):

            # get the idx from binary search
            # print("======================")
            # idx = self._find_lower_price_idx(queries[j], items)
            # # print(queries[j], f" TO {idx=}")
            # # print(items[idx][1])
            # while idx >= 0:
            #     if items[idx][0] >= queries[j]:
            #         idx -= 1
            #     else:
            #         break

            # print(idx)

            beauty = self._find_beauty(items, queries[j])
            # max_loot.append(items[idx][1])
            max_loot.append(beauty)

        return max_loot


def main():
    obj = Solution()
    items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    queries = [1, 2, 3, 4, 5, 6]
    expected = [2, 4, 5, 5, 6, 6]

    # TS 2
    items = [[1, 2], [1, 2], [1, 3], [1, 4]]
    queries = [1]
    expected = [4]
    print(obj.maximumBeauty(items, queries))


if __name__ == "__main__":
    main()
