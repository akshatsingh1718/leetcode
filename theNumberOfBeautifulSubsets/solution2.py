from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict


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
Problem: https://leetcode.com/problems/the-number-of-beautiful-subsets/submissions/1265601270/?envType=daily-question&envId=2024-05-23
Help: https://www.youtube.com/watch?v=Dle_SpjHTio
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2^N) [two choices of include and exclude at each stage]
    SC: O(N) [hashmap]

    ==========================
    Algorithm:
    ==========================
    Likewise when we create subsets we ask if the num needs to be added or not we
    add one more condition of num - k and num + k is present in map or not
    """

    def _beautifulSubsets(self, nums: List[int], k: int) -> int:

        n = len(nums)

        def subsets(idx, not_allowed: Dict):
            nonlocal nums, k

            if idx == n:
                return 1

            num = nums[idx]
            include = 0
            # check num +- k in the map as they are the only ones
            # which can give k by adding current num with (current_num +- k)
            if not_allowed[num - k] == 0 and not_allowed[num + k] == 0:
                # +1 and not = 1 since duplicate can be there and if we got same number 
                # multiple times and we backtrack to the last duplicate we will be marking as = 0
                # which is wrong since above backtracks will also have not_allowed[num] = 0 and 
                # code will fail for duplicates
                not_allowed[num] += 1 
                include = subsets(idx + 1, not_allowed=not_allowed)
                not_allowed[num] -= 1

            exclude = subsets(idx + 1, not_allowed=not_allowed)
            print(not_allowed)
            return exclude + include

        return subsets(0, defaultdict(int)) - 1


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(2^N)
    SC: O(N) [hashset]

    ==========================
    Algorithm:
    ==========================
    Likewise when we create subsets we ask if the num needs to be added or not we
    add one more condition of num - k and num + k is present in map or not

    - To encounter the hashset problem of adding and popping out for duplicated discussed in
    above solution we can use already_have for duplicated
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        n = len(nums)

        def subsets(idx, not_allowed: Set[int]):
            nonlocal nums, k

            if idx == n:
                return 1

            num = nums[idx]
            include = 0
            # check num +- k in the map as they are the only ones
            # which can give k by adding current num with (current_num +- k)
            if (num - k) not in not_allowed and (num + k) not in not_allowed:
                already_have = num in not_allowed
                not_allowed.add(num)
                include = subsets(idx + 1, not_allowed=not_allowed)
                if not already_have:
                    not_allowed.discard(num)

            exclude = subsets(idx + 1, not_allowed=not_allowed)
            return exclude + include

        return subsets(0, set()) - 1


def main():
    obj = Solution()
    # TS 1
    nums = [2, 4, 6]
    k = 2
    output = 4

    # TS 2
    # nums = [1]
    # k = 1
    # output = 1

    # TS 3
    nums = [1, 1, 2, 3]
    k = 1
    output = 8
    print(Solution().beautifulSubsets(nums, k))


if __name__ == "__main__":
    main()
