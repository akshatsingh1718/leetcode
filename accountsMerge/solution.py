from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from math import floor, ceil, gcd
import heapq
from heapq import heapify, heappop, heappush
import itertools as it
import sys

# Check the current recursion limit
current_limit = sys.getrecursionlimit()

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
def create_adjacency_list(edges: List[tuple], directed=False):
    # When n nodes is told but graph does not have all the nodes present
    # this will prevent it from keyerror
    adjacency_list = defaultdict(lambda: [])

    for edge in edges:
        u, v = edge
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []

        adjacency_list[u].append(v)
        if not directed:
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
Problem: https://leetcode.com/problems/accounts-merge/description/
Help:
"""


class Disjoint:

    def __init__(self, V: int):
        self.V = V
        self.rank = [0] * V
        self.parent = list(range(V))

    def find(self, x: int) -> int:
        """
        Find parent of X using path compression
        """
        x_parent = self.parent[x]
        if x_parent == x:
            return x

        self.parent[x] = self.find(x_parent)
        return self.parent[x]

    def union(self, x: int, y: int):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        if self.rank[x_parent] == self.rank[y_parent]:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    V = total accounts
    K = max length of an account
    TC: O(V * K) +  O(V * K * a(V))  + O(V * (VKlogVK + VK + VK))
     => VK + VK a(V) + VVKLogVK + VVK + VVK
     => VK( 1 + a(V) +  VlogVK + V + V )
     => VK ( a(V) + VlogVK)
     => VK * a(V) + VK log vK
    SC: O(VK) [mail_to_node] + O(VK) [emails_list]

    ==========================
    Algorithm:
    ==========================
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # disjoint set
        V = len(accounts)
        ds = Disjoint(V)

        # Map each email to their parent node
        mail_to_node: Dict[str, int] = dict()

        for i in range(V):  # TC: O(V * K)
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]

                # mail is already seen meaning we have already assigned
                # this to another node_id; no need to add into map
                if mail in mail_to_node:
                    ds.union(i, mail_to_node[mail])
                else:
                    mail_to_node[mail] = i  # i is the node id

        # Add the email to the correct username group
        emails_list = [[] for _ in range(V)]
        for mail, node_id in mail_to_node.items():  # TC: O(V * K * alpha(V))
            # get the true parent id
            parent_id = ds.find(node_id)
            emails_list[parent_id].append(mail)

        # sort and add the username before each group emails
        res = []

        for idx, emails in enumerate(emails_list):  # TC: O(V)
            if len(emails) == 0:
                continue

            temp_res = [accounts[idx][0]]  # add username

            # TC: O(VK logVK) [all emails end up in one group]
            emails.sort()  # sort the emails

            # add the username and emails
            temp_res.extend(emails)  # TC: O(VK)

            # add to the res
            res.append(temp_res)  # TC: O(VK)

        return res


def main():
    obj = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    Output = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(obj.accountsMerge(accounts))


if __name__ == "__main__":
    main()
