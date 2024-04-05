from typing import List, Optional
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
        46ms
        Beats 39.58%of users with Python3
        Memory
        Details
        17.05MB
        Beats 99.32%of users with Python3

        TC : O(n) [creating simple list] + O(n) [setting randoms]
        SC : O(n) [nodes list] + O(n) [nodes_dict] ~ O(n)
        """

        if head is None:
            return None

        nodes_list: List[Node] = []  # store nodes of new copy list
        nodes_dict = dict()  # (node : idx) store original node data

        prv_node = None
        curr_node = head
        node = head

        # create copy list with random as nulls
        i = 0
        while node is not None:
            curr_node = Node(node.val, next=None, random=None)
            nodes_dict[node] = i
            # add the node to nodes list to later access using index
            nodes_list.append(curr_node)

            if prv_node is not None:
                prv_node.next = curr_node

            prv_node = curr_node
            node = node.next
            i += 1

        # set the random pointers
        node = head
        i = 0
        while node is not None:
            nodes_list[i].random = (
                nodes_list[nodes_dict[node.random]] if node.random is not None else None
            )
            i += 1
            node = node.next

        return nodes_list[0]


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
