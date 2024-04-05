from typing import List, Optional, Dict
from sample import *

# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Runtime
        Details
        35ms
        Beats 92.96%of users with Python3
        Memory
        Details
        17.00MB
        Beats 99.32%of users with Python3
        """

        if head is None:
            return None

        nodes_dict: Dict[
            Node, Node
        ] = dict()  # (node : node) store original node data : node of copy data

        node = head

        # create blocks of list with no next and random pointers
        while node is not None:
            new_node = Node(val=node.val)
            nodes_dict[node] = new_node

            node = node.next

        # set random and next for each list items
        node = head
        while node is not None:
            new_node = nodes_dict[node]
            new_node.next = nodes_dict[node.next] if node.next is not None else None
            new_node.random = (
                nodes_dict[node.random] if node.random is not None else None
            )
            node = node.next

        return nodes_dict[head]


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
