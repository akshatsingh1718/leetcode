from typing import Optional
from sample import *


class Solution:
    """
    Runtime
    Details
    136ms
    Beats 62.41%of users with Python3
    Memory
    Details
    32.59MB
    Beats 8.64%of users with Python3
    """

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        visited_nodes = dict()

        # Add all nodes to visited_nodes dict
        curr1 = headA
        while curr1 != None:
            item = visited_nodes.get(curr1)
            visited_nodes[curr1] = 1
            curr1 = curr1.next

        # Iterate over list2
        curr2 = headB
        while curr2 != None:
            item = visited_nodes.get(curr2)

            if item is not None:
                return curr2  # found node

            visited_nodes[curr2] = 1
            curr2 = curr2.next

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
