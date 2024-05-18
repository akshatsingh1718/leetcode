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
Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
Help: https://www.youtube.com/watch?v=Of0HPkk3JgI&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=34
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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(node: ListNode):
            prv = None
            curr = node
            while curr is not None:
                curr.next, curr, prv = prv, curr.next, curr
            # return new head
            return prv

        def find_kth_node(node: ListNode, k: int):
            i = 1
            while i < k and node is not None:
                node = node.next
            return node

        next_node = head
        prv = ListNode(-1, next=head)
        i = 0
        main_head = head
        while next_node is not None:

            temp = next_node
            # find the kth node
            kth_node = temp
            counter = k
            while counter > 1 and kth_node.next is not None:
                kth_node = kth_node.next
                counter -= 1

            if counter == 1:
                next_node = kth_node.next
                kth_node.next = None
                # reverse from temp to kth node
                reverse(temp)

                prv.next = kth_node
                prv = temp
                temp.next = next_node
            else:
                break
            if i == 0:
                main_head = kth_node

            i += 1

        return main_head


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n)
    SC: O(1)

    ==========================
    Algorithm:
    ==========================
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(node: ListNode):
            prv = None
            curr = node
            while curr is not None:
                curr.next, curr, prv = prv, curr.next, curr
            # return new head
            return prv

        def find_kth_node(node: ListNode, k: int):
            i = 1
            while i < k and node is not None:
                node = node.next
                i += 1

            return node

        next_node = head
        prv = ListNode(-1, next=head)
        main_head = head
        while True:
            
            # make the next node as temp node (which will be starting node)
            temp = next_node
            # find the kth node
            kth_node = find_kth_node(temp, k)

            if kth_node is not None:
                # preserve the next node of the kth node
                # to further do operation on other half
                next_node = kth_node.next
                # break the kth node link to make the ll
                # group independent of other nodes
                kth_node.next = None
                # reverse the group
                reverse(temp)

                # prv node will point to the kth node
                prv.next = kth_node
                # prv will be now the temp node which was the starting of
                # the current group and now becomes ending of the current node
                # so prv will become the last node of the current grp
                prv = temp
                # now the last node of current grp which is prv
                # will point to the first node of the next group
                prv.next = next_node
            else:
                break
            
            # if the temp is equal to the given head
            # it means its the first group and 1st group
            # kth element will be the head of the resultant
            if temp == head:
                main_head = kth_node


        return main_head


def main():
    head = list_to_ll([1, 2, 3, 4, 5, 6, 7])
    k = 3
    res = Solution().reverseKGroup(head, k)
    printList(res)


if __name__ == "__main__":
    main()
