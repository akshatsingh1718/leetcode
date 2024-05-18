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
Help: https://www.youtube.com/watch?v=ysytSSXpAI0&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=39
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
    N = len of linked list along next axis
    M = len of linked list along down axis
    TC: O(N * 2M) ~ O(N * M) [N operations will take place for 2 M ops for checking values]
    SC: O(N) [if considering recursion stack space]

    ==========================
    Algorithm:
    ==========================
    """

    def flatten(self, root):

        def merge(node1: Node, node2: Node):
            prv = Node(-1)
            dummyNode = prv

            while node1 is not None and node2 is not None:
                if node1.data < node2.data:
                    prv.bottom = node1
                    prv = node1
                    node1 = node1.bottom
                else:
                    prv.bottom = node2
                    prv = node2
                    node2 = node2.bottom

            if node2 is not None:
                prv.bottom = node2
            if node1 is not None:
                prv.bottom = node1

            return dummyNode.bottom

        def dfs(node: Node):
            if node is None or node.next is None:
                return node

            node2 = dfs(node.next)

            # merge
            node.next = None
            head = merge(node, node2)

            return head

        return dfs(root)


def main():
    obj = Solution()


if __name__ == "__main__":
    main()
