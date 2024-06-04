from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque

import sys

# Check the current recursion limit
current_limit = sys.getrecursionlimit()
print(f"Current recursion limit: {current_limit}")

# Set a new recursion limit
new_limit = 10**5  # Set this to the desired limit
sys.setrecursionlimit(new_limit)


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


# class Solution:
#     """
#     ==========================
#     Time and space complexity:
#     ==========================
#     TC:
#     SC:

#     ==========================
#     Algorithm:
#     ==========================
#     """

#     def checkRecord(self, n: int) -> int:
#         result = 0

#         def dfs(idx: int, s: str, last_two_L: int, last_one_A: int):
#             nonlocal n, result
#             if idx == n:
#                 print(s)
#                 result += 1
#                 return

#             dfs(idx + 1, s + "p", last_two_L=0, last_one_A=0)  # present today
#             if last_one_A < 1:
#                 dfs(idx + 1, s + "A", last_two_L=0, last_one_A=1)  # absent today
#             if last_two_L <= 2:
#                 dfs(
#                     idx + 1, s + "A", last_two_L=last_two_L + 1, last_one_A=0
#                 )  # late today

#         dfs(0, "", 0, 0)
#         return result


# class Solution:
#     """
#     ==========================
#     Time and space complexity:
#     ==========================
#     TC:
#     SC:
#     ==========================
#     Algorithm:
#     ==========================
#     """

#     def checkRecord(self, n: int) -> int:

#         def dfs(idx: int, last_two_L: int, last_one_A: int):
#             nonlocal n

#             if idx == n:
#                 return 1

#             result = 0

#             result += dfs(idx + 1, last_two_L=0, last_one_A=0)  # present today
#             if last_one_A < 1:
#                 result += dfs(idx + 1, last_two_L=0, last_one_A=1)  # absent today
#             if last_two_L <= 2:
#                 result += dfs(
#                     idx + 1, last_two_L=last_two_L + 1, last_one_A=0
#                 )  # late today
#             return result

#         return dfs(0, 0, 0)


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

    def checkRecord(self, n: int) -> int:
        cache = dict()

        def dfs(s: str):
            nonlocal n
            if len(s) == n:
                return 1

            result = 0
            if cache.get(s, None) is None:

                result += dfs(s + "p")  # present today
                # if last_one_A < 1:
                if len(s) < 1 or s[-1] != "a":
                    result += dfs(s + "a")  # absent today
                # if last_two_L <= 2:
                if len(s) < 2 or (s[-1] != s[-2] != "l"):
                    result += dfs(s + "l")  # late today
                cache[s] = result
            else:
                result = cache[s]

            return result

        return dfs("")


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

    def checkRecord(self, n: int) -> int:
        cache = dict()

        def dfs(idx: int, s: List[str]):
            nonlocal n
            if idx == n:
                return 1

            result = 0
            if cache.get("".join(s), None) is None:

                popped_v1 = None
                # present today
                s.append("p")
                if len(s) > 2:
                    popped_v1 = s.pop(0)
                result += dfs(idx + 1, s)
                if popped_v1:
                    s.insert(0, popped_v1)
                try:
                    s.pop()
                except Exception as e:
                    print(s)
                    sys.exit()

                # Absent today
                popped_v2 = None
                if len(s) < 1 or s[-1] != "a":
                    s.append("a")
                    if len(s) > 2:
                        popped_v2 = s.pop(0)
                    result += dfs(idx + 1, s)
                    if popped_v2:
                        s.insert(0, popped_v2)
                    s.pop()

                # late today
                popped_v3 = None
                if len(s) < 2 or (s[-1] != s[-2] != "l"):
                    s.append("l")
                    if len(s) > 2:
                        s.pop(0)
                    result += dfs(idx + 1, s)
                    if popped_v3:
                        s.insert(0, popped_v3)
                    s.pop()

                cache["".join(s)] = result
            else:
                result = cache["".join(s)]

            return result

        return dfs(0, [])


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

    def checkRecord(self, n: int) -> int:
        cache = dict()

        def dfs(idx: int, s: List[str], already_absent: bool):
            nonlocal n, cache
            if idx == n:
                print(s)

                return 1

            result = 0

            if cache.get((idx, already_absent), None) is None:
                if len(s) > 2:
                    s = s[-2:]

                for next_day in ["p", "l"] + (["a"] if not already_absent else []):
                    s_prv = s.copy()
                    s.append(next_day)

                    # present day
                    if s[-1] == "p":
                        result += dfs(idx + 1, s, already_absent)

                    # Absent today
                    elif s[-1] == "a":
                        result += dfs(idx + 1, s, already_absent=True)

                    # late today
                    elif s[-1] == "l":
                        if len(s) < 3: # 2 can be possible
                            result += dfs(idx + 1, s, already_absent)
                        else:
                            if s[-3] != s[-2]:
                                result += dfs(idx + 1, s, already_absent)
                    s = s_prv
                cache[(idx, already_absent)] = result
            else:
                result = cache[(idx, already_absent)]

            return result

        return dfs(0, [], False)


def main():
    obj = Solution()
    n = 5
    output = 8

    # TS 2
    # n = 10101
    # output = 183236316
    print(Solution().checkRecord(n))


if __name__ == "__main__":
    main()
