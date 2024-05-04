"""
Question: https://leetcode.com/problems/add-two-numbers/

"""

from typing import Optional
import sys
from collections import deque

sys.path.insert(0, "utils")
import ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    len1 = len(l1)
    len2 = len(l2)
    TC: O( max(len1, len2) ) [traversal over the longest linked list]
    SC: O( max(len1, len2) + 1 ) [store the sum of both nums + extra 1 for carry if it is there at the end]
        99 + 99 = 198 (len1= 2; len2= 2; len(res) =3)
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # iterate over head1 and head2
        head1 = l1
        head2 = l2

        head = ListNode()
        res = head

        carry = 0
        while head1 is not None or head2 is not None:
            # if head1 and head2 is not none then take their values
            # else assign 0 if one list is smaller than other list
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0

            sum_temp = val1 + val2 + carry

            # Store the result in node
            res.next = ListNode(val=sum_temp % 10)
            res = res.next

            # find out the carry
            carry = sum_temp // 10

            # move on to the next node
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        # if carry bit is still there then add it to the linked list
        if carry == 1:
            res.next = ListNode(val=1)
            res = res.next

        return head.next


l1 = ll.ListFactory.createNodes([2, 4, 9])
l2 = ll.ListFactory.createNodes([5, 6, 4, 9])
expected = ll.ListFactory.createNodes([7, 0, 4, 0, 1])

res = Solution().addTwoNumbers(l1, l2)
ll.printList(res)
