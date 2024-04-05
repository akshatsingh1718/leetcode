"""
Started On: 24 Aug 23
End On: 24 Aug 23

"""
from typing import List
from sample import *
import numpy as np


class Solution:
    '''
    Runtime
    49ms
    Beats 72.70%of users with Python3

    Memory
    16.98MB
    Beats 20.69%of users with Python3
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = low + (high - low) // 2

            row, col = mid // n, int(mid % n)
            print(f"({row}, {col}), mid={mid}")

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1
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
        print("=" * 50)
        given = TestCases[i]
        res = sol.searchMatrix(TestCases[i][0], TestCases[i][1])
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
            print(f"Passes TC = {i+1}")
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
