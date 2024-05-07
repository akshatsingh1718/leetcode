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
    TC: O(n) [recursion]
    SC: O(n) [recursion stack space]
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # new list to store the double of ll result
        new_list = None

        def dfs(head: ListNode, carry: int) -> ListNode:
            nonlocal new_list

            if head is None:
                return 0

            # get the carry from the right number double
            carry = dfs(head.next, carry)

            # calculate the current number double
            node_val_double = head.val * 2
            # add the carry passed from the right number double
            node_val_double += carry

            # extract the ones place of the number after doubling
            # to set the value of the current node
            new_carry = node_val_double // 10
            # extract the carry to be send to the next recursion call in waiting
            new_node_val = node_val_double % 10

            # the current head will become the next of the
            # the current node since we are iterating backwards
            new_list = ListNode(val=new_node_val, next=new_list)

            # return the carry of the current node double value
            return new_carry

        # if the carry is returned for the first number in the linked list
        # then create node for that as well
        carry = dfs(head, 0)
        if carry > 0:
            new_list = ListNode(val=carry, next=new_list)

        return new_list


class Solution:  # Compact version of above code
    """
    TC: O(n) [recursion]
    SC: O(n) [recursion stack space]
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # new list to store the double of ll result
        new_list = None

        def dfs(head: ListNode) -> ListNode:
            nonlocal new_list

            if head is None:
                return 0

            node_val_double = (head.val * 2) + dfs(head.next)

            new_list = ListNode(val=node_val_double % 10, next=new_list)

            # return the carry of the current node double value
            return node_val_double // 10

        # if the carry is returned for the first number in the linked list
        # then create node for that as well
        carry = dfs(head)
        if carry > 0:
            new_list = ListNode(val=carry, next=new_list)

        return new_list
