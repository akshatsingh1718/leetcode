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


class Job:

    # Job class which stores profit and deadline.

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n logn) [sorting] + O(n * n) [for loop on jobs * finding slots]
    SC: O(n) [slots]

    ==========================
    Algorithm:
    ==========================
    """

    def JobScheduling(self, Jobs: List[Job], n):
        Jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        slots = [0 for _ in range(n)]
        profit = 0
        jobs_done = 0

        for job in Jobs:
            prof = job.profit
            deadline = job.deadline

            slot_i = deadline - 1
            while slot_i >= 0 and slots[slot_i] == 1:
                slot_i -= 1

            # if no slot assigned meaning task cannot be done
            if slot_i != -1:
                jobs_done += 1
                profit += prof
                slots[slot_i] = 1

        return [jobs_done, profit]


def main():
    obj = Solution()

    N = 4
    Jobs = {(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)}
    Jobs = [Job(profit=p, deadline=d) for _, d, p in Jobs]
    output = [2, 60]

    N = 5
    Jobs = {(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)}
    Jobs = [Job(profit=p, deadline=d) for _, d, p in Jobs]
    output = [2, 127]
    print(Solution().JobScheduling(Jobs=Jobs, n=N))


if __name__ == "__main__":
    main()
