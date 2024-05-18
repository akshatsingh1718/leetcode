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
Help: done by me
"""

class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    TC: O(n) [find len] + [O((n//k)* k) ~ O(n)] (reverser groups) + O(n//k) [queue to list]
    SC: O(n)

    ==========================
    Algorithm:
    ==========================
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find the len of list
        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1

        # Queue will hold all the groups data which consists of starting of a group
        # and ending of group.
        # will have starting and ending of nodes after reversal
        # Ex:- queue = [ (starting_1, ending_1), (starting_pt_2, ending_pt_2) ..]
        queue: List[Tuple[ListNode, ListNode]] = []

        # assign the node as head
        start_head = head

        # we can only make n // k groups
        for _ in range(n // k):
            # reverse the group
            curr = start_head
            prv = None
            # reverse a certain group
            for _ in range(k):
                curr.next, curr, prv = prv, curr.next, curr

            ## What is prv after reversal ?
            # after reversal prv will be pointing to the last element of the
            # current group which will be become the 1st element of the group
            # after reversal

            # what is node after reversal ?
            # node will still be pointing to the first node of the group

            # append the starting and ending of node
            # prv = last node
            # node = first node
            queue.append((prv, start_head))  # (new head, new tail)

            # update the start_head to the next element of the group
            start_head = curr

        # append the last start_head as no further
        # group can be made
        queue.append((start_head, None))

        # the new head we have
        head = queue[0][0]
        prv_end_node = queue[0][1]

        # move over all the group pairs
        for start_node, end_node in queue[1:]:
            # make the prv end node next as current start node
            prv_end_node.next = start_node
            # update the prv end node
            prv_end_node = end_node

        return head


def main():
    head = list_to_ll([1, 2, 3, 4, 5])
    k = 2
    res = Solution().reverseKGroup(head, k)
    printList(res)


if __name__ == "__main__":
    main()
