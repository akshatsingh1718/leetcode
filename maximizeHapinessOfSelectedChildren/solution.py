"""
Problem: https://leetcode.com/problems/maximize-happiness-of-selected-children/
"""

from typing import List


class Solution:
    """
    TC: O(n logn) [sorting] + O(k) [find max happiness] ~ O(n logn)
    SC: O(n) [storing sorted array]
    """

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0

        # offset to lower the happiness after each pass
        offset = 0

        # sort the happiness in desc order to get the max happiness at first
        sorted_happiness = sorted(happiness, reverse=True)

        # find the k students happiness
        for i in range(k):
            # happiness cannot go lower than 0 | always positive
            res += max(sorted_happiness[i] - offset, 0)
            offset += 1

        return res


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        offset = 0

        sorted_happiness = sorted(happiness, reverse=True)

        for offset in range(k):
            res += max(sorted_happiness[offset] - offset, 0)

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
