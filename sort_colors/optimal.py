from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch national flag algorithm
        """

        n = len(nums)
        mid = 0
        low = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums

# nums = [2, 0, 2, 1, 1, 0]
# o = [0, 0, 1, 1, 2, 2]

nums = [1,2,0]
o = [0, 1, 2]

ans = Solution().sortColors(nums)

# print(ans)
