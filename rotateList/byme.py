from typing import Optional
from sample import *


class Solution:
    """
    Runtime
    Details
    45ms
    Beats 69.61%of users with Python3
    Memory
    Details
    16.42MB
    Beats 11.62%of users with Python3
    """

    # def get_kth_node_And(self, head: Optional[ListNode], k: int):

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        length = 0
        last_node = None
        last_kth_node = None

        # find length of list
        curr = head
        while curr is not None:
            last_node = curr
            curr = curr.next
            length += 1

        # get new k = k % len(list)
        new_k = k % length

        if new_k == 0:
            return head

        # find the last (k + 1)th element
        last_kth_node_idx = length - new_k
        curr = head
        i = 0
        while curr is not None and i < last_kth_node_idx:
            last_kth_node = curr
            curr = curr.next
            i += 1

        # set the (k+1)th element next to NULL
        new_head = last_kth_node.next
        last_kth_node.next = None

        # set the last element next to the first element of the list
        last_node.next = head
        return new_head

    def rotateRight1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Runtime
        Details
        45ms
        Beats 69.61%of users with Python3
        Memory
        Details
        16.34MB
        Beats 49.30%of users with Python3
        '''
        if head is None:
            return head

        length = 0

        # find length of list
        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1
        
        # convert idx to true length
        length += 1
        # set last node next to head
        curr.next = head

        # get new k = k % len(list)
        new_k = k % length

        # find the last (k)th element
        new_k = length - new_k
        while new_k > 0:
            new_k -= 1
            curr = curr.next

        head = curr.next
        curr.next = None

        return head


if __name__ == "__main__":
    sol = Solution()

    # Input = TestCases[0]
    # res = sol.rotateRight(*Input)
    # print(printList(res))
    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        Input = TestCases[i]
        res = sol.rotateRight1(*Input)
        if not isListsSame(res, Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(printList(Expected[i]))
            print("--> Got")
            print(printList(res))
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
