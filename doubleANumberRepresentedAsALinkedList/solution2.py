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
    TC: O(n) [fill stack] + o(n) [empty stack] ~ o(n)
    SC: O(n) [stack space]
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []

        node = head
        while node is not None:
            stack.append(node)
            node = node.next

        new_list = None
        carry = 0

        while stack:
            node = stack.pop()
            double_val = (node.val * 2) + carry
            carry = double_val // 10
            new_val = double_val % 10
            new_list = ListNode(val=new_val, next=new_list)

        if carry > 0:
            new_list = ListNode(val=carry, next=new_list)

        return new_list
