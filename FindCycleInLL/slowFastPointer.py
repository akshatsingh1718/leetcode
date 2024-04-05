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
    53ms
    Beats 83.83%of users with Python3
    Memory
    Details
    20.49MB
    Beats 67.71%of users with Python3

    TC : O(n) [ the fast can have multiple turns to catch the slow but appx it will be O(n)]
    SC : O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if fast_p is slow_p:
                return True

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
