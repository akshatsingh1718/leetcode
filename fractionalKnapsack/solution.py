from typing import List, Optional, Union, Dict, Tuple
from bisect import bisect, bisect_left, bisect_right
from collections import Counter


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


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(nlogn) [sorting] + O(n) [while loop]
    SC: O(n) [ratios]

    ==========================
    Algorithm:
    ==========================
    """

    def fractionalknapsack(self, w: int, arr: List[Item], n: int):

        # find the max value / weight meaning which is the best
        # value per unit weight. Whose single weight is giving the max val
        ratios = [(idx, i.value / i.weight) for idx, i in enumerate(arr)]
        # sort in desc order of val/weight ratio
        ratios.sort(key=lambda x: x[1], reverse=True)

        knapsack = 0

        ratio_i = 0
        while ratio_i < n and w > 0:
            item_idx = ratios[ratio_i][0]

            if w - arr[item_idx].weight > 0:
                w -= arr[item_idx].weight
                knapsack += arr[item_idx].value
            else:
                knapsack += ratios[ratio_i][1] * w
                w -= w
            ratio_i += 1
        return knapsack


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(nlogn) [sorting] + O(n) [while loop]
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def fractionalknapsack(self, w: int, arr: List[Item], n: int):

        arr.sort(key=lambda x: x.value / x.weight, reverse=True)

        knapsack = 0
        i = 0
        while i < n and w > 0:
            weight_used = arr[i].weight if (w - arr[i].weight > 0) else w
            knapsack += (arr[i].value / arr[i].weight) * weight_used
            w -= weight_used
            i += 1
        return knapsack


def main():
    obj = Solution()
    # TS 1
    n = 3
    w = 50
    value = [60, 100, 120]
    weight = [10, 20, 30]
    output = 240

    # TS 2
    n = 2
    w = 50
    value = [60, 100]
    weight = [10, 20]
    output = 160

    arr = [Item(val, w) for val, w in zip(value, weight)]
    print(Solution().fractionalknapsack(w, arr, n))


if __name__ == "__main__":
    main()
