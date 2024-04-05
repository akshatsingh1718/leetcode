from typing import List
from sample import *
import numpy as np


class Solution:
    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swap_cols(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.swap_cols(matrix)


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0

    for i in range(len(TestCases)):
        given = np.array(TestCases[i])
        sol.rotate(TestCases[i])
        if TestCases[i] != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(np.array(Expected[i]))
            print("--> Got")
            print(np.array(TestCases[i]))
            print("--> Given")
            print(given)
            testcases_failed += 1
        else:
            testcases_passed += 1
    
    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
