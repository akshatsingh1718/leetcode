"""
Started On: 26 Aug 23
End On: 26 Aug 23
"""
from typing import List
from sample import *
import numpy as np


class Solution:
    """
    Runtime
    Details
    59ms
    Beats 93.11%of users with Python3
    Memory
    Details
    17.65MB
    Beats 33.83%of users with Python3
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        visited_map = dict()

        for i in range(n):
            diff = target - nums[i]
            idx = visited_map.get(diff)
            if idx is not None:
                # remember to put idx first and i as idx comes first in the list
                # as it has been already added to the map
                return [idx, i]
            else:
                visited_map[nums[i]] = i


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
