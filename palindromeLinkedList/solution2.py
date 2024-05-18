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
Problem:https://leetcode.com/problems/palindrome-linked-list/submissions/1261148430/
Help: https://www.youtube.com/watch?v=-DtNInqFUXs&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=37
"""


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n // 2) [find middle] + O(n//2) [reversal] + O(n // 2) [check both half]
    TC (for get back the original list): Above TC + O(n//2) [again find middle] + O(n // 2) [again reverse]
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # slow and fast pointer to find the middle of the linked list
        def find_middle_node(node: ListNode):
            slow = node
            fast = node

            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow

        middle_node = find_middle_node(head)

        # reverse the linked list from the middle
        def reverse_list(node: ListNode):
            curr = node
            prv = None
            while curr is not None:
                curr.next, curr, prv = prv, curr.next, curr
            return prv

        reversed_list_head = reverse_list(middle_node.next)

        # move pointer from starting of linked list and reversed linked list
        # and check if they both are same or not
        node = head
        while reversed_list_head is not None:
            if reversed_list_head.val != node.val:
                return False
            reversed_list_head = reversed_list_head.next
            node = node.next

        return True


def main():
    obj = Solution()
    head = list_to_ll([1, 2, 2, 1])
    head = list_to_ll([1, 2])

    print(obj.isPalindrome(head))


if __name__ == "__main__":
    main()
