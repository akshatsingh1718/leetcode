from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):

                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        TC: O(2N)
        SC: O(1)
        """

        n = len(nums)

        count_0 = 0
        count_1 = 0

        # TC: O(N)
        # SC: O(2)  ~ O(1) constant 
        for i in range(n):

            # check the current number of the list
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1

        # TC: O(N) 
        # SC: O(0)
        for i in range(0, count_0):
            nums[i] = 0
        for i in range(count_0, count_1):
            nums[i] = 1
        for i in range(count_1, n):
            nums[i] = 2

        return nums


nums = [2, 0, 2, 1, 1, 0]
o = [0, 0, 1, 1, 2, 2]
ans = Solution().sortColors(nums)

print(ans)
