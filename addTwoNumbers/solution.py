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

    TC: O(l1) + O(l2) + O(max(l1, l2)) ~ O(3 n)
    SC: O(l1) + O(l2)
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1 = deque()
        list2 = deque()

        # iterate over head1
        head1 = l1
        while head1 is not None:
            list1.append(head1.val)
            head1 = head1.next

        # iterate over head2
        head2 = l2
        while head2 is not None:
            list2.append(head2.val)
            head2 = head2.next

        carry = 0
        head = ListNode()
        res = head

        # index of lists for iteration
        i = 0

        # start iteration over list1 and list2 for summation
        while i < len(list1) and i < len(list2):
            # sum of ith indexes of both the lists + carry
            sum_temp = list1[i] + list2[i] + carry

            # Store the result in node
            res.next = ListNode(val=sum_temp % 10)
            res = res.next

            # check for carry bit
            if sum_temp <= 9:
                carry = 0
            else:
                carry = 1

            i += 1

        # if list1 is bigger than list2 then take the rest of the nums
        while i < len(list1):
            sum_temp = list1[i] + carry
            res.next = ListNode(val=sum_temp % 10)
            res = res.next

            if sum_temp <= 9:
                carry = 0
            else:
                carry = 1

            i += 1

        # if list2 is bigger than list1 then take the rest of the nums
        while i < len(list2):
            sum_temp = list2[i] + carry
            res.next = ListNode(val=sum_temp % 10)
            res = res.next

            if sum_temp <= 9:
                carry = 0
            else:
                carry = 1
            # print(sum_temp % 10, carry)

            i += 1

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
