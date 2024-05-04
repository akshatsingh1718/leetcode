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
    '''
    TC: O(len)
    SC: O(1)
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head 
        slow = head

        # make the fast pointer ahead of slow pointer by n nodes
        for _ in range(n):
            fast = fast.next

        # n is index for head (so remove head)
        if fast is None: return head.next

        # move the fast pointer along with slow pointer till fast ptr next points to none
        # because we know fast is ahead slow by n nodes which means when fast reached to end
        # the slow will be n nodes behind it and other way to say is slow is behind n nodes from the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # change the slow.next to point to the next to next and leaving the in between node
        slow.next = slow.next.next

        return head


head = ll.ListFactory.createNodes([1, 2, 3, 4, 5])
n = 1
expected = ll.ListFactory.createNodes([1, 2, 3, 5])

res = Solution().removeNthFromEnd(head, n)
ll.printList(res)
