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
        cache = dict()

        def find(
            idx: int,
            curr_val: int,
            curr_expr: str,
            result: List[str],
            has_non_zero_ahead: bool,
        ):
            nonlocal num, target, cache
            if idx == n:
                if curr_val == target:
                # if eval(curr_expr) == target:
                    # result.add(curr_expr)
                    return curr_expr
                    # return True
                return ""

            # '+', '-', and/or '*'
            if cache.get((idx, curr_val)) is None:
                # Add
                add_expr = curr_expr + f"+{num[idx]}" if curr_expr else str(num[idx])
                add_res = find(
                    idx + 1,
                    eval(add_expr),
                    add_expr,
                    result,
                    has_non_zero_ahead=num[idx] != "0",
                )
                
                # Subtract
                sub_expr = curr_expr + f"-{num[idx]}" if curr_expr else str(num[idx])
                sub_res = find(
                    idx + 1,
                    eval(sub_expr),
                    sub_expr,
                    result,
                    has_non_zero_ahead=num[idx] != "0",
                )
                # Multiplication
                mul_expr = curr_expr + f"*{num[idx]}" if curr_expr else str(num[idx])
                mul_res = find(
                    idx + 1,
                    eval(mul_expr),
                    mul_expr,
                    result,
                    has_non_zero_ahead=num[idx] != "0",
                )
                # add nothing
                nothing_res = ""
                if has_non_zero_ahead:
                    nothing_expr = curr_expr + str(num[idx])
                    nothing_res =find(
                        idx + 1,
                        eval(nothing_expr),
                        nothing_expr,
                        result,
                        has_non_zero_ahead=has_non_zero_ahead,
                    )


                cache[(idx, curr_val)] = []
                for res in [add_res, sub_res, mul_res, nothing_res]:
                    if res:
                        print(">", res)
                        cache[(idx, curr_val)].append(res)
                

            return cache[(idx, curr_val)]

        result = set()
        return find(0, 0, "", result, False)


def main():
    obj = Solution()
    num = "123"
    target = 6
    output = ["1*2*3", "1+2+3"]

    # num = "105"
    # target = 5
    # output = ["1*0+5", "10-5"]
    print(Solution().addOperators(num, target))


if __name__ == "__main__":
    main()
