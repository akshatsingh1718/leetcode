from typing import List, Optional, Union, Dict, Tuple, Set
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict


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

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # check for distinct colors
        n = len(queries)
        result = []
        balls = [0 for _ in range(limit + 1)]
        freq = defaultdict(int)

        distinct = 0
        for idx, (ball_no, color) in enumerate(queries):
            # ball seen already
            if balls[ball_no] != 0:
                # same color for ball
                if balls[ball_no] == color:
                    pass
                # different color for ball
                else:
                    # already seen color
                    if freq[color] > 0:
                        freq[color] += 1  # new color took the new place
                        freq[
                            balls[ball_no]
                        ] -= 1  # color has been vanished from a place
                        distinct -= 1  # distinct color decreases as ball color is seen already and its prv color was different from the new given color
                    # new color
                    else:
                        distinct += 1 # color has not been seen yet
                        freq[
                            balls[ball_no]
                        ] -= 1  # color has been vanished from a place
                        freq[color] += 1  # new color took the new place

                    # paint with the new given color
                    balls[ball_no] = color
            # ball not seen yet
            else:
                # already seen color
                if freq[color] > 0:
                    freq[color] += 1  # new color took the new place
                # new color
                else:
                    freq[color] += 1  # new color took the new place
                    distinct += 1

                # pain the new ball
                balls[ball_no] = color
            # ball never seen

            result.append(distinct)

        return result


def main():
    obj = Solution()

    limit = 4
    queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    output = [1, 2, 2, 3, 4]

    # TS 2
    limit = 4
    queries = [[1,4],[2,5],[1,3],[3,4]]
    output= [1,2,2,3]

    # TS 3
    # queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]
    # limit = 1
    # expected = [1,2,1,2,1]


    print(obj.queryResults(limit, queries))


if __name__ == "__main__":
    main()
