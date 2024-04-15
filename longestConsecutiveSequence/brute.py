from typing import List


class Solution:
    """
    TC: O(N) [for loop] + (~ O(N)) [linear search to find (ele+1) + increment count and ele] ~ O(N^2)
    SC: O(1)

    """

    def longestConsecutive(self, nums: List[int]) -> int:

        max_ctr = 0

        for ele in nums:
            ctr = 1
            ele += 1

            while ele in nums: # linear search
                ctr += 1 # increment counter
                ele += 1 # increment to next number sequence

            max_ctr = max(max_ctr, ctr)

        return max_ctr


# TS1
nums = [100, 4, 200, 1, 3, 2]
output = 4

nums = []
output = 0

print(Solution().longestConsecutive(nums))
