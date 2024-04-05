from typing import Optional
from sample import *

class Solution:
    '''
    Time Limit Exceeded
    '''
    
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Iterate over list1
        curr1 = headA

        while curr1 != None:
            curr2 = headB
            # Iterate over list2
            while curr2 != None:
                if curr1 == curr2:
                    return curr1
                curr2 = curr2.next
            curr1 = curr1.next
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
