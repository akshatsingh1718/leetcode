from typing import List, Optional, Union, Dict, Tuple


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
    GOT TLE

    ==========================
    Time and space complexity:
    ==========================
    TC: 
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        def is_special(nums):
            if len(nums) in [1, 0]:
                return True

            n = len(nums)

            for i in range(n - 1):
                if nums[i] % 2 == nums[i + 1] % 2:
                    return False
            return True

        n = len(nums)
        can_never_make = []
        for i in range(n - 1):
            if not is_special(nums[i : i + 2]):
                can_never_make.append(i)

        can_never_make.sort()

        def search(start):
            nonlocal can_never_make
            low = 0
            high = len(can_never_make)

            while low < high:
                mid = low + (high - low) // 2
                print(start, " ", mid)
                if mid == start:
                    return True
                
                elif mid <= start:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        res = []
        for start, end in queries:

            if search(start):
                res.append(False)
            else:
                res.append(True)

        return res


def main():
    obj = Solution()

    nums = [3, 4, 1, 2, 6]
    queries = [[0, 4]]

    # TS2
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]

    # TS3
    nums = [1,4]
    queries = [[0, 1]]
    print(obj.isArraySpecial(nums, queries))


if __name__ == "__main__":
    main()
