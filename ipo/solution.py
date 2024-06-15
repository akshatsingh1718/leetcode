    from typing import List, Optional, Union, Dict, Tuple, Set
    from bisect import bisect, bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from functools import cache
    from math import floor, ceil
    from heapq import heapify, heappop, heappush

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
        TC: O(n) [comb list] + O(n log n) [sort] + O(n) * O(2 log n)[push and pop] ~ O(n log n)
        SC: O(n) [combined list] + O(n) [tim sort] + O(n) [heap] ~ O(n)

        ==========================
        Algorithm:
        ==========================
        1. Create a combined list of capital and profits and sort it based on capital since it is the only thing which determines if we can start a project or not.
        2. Given the initial capital we need to add all the profit into heap which we can have by investing the current capital we have.
        3. After gathering all the profits we can do get the max profit and pop it from the heap.
        4 Add the profit to the current capital `w` we have and check for new profits we can make with the current capital.
        """

        def findMaximizedCapital(
            self, k: int, w: int, profits: List[int], capital: List[int]
        ) -> int:
            profit_capital = list(zip(capital, profits))  # TC: O(n)
            profit_capital.sort(key=lambda x: x[0])  # TC: O(n log n)

            i = 0
            # bucket to store how much projects you can do till
            min_heap = []
            while i < len(profit_capital) and k > 0:  # TC: O(n)
                # get all the projects we can do with the current capital w we have
                while i < len(profit_capital) and profit_capital[i][0] <= w:
                    heappush(
                        min_heap, -profit_capital[i][1]
                    )  # use -ve to use min heap as max heap
                    i += 1

                # find the max profit
                if len(min_heap) > 0:
                    w += -heappop(min_heap)
                    k -= 1
                else:
                    break  # cannot create further profit

            while k > 0 and len(min_heap) > 0:  # TC: O(n)
                w += -heappop(min_heap)
                k -= 1

            return w


    def main():
        obj = Solution()
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        output = 4

        # Ts 2
        # k = 1
        # w = 0
        # profits = [1, 2, 3]
        # capital = [0, 1, 2]
        # output = 1

        # Ts 3
        # k = 1
        # w = 0
        # profits = [1, 2, 3]
        # capital = [1, 1, 2]
        # output = 0

        # Ts 2
        # k = 3
        # w = 0
        # profits = [1, 2, 3]
        # capital = [0, 1, 2]
        # output = 6
        print(obj.findMaximizedCapital(k, w, profits, capital))


    if __name__ == "__main__":
        main()
