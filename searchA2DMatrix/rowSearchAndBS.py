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
    47ms
    Beats 80.93%of users with Python3

    Memory
    16.80MB
    Beats 86.58%of users with Python3

    TC = O(n) + O(log m) ~ O(n) 
    It it as good as  O(n)
    '''
    def bs(self, array: List[int], target: int) -> bool:
        n = len(array)
        high = n - 1
        low = 0

        while low <= high:
            mid = low + (high - low) // 2

            if array[mid] == target:
                return True

            # if target is gt mid value then ignore left half
            if array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) , len(matrix[0]) - 1

        for i in range(m): # O(n)
            if matrix[i][0] <= target <= matrix[i][n]:
                return self.bs(matrix[i], target) # O(log m)
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
