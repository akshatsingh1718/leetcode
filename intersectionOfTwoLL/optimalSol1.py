from typing import Optional
from sample import *

class Solution:
    """
    Runtime
    Details
    130ms
    Beats 73.00%of users with Python3
    Memory
    Details
    31.53MB
    Beats 67.02%of users with Python3
    """

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        curr1, curr2 = headA, headB

        # find length of list1 and list2
        len1, len2 = 0, 0
        while curr1 != None or curr2 != None:
            if curr1 != None:
                len1 += 1
                curr1 = curr1.next

            if curr2 != None:
                len2 += 1
                curr2 = curr2.next

        # find longest list
        longest = headA
        shortest = headB
        if len2 > len1:
            longest = headB
            shortest = headA

        # move the longest length to the offset difference
        offset = abs(len1 - len2)

        while offset > 0:
            longest = longest.next
            offset -= 1

        # iterate over both list's simultaneously
        while longest != None or shortest != None:
            if longest is shortest:
                return longest

            longest = longest.next
            shortest = shortest.next

        return None


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
