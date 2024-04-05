from typing import List, Optional, Dict
from sample import *

# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    """
    Runtime
    Details
    38ms
    Beats 86.29%of users with Python3
    Memory
    Details
    17.26MB
    Beats 69.09%of users with Python3


    TC : O(n) + O(n) + O(n) ~ O(n)
    SC : O(1)
    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # add the new copy nodes in between the original list

        n = head
        while n is not None:
            new_node = Node(n.val, n.next)
            temp_next = n.next
            n.next = new_node
            n = temp_next

        # set the random pointer to the correct random nodes
        n = head
        while n is not None:
            copy_node = n.next
            copy_node.random = n.random.next if n.random is not None else None
            n = n.next.next

        # break the connection bw orig and copy linked list
        n = head
        dummy = Node()
        dummy_t = dummy

        while n is not None:
            front = n.next.next
            dummy.next = n.next
            n.next = front
            n = n.next
            dummy = dummy.next

        return dummy_t.next


def main():
    s = Solution()
    isAllPassed = True

    for i, tc in enumerate(TestCases):
        res = s.copyRandomList(tc)

        if not isListsSame(res, tc):
            print("=========================")
            print(f"Testcase Failed : {i + 1}")
            print(f"Expected: {getList(tc)}")
            print(f"GOT     : {getList(res)}")

            isAllPassed = False

    if isAllPassed:
        print(f"All testcase Passed !")


if __name__ == "__main__":
    main()
