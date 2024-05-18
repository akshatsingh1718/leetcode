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
Problem: https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
Help:
"""


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom

    print()


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n * m * m * n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def flatten(self, root):
        if root is None:
            return root

        def add_node(node: Node, new_node: Node):

            while node.next is not None and node.val < new_node.val:
                node = node.val

            node_next = node.next
            node.next = new_node
            new_node.next = node_next

        node = root
        while node is not None:
            btm_node = node.bottom

            while btm_node is not None:
                add_node(node, btm_node)
                btm_node = btm_node.next


            node.bottom = None
            node = node.next

        return root


def main():
    obj = Solution()


if __name__ == "__main__":
    main()
