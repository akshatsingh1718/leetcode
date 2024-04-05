'''
Started On: 24 Aug 23
End On: 24 Aug 23

'''
from typing import List
from sample import *
import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # size of matrix
        n = len(matrix)
        result = [[i for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                next_rIDX, next_cIDX = j, n - 1 - i
                result[next_rIDX][next_cIDX] = matrix[i][j]
        return result


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    for i in range(len(TestCases)):
        given = np.array(TestCases[i])
        res = sol.rotate(TestCases[i])
        if res != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(np.array(Expected[i]))
            print("--> Got")
            print(np.array(TestCases[i]))
            print("--> Given")
            print(given)
