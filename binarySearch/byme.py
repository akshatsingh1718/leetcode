"""
Started On: 24 Aug 23
End On: 24 Aug 23

"""
from typing import List
from sample import *
import numpy as np


class Solution:
    def isValueInList(self, vector: List[int], value: int) -> None:
        n = len(vector)

        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if vector[mid] == value:
                return True

            # if value is gt the mid value, ignore the left half
            elif vector[mid] < value:
                low = mid + 1
            # if value is lt the mid value, ignore the right half
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    # iterate over rows
    for i in range(len(TestCases)):
        given = TestCases[i]
        res = sol.isValueInList(TestCases[i][0], TestCases[i][1])
        if res != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(TestCases[i])
            print("--> Given")
            print(given)
            testcases_failed += 1
        else:
            testcases_passed += 1
    
    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
