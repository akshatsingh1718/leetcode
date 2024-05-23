from typing import List, Optional, Union, Dict, Tuple
from bisect import bisect, bisect_left, bisect_right
from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isListsSame(list1: ListNode, list2: ListNode):
    head1, head2 = list1, list2
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def printList(head: ListNode):
    lstr: str = ""
    while head is not None:
        lstr += str(head.val) + ", "
        head = head.next

    print(lstr)


# Graph utils
def create_adjacency_list(edges: List[tuple]):
    adjacency_list = {}

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list


# List utils


def list_to_ll(vector: List[int]):
    prv_node = None
    for i, val in enumerate(vector[::-1]):
        prv_node = ListNode(val, prv_node)
    return prv_node


# Tree Utils
def list_to_binary_tree(lst: List[int]):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current_node = queue.pop(0)

        if lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)

        i += 1

    return root


###################################################
################# Code Goes Here ##################
###################################################
"""
Problem:
Help:
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def addOperators(self, num: str, target: int) -> List[str]:

        n = len(num)
        result = []

        def find(idx: int, curr_val: int, prv_val: int, expr: str):
            nonlocal result, n, target, num
            if idx == n:
                if curr_val == target:
                    result.append(expr)
                return

            for i in range(idx, n):
                # ignore leading zeros
                # return and not continue because any number after 0 will
                # be invalid without any in between operand
                if i > idx and num[idx] == "0":
                    return

                next_int = int(num[idx : i + 1])

                # if the insertion is for the first time
                # we dont want to add any operand first only num first
                if idx == 0:
                    find(
                        i + 1,
                        curr_val=next_int,
                        prv_val=next_int,
                        expr=str(next_int),
                    )
                else:

                    for opr in ["+", "-", "*"]:
                        if opr == "+":
                            find(
                                i + 1,
                                curr_val=curr_val + next_int,
                                prv_val=next_int,
                                expr=f"{expr}+{next_int}",
                            )
                        elif opr == "-":
                            find(
                                i + 1,
                                curr_val=curr_val - next_int,
                                prv_val=-next_int,
                                expr=f"{expr}-{next_int}",
                            )
                        elif opr == "*":
                            find(
                                i + 1,
                                curr_val=curr_val - prv_val + (prv_val * next_int),
                                prv_val=(prv_val * next_int),
                                expr=f"{expr}*{next_int}",
                            )

        find(0, 0, 0, "")
        return result


def main():
    obj = Solution()
    num = "123"
    target = 6
    output = ["1*2*3", "1+2+3"]

    # TS2
    # num = "105"
    # target = 5
    # output = ["1*0+5", "10-5"]

    # TS 3
    # num = "3456237490"
    # target = 9191
    # output = []

    # TS 4
    num = "105"
    target = 5
    output = ["1*0+5", "10-5"]

    # TS 5
    # num = "00"
    # target = 0
    # output = ["0*0", "0+0", "0-0"]

    # TS 6
    # num = "123456789"
    # target = 45

    res = Solution().addOperators(num, target)
    print(res)


if __name__ == "__main__":
    main()
