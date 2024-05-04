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
    TC: O(len) [for length finding] + O(len - n) [for node deletion] ~ O(2 len) [at worst len-n could be len when n = 1]
    SC: O(1)
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of linked list
        def find_ll_length(node: ListNode):
            if node is None:
                return 0

            l = 0

            while node is not None:
                l += 1
                node = node.next

            return l

        # remove the kth from the list
        length = find_ll_length(head)

        # if n is equal to length meaning remove head
        if length == n:
            return head.next

        # translate the nth from end to kth pos from starting
        k = length - n

        i = 0
        node_prv = None
        curr_node = head

        while i != k: # move until i matches k
            node_prv = curr_node
            curr_node = curr_node.next
            i += 1

        node_prv.next = curr_node.next if curr_node else None

        return head


head = ll.ListFactory.createNodes([1, 2, 3, 4, 5])
n = 1
expected = ll.ListFactory.createNodes([1, 2, 3, 5])

res = Solution().removeNthFromEnd(head, n)
ll.printList(res)
