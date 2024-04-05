from typing import List, Optional
from sample import *

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    Runtime
    Details
    37ms
    Beats 70.25%of users with Python3
    Memory
    Details
    16.20MB
    Beats 64.22%of users with Python3
    
    TC = O(n/2)
    SC = O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - Using two turtles slow and fast
        - slow will inc by 1 and fast will inc by 2
        - If fast is none or fast.next is none then our slow turtle is on the middle element
        _____________________________________________________________________________________

        - if the question asks for the 1st element if the list if of even no then
        1. store the prv of the slow turtle
        2. Or, stop when fast turtle is at the 2nd last node
        """

        slow_t = head
        fast_t = head

        # while fast_t is not None and fast_t.next is not None:
        while fast_t and fast_t.next:
            slow_t = slow_t.next
            fast_t = fast_t.next.next

        return slow_t


def main():
    s = Solution()
    isAllPassed = True

    for i, (tc, ex) in enumerate(TestCases):
        res = s.middleNode(tc)

        if isListsSame(res, ex) == False:
            print("=========================")
            print(f"Testcase Failed : {i + 1}")
            print(f"Expected: {printList(ex)}")
            print(f"GOT     : {printList(res)}")

            isAllPassed = False

    if isAllPassed:
        print(f"All testcase Passed !")


if __name__ == "__main__":
    main()
