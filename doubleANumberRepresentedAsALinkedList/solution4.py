"""
Question: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07
"""

from utils.ll import *
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    TC: O(n)
    SC: O(1)


    Cons
    ==========================
    1. It is not feasible for working when double becomes triple or any other multiplication since more than 2 could yield another carry for prv number.
    2. Inplace operation.
    """

    def doubleIt(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr is not None:

            # find out the double value
            double_value = curr.val * 2

            # if the double value is less than 10 then simple set the
            # curr value as double value
            if double_value < 10:
                curr.val = double_value
            # if double is gt 10 and prev is not none
            # meaning we should set the curr.val = ones digit of double value
            # AND also increase the prv value by 1 since the current is gt 10 so
            # it will contribute 1 as carry for prev
            elif prev is not None:

                curr.val = double_value % 10
                prev.val += 1  # carry from curr value double
            # if number is gt > 10 and prev is none meaning first node
            else:
                head = ListNode(1)  # Create head with carry of 1
                head.next = curr # set the head next value as curr
                curr.val = double_value % 10 # set the curr value as ones digit of double_value

            curr, prev = curr.next, curr

        return head


head = ListFactory.createNodes([1, 8, 9])
output = [3, 7, 8]

# TS2
head = ListFactory.createNodes([6, 8, 9])
output = [1, 3, 7, 8]

res = Solution().doubleIt(head)

printList(res)
