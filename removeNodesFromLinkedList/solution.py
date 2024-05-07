from utils.ll import *
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    SC: O(n)
    TC: O(n)
    '''
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack: List[ListNode] = []
        node = head

        while node is not None:

            while len(stack) > 0 and stack[-1].val < node.val:
                stack.pop()

            # till here node should be the greatest value
            stack.append(node)
            node = node.next

        node = ListNode()
        head = node
        # create list from stack
        while len(stack) > 0:
            node.next = stack.pop(0)
            node = node.next

        return head.next


head = ListFactory.createNodes([5, 2, 13, 3, 8])
res = Solution().removeNodes(head)
printList(res)
