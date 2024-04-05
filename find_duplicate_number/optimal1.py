from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = 0

        for i in nums:
            x = x ^ i

        for i in range(1, len(nums)):
            x = x ^ i
        return x


nums = [1,3,4,2,3]
Output= 2

res = Solution().findDuplicate(nums)

print(res)



