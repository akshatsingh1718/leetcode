from typing import Optional
from sample import *
import numpy as np


class Solution:
    '''
    Runtime
    Details
    44ms
    Beats 69.00%of users with Python3
    Memory
    Details
    17.77MB
    Beats 96.70%of users with Python3
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prv = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prv
            prv = curr
            curr = next_node
        return prv


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        res = sol.reverseList(TestCases[i])
        if not isListsSame(res, Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(printList(Expected[i]))
            print("--> Got")
            print(printList(res))
            print("--> Given")
            print(printList(TestCases[i]))
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
