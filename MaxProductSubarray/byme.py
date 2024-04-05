from typing import *


class Solution:
    def prod(self, nums: List[int]):
        prod = 1
        for n in nums:
            prod *= n
        return prod

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]

        for i in range(n):
            for j in range(i + 1, n + 1):
                print(f"{self.prod(nums[i:j])} when {i=} {j=}")
                if max_sum < self.prod(nums[i:j]):
                    max_sum = self.prod(nums[i:j])
        return max_sum


def main():
    s = Solution()

    nums = [2,3,-2,4]
    output= 6

    # nums = [-2, 0, -1]
    # output = 0

    # nums = [-4,-3]
    # output = 12


    res = s.maxProduct(nums)

    print(res)

    # assert output == res, "Not Matching"


main()
