from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        TC: O(n^3)
        SC: O(1)
        """

        max_val = -9999
        n = len(nums)
        for i in range(n):
            for j in range(i, n):

                _sum = 0
                for k in range(i, j):
                    _sum += nums[k]

                max_val = max(_sum, max_val)

        return max_val

    def maxSubArray_better(self, nums: List[int]) -> int:
        """
        TC: O(n^2)
        SC: O(1)
        """

        max_val = -9999
        n = len(nums)
        for i in range(n):

            _sum = 0
            for j in range(i, n):
                _sum += nums[j]
                max_val = max(_sum, max_val)

        return max_val


i = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
o = [4, -1, 2, 1]
a = Solution().maxSubArray_better(i)

print(a)
