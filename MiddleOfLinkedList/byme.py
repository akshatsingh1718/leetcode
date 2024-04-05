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
    51ms
    Beats 5.70%of users with Python3
    Memory
    Details
    16.00MB
    Beats 99.11%of users with Python3


    Runtime
    Details
    37ms
    Beats 70.25%of users with Python3
    Memory
    Details
    16.26MB
    Beats 64.22%of users with Python3
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        # find the len of the ll
        next_node = head

        while next_node is not None:
            next_node = next_node.next
            n += 1

        middle_idx = n // 2

        # get the middle of the list
        next_node = head
        while middle_idx > 0:
            next_node = next_node.next
            middle_idx -= 1

        return next_node


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
