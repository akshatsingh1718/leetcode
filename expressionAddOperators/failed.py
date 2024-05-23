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

        def find(
            idx: int,
            curr_val: int,
            prv_val: int,
            curr_expr: str,
            zero_ahead = bool
        ):
            nonlocal num, target, result

            if idx == n:
                # if curr_expr == "1*0+5":

                if curr_val == target:
                    if eval(curr_expr) != target:
                        print(f"Error at :{curr_expr} | {curr_val=}")

                        # print(curr_expr, curr_val)
                    result.append(curr_expr)
                return

            curr_num = int(num[idx])

            # if idx == 0:
            #     find(
            #         idx=idx + 1,
            #         curr_val=curr_num,
            #         prv_val=curr_num,
            #         curr_expr=num[idx],
            #     )
            #     return

            for opr in ["+", "-", "*"]:

                if opr == "+":  # Add
                    if False and curr_expr == "1+2*34":
                        print("====================")
                        print(f"{curr_num=}")
                        print(f"{curr_val=}")
                        print(f"{prv_val=}")
                        print(f"{curr_expr=}")
                        print(f"New curr val = {curr_val + curr_num}")
                        print(f"New prev val = {curr_num}")
                        print(f"New expr val = {curr_expr}+{num[idx]}")
                        print("====================")
                    find(
                        idx=idx + 1,  # start
                        curr_val=curr_val + curr_num,  # path
                        prv_val=curr_num,
                        curr_expr=f"{curr_expr}+{num[idx]}",  #
                        zero_ahead = curr_num == 0
                    )

                if opr == "-":  # Subtract
                    find(
                        idx=idx + 1,  # start
                        curr_val=curr_val - curr_num,  # path
                        prv_val=-curr_num,
                        curr_expr=f"{curr_expr}-{num[idx]}",  #
                        zero_ahead = curr_num == 0

                    )

                if opr == "*":  # Multiplication
                    sign = prv_val // abs(prv_val)
                    # if curr_expr == "1+2*34+5-6":
                    #     print("====================")
                    #     print(f"{curr_num=}")
                    #     print(f"{curr_val=}")
                    #     print(f"{prv_val=}")
                    #     print(f"{curr_expr=}")
                    #     print(f"New curr val = {(curr_val - prv_val) + prv_val * curr_num}")
                    #     print(f"New prev val = {prv_val * curr_num}")
                    #     print(f"New expr val = {curr_expr}*{num[idx]}")
                    #     print("====================")
                    find(
                        idx=idx + 1,  # start
                        curr_val=(curr_val - prv_val) + prv_val * curr_num,  # path
                        # curr_val=(curr_val // prv_val) + prv_val * curr_num,  # path
                        prv_val=prv_val * curr_num,
                        curr_expr=f"{curr_expr}*{num[idx]}",  #
                        # zero_ahead = prv_val * curr_num == 0
                        zero_ahead = curr_num == 0
                    )

            if not zero_ahead:
                # add nothing
                # if curr_expr == "3+456*2":
                # if curr_expr == "123-45-6*7":
                sign = prv_val // abs(prv_val)
                # if curr_expr == "123-4":
                if curr_expr == "1+2*3":
                    print("====================")
                    print(f"{curr_num=}")
                    print(f"{curr_val=}")
                    print(f"{prv_val=}")
                    print(f"{curr_expr=}")
                    print(f"New curr val = {(curr_val - prv_val) + (prv_val * 10) + sign * curr_num}")
                    print(f"New prev val = {prv_val * 10 + sign * curr_num}")
                    print(f"New expr val = {curr_expr}{num[idx]}")
                    print("====================")

                    # ====================
                    # curr_num=4
                    # curr_val=7
                    # prv_val=6
                    # curr_expr='1+2*3'
                    # New curr val = 65
                    # New prev val = 64
                    # New expr val = 1+2*34
                    # ====================
                    # This will fail here since prv value will be carrying 6 and when new number 4
                    # will come to concat at end and 3 will become 34 then we are negating whole
                    # 2 * 3 from curr_val and then adding (prv * 10) + curr_num which is giving us 65
                    # instead we want to mul 2 * 34 it is mul ((2 * 3) * 10) * 4
                find(
                    idx=idx + 1,  # start
                    # curr_val=(curr_val - prv_val) + (prv_val * 10) + curr_num,  # path
                    curr_val= (curr_val - prv_val) + (prv_val * 10) + sign * curr_num,  # path

                    prv_val=  prv_val * 10 + sign * curr_num, # prv_val * 10 + curr_num,
                    curr_expr=f"{curr_expr}{num[idx]}",  #
                    zero_ahead = zero_ahead
                )

        result = []
        find(idx=1, curr_val=int(num[0]), prv_val=int(num[0]), curr_expr=num[0], zero_ahead= num[0] == "0")

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

    # TS 5
    num = "00"
    target = 0
    output = ["0*0","0+0","0-0"]

    # TS 6
    num = "123456789"
    target = 45

    res = Solution().addOperators(num, target)
    # print(res)

if __name__ == "__main__":
    main()
