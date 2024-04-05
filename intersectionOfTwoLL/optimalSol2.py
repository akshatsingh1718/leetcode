from typing import Optional
from sample import *


class Solution:
    """
    Runtime
    Details
    123ms
    Beats 87.86%of users with Python3
    Memory
    Details
    31.46MB
    Beats 87.03%of users with Python3
    """

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        curr1, curr2 = headA, headB

        while curr1 != curr2:
            curr1 = headB if (curr1 is None) else curr1.next
            curr2 = headA if (curr2 is None) else curr2.next

        return curr1


if __name__ == "__main__":
    sol = Solution()

    # Input = TestCases[0][0], TestCases[0][1]
    # Expected = TestCases[0][2]
    # res = sol.getIntersectionNode(*Input)
    # print(res is Expected)

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        Input = TestCases[i][0], TestCases[i][1]
        Expected = TestCases[i][2]
        res = sol.getIntersectionNode(*Input)
        if res is not Expected:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(printList(Expected))
            print("--> Got")
            print(printList(res))
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
