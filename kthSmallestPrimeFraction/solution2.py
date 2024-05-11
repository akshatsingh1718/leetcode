from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    """
    Time & Space complexity
    =======================
    NOTE: There will n^2 elements added to the heap.

    TC: O(n^2) [for loop] * O(log n^2) [heap insertion] + O(k * log n^2) [k heap pop operations] ~  O(n^2 * log(n) + k * log(n))
    SC: O(n^2) [n^2 elements added to the heap]

    Algo (Min heap):
    1. Find all the fractions from i: 0->n ; j: i+1->n and add them to min heap.
    2. pop the top k elements.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)

        min_heap = []
        for i in range(n):
            for j in range(i + 1, n):
                heappush(min_heap, [arr[i] / arr[j], [arr[i], arr[j]]])

        res = None
        for _ in range(k):
            res = heappop(min_heap)[1]

        return res


arr = [1, 2, 3, 5]
k = 3
output = [2, 5]

print(Solution().kthSmallestPrimeFraction(arr, k))
