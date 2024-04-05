from sample import *
from typing import List


"""
Started On: 27 Aug 23
Ended On: 27 Aug 23
"""


class Solution:
    """
    Runtime
    Details
    46ms
    Beats 61.58%of users with Python3
    Memory
    Details
    16.53MB
    Beats 36.15%of users with Python3
    """

    def backtrack(self, idx, nums, arr):
        if idx == len(nums):
            arr.append(nums[:])
            return

        for i in range(idx, len(nums)):
            # swap elements
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(idx + 1, nums, arr)
            nums[idx], nums[i] = nums[i], nums[idx]

    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        self.backtrack(0, nums, arr)
        return arr


if __name__ == "__main__":
    sol = Solution()
    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        res = sol.permute(TestCases[i])
        if checkSol(res, Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(res)
            print("--> Given")
            print(TestCases[i])
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }/{len(TestCases)}")
    print(f"{testcases_failed = }/{len(TestCases)}")
