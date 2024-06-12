from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        ==========================
        Time and space complexity:
        ==========================

        TC: O(n) + O(n) ~ O(n)
        SC: O(1)

        ==========================
        Algorithm:
        ==========================
        """

        n = len(nums)
        nums_sum = 0
        count_1 = 0
        for num in nums:
            nums_sum += num
            count_1 += 1 if num == 1 else 0

        count_2 = (nums_sum - count_1) // 2
        count_0 = len(nums) - count_1 - count_2

        i = 0
        while i < count_0:
            nums[i] = 0
            i += 1
        while i < count_0 + count_1:
            nums[i] = 1
            i += 1
        while i < count_0 + count_1 + count_2:
            nums[i] = 2
            i += 1


# nums = [2, 0, 2, 1, 1, 0]
# o = [0, 0, 1, 1, 2, 2]

nums = [1, 2, 0]
o = [0, 1, 2]

ans = Solution().sortColors(nums)

print(ans)
