"""
Problem: https://leetcode.com/problems/maximize-happiness-of-selected-children/
"""

from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        # Python's default heap data structure is a min heap
        max_heap = [-h for h in happiness]
        heapify(max_heap)
        res = 0

        for turns in range(k):
            res += max(-heappop(max_heap) - turns, 0)

        return res


happiness = [1, 2, 3]
k = 2
output = 4

# TS2

happiness = [2, 3, 4, 5]
k = 1
output = 5

# TS3
# happiness = [1, 1, 1, 1]
# k = 2
# output = 1

print(Solution().maximumHappinessSum(happiness, k))
