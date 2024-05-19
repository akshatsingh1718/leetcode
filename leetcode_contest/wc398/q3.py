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
    ==========================
    Time and space complexity:
    ==========================
    TC:
    SC:

    ==========================
    Algorithm:
    ==========================
    """

    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return 0

        counts = 0

        def difference(n1, n2):
            c = 0
            for c1, c2 in zip(str(n1), str(n2)):
                if c1 != c2:
                    c += 1
            return c

        nums.sort()

        prv = -1
        prv_count = 0
        for i in range(n - 1):

            if nums[i] == prv:
                cnt = prv_count
                continue
            else:
                visited = dict()
                cnt = 0
                for j in range(i + 1, n):
                    if visited.get(nums[j]) is None:
                        ans = difference(nums[i], nums[j])
                        cnt += ans
                        visited[nums[j]] = ans
                    else:
                        cnt += visited[nums[j]]

                prv = nums[j]
                prv_count = cnt

            counts += cnt
        return counts


def main():
    obj = Solution()

    nums = [13, 23, 12]  # 4

    # nums = [6, 5, 3, 6, 4, 3]  # 13
    # nums = [10,10,10,10] # 0

    print(obj.sumDigitDifferences(nums))


if __name__ == "__main__":
    main()
