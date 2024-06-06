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
Problem: https://leetcode.com/problems/hand-of-straights/?envType=daily-question&envId=2024-06-06
Help: https://www.youtube.com/watch?v=lpVhzcdiHMs
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(nlogn) [adding elements to map] + O(n) [for loop]
    SC: O(n) [hash map]

    ==========================
    Algorithm:
    ==========================
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # if there is not enough elements to make group
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)

        for num, occ in freq.items():
            
            # exhaust all the occurences of the num
            while freq[num] != 0:
                # decrement the freq
                freq[num] -= 1
                # move till the groupsize from current num
                for i in range(1, groupSize):
                    # if the next numbers have freq of 0 then we cannot make a grp
                    # and return false
                    if freq[num + i] == 0:
                        return False
                    # if the grp can be made then decrement the freq of next num as 
                    # it is consider used now
                    freq[num + i] -= 1

        return True


def main():
    obj = Solution()
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    output = True

    # TS 2

    # hand = [1,2,3,4,5]
    # groupSize = 4
    # output= False

    # TS 3
    # hand = [1]
    # groupSize = 1
    # output = True

    # TS 4
    # hand = [2, 1]
    # groupSize = 2
    # output = True

    print(obj.isNStraightHand(hand, groupSize))


if __name__ == "__main__":
    main()
