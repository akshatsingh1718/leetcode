"""
Started On: 26 Aug 23
End On: 26 Aug 23

Variant 2 : where user needs to return Yes or No is the sum exist and not the idx
This sol will sort the array so we cannot return the true idx
"""
from typing import List
from sample import *
import numpy as np


class Solution:
    """ """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1

        # sort array
        nums.sort()

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return "YES"

            # if current sum is lt target then increase the current sum
            # by moving to right
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return "NO"


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    # iterate over rows
    for i in range(len(TestCases)):
        given = TestCases[i]
        res = sol.twoSum(TestCases[i][0], TestCases[i][1])
        if res != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(res)
            print("--> Given")
            print(given)
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
