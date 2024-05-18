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


def list_to_circular_ll(values, link_info):
    if not values:
        return None

    nodes = [ListNode(value) for value in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    nodes[-1].next = nodes[0]  # By default, make it circular

    target_index, next_index = link_info
    nodes[target_index].next = nodes[next_index]

    return nodes[0]


def print_circular_ll(head, count):
    current = head
    for _ in range(count):
        print(current.val, end=" -> ")
        current = current.next
    print("...")


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
    TC: O(n)
    SC: O(n)

    ==========================
    Algorithm:
    ==========================
    Create a set and add the visited nodes and if already visited then return the node.
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

        return None


def main():
    obj = Solution()
    # Example usage:
    values = [3, 2, 0, -4]
    link_info = (3, 1)
    head = list_to_circular_ll(values, link_info)

    head = list_to_circular_ll([1, 2], (1, 0))
    res = obj.detectCycle(head)
    print(res.val)


if __name__ == "__main__":
    main()
