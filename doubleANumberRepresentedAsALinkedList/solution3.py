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
    '''
    TC: O(n) [reverse list] + O(n) [list loop]
    SC: O(1) [no extra space used]
    '''
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # revers list
        prev = None
        curr = head
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next

        # iterate through from left to right
        new_list = None
        node = prev
        carry = 0

        # loop over list
        while node is not None:
            double_val = (node.val * 2) + carry
            carry = double_val // 10
            new_list = ListNode(val=double_val % 10, next=new_list)
            node = node.next

        if carry > 0:
            new_list = ListNode(val=carry, next=new_list)
        return new_list


head = ListFactory.createNodes([9, 9, 9])
output = [1, 9, 9, 8]

head = ListFactory.createNodes([1, 8, 9])
output = [3, 7, 8]

res = Solution().doubleIt(head)

printList(res)
