from typing import Optional
import sys

sys.path.insert(0, "utils")
import ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = ListNode()
        prvNode = head

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                prvNode.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                prvNode.next = ListNode(val=list2.val)
                list2 = list2.next

            prvNode = prvNode.next

        while list1 is not None:
            prvNode.next = ListNode(val=list1.val)
            prvNode = prvNode.next
            list1 = list1.next

        while list2 is not None:
            prvNode.next = ListNode(val=list2.val)
            prvNode = prvNode.next
            list2 = list2.next

        return head.next


class Solution2:
    """
    This solution is just the better code written version of above solution
    """

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = ListNode()
        prvNode = head

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                prvNode.next = list1
                list1 = list1.next
            else:
                prvNode.next = list2
                list2 = list2.next

            prvNode = prvNode.next

        if list1 or list2:
            prvNode.next = list1 if list1 else list2

        return head.next


list1 = ListFactory.createNodes([1, 2, 4])
list2 = ListFactory.createNodes([1, 3, 4])
expected = ListFactory.createNodes([1, 1, 2, 3, 4, 4])

res = Solution().mergeTwoLists(list1, list2)
printList(res)
