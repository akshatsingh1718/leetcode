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

    def maximumInvitations(self, favorite: List[int]) -> int:

        # Create reverse adj list for BFS
        adj = defaultdict(lambda: [])
        n = len(favorite)
        for i in range(n):
            u = i
            v = favorite[i]

            adj[v].append(u)  # reverse mapping

        # write max BFS
        def bfs(start: int, adj: Dict[int, List[int]], visited):

            queue = deque()
            queue.append((start, 0))  # node, distance
            max_distance = 0

            while queue:
                node, distance = queue.popleft()

                for neig in adj[node]:

                    if neig not in visited:
                        visited.add(neig)
                        queue.append((neig, distance + 1))

                        max_distance = max(max_distance, distance + 1)

            return max_distance

        visited: Set[int] = set()
        happy_couple_emp_len = 0
        cycle_emp_len = 0

        for i in range(n):

            # if i is not visited yet meaning we can start finding a cycle
            # from the ith node since it is evident that the cycle will be present
            # I think this visited is just to use for detecting a cycle because
            # no element can occur in two different component
            if i not in visited:
                # lets start counting our distance from ith node
                curr_node = i

                mp: Dict[int, int] = dict()  # node : distance covered
                distance = 0
                next_node = None
                # move until we hit a circle
                while curr_node not in visited:
                    visited.add(curr_node)  # mark the curr node visited
                    mp[curr_node] = distance  # cal its distance

                    next_node = favorite[curr_node]  # get the next node
                    # increment distance for next node to cal its distance
                    distance += 1

                    if next_node in mp:

                        # now here our curr_node should be visited thats why we break out
                        # of while loop
                        # Now find the cycle length
                        cycle_len = distance - mp[next_node]

                        # always take max cycle even though cycle len == 2
                        cycle_emp_len = max(cycle_emp_len, cycle_len)

                        if cycle_len == 2:
                            # we should create a visited set here and not in BFS since
                            # it can happen that curr_node can take path of next_node as well
                            # since they both are connected with each other
                            visitedNodes = set()
                            visitedNodes.add(curr_node)
                            visitedNodes.add(next_node)

                            # happy couple and can be adjusted with anybody
                            # take both couples max sub routes
                            # example if we take curr_node (person) it can have a lot of persons
                            # liking them / fav person and hence we want the max chain we can obtain
                            happy_couple_emp_len += (
                                2
                                + bfs(curr_node, adj, visitedNodes)
                                + bfs(next_node, adj, visitedNodes)
                            )
                        break

                    # make the curr node as next node to go further
                    curr_node = next_node

        return max(happy_couple_emp_len, cycle_emp_len)


def main():
    obj = Solution()
    favorite = [2, 2, 1, 2]
    Output = 3

    # my testcase
    #             0  1  2  3    4  5  6  7  8
    # favorite = [1, 2, 3, 100, 3, 4, 5, 6, 7]
    # favorite = [1, 2, 3, 100, 3, 4]
    print(obj.maximumInvitations(favorite))


if __name__ == "__main__":
    main()
