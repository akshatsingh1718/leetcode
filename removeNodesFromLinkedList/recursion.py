from utils.ll import *
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    SC: O(n) [iterate over lists recursively]
    TC: O(n) [stack space]
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        # get the next greater value node or get none if end found
        next_greater_node = self.removeNodes(head.next)  # None | ListNode

        # duplicate the head as node
        node = head
        # Assume that the current node will point next to next_greater_value node
        node.next = next_greater_node

        # If next_greater_node is none then return the current node
        # OR
        # if current node value is greater than next greater node value it means
        # we should remove the next_greater_node from the result as farther elements
        # should have only values which are smaller than the current node
        if next_greater_node is None or node.val >= next_greater_node.val:
            return node
        # Else delete the current node from the result
        return next_greater_node


head = ListFactory.createNodes([5, 2, 13, 3, 8])
res = Solution().removeNodes(head)
printList(res)
