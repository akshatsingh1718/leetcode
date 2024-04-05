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
    684ms
    Beats 5.04%of users with Python3
    Memory
    Details
    20.56MB
    Beats 46.82%of users with Python3

    TC : O(n)
    SC : O(n) [storing nodes]
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = []

        while node is not None:
            if node in visited:
                return True
            visited.append(node)
            node = node.next

        return False


def main():
    s = Solution()
    isAllPassed = True

    for i, (tc, ex) in enumerate(TestCases):
        res = s.hasCycle(tc)

        if res != ex:
            print("=========================")
            print(f"Testcase Failed : {i + 1}")
            print(f"Expected: {ex}")
            print(f"GOT     : {res}")

            isAllPassed = False

    if isAllPassed:
        print(f"All testcase Passed !")


if __name__ == "__main__":
    main()
