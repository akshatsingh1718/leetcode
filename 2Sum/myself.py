"""
Started On: 26 Aug 23
End On: 26 Aug 23
"""
from typing import List
from sample import *
import numpy as np


class Solution:
    '''
    Runtime
    5987ms
    Beats 5.38%of users with Python3
    
    Memory
    17.10MB
    Beats 91.22%of users with Python3
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    return [i, j]
                

                


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
