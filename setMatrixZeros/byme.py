'''
Started on 21 Aug 23
'''
from typing import List
import numpy as np
from sample import TestCases, Expected

class Solution:
    '''
    Runtime
    123 ms

    Memory
    17.1 MB
    '''
    def getZeroIndexsInRow(self, m, i):
        idx = []
        # iterate over cols
        for k in range(len(m[i])):
            if m[i][k] == 0:
                idx.append(k)
        return idx

    def setZerosInRowAndCol(self, m, r, c):
        # set 0 in row
        for k in range(len(m[r])):
            m[r][k] = 0

        # set 0 in col
        for k in range(len(m)):
            m[k][c] = 0

    # def isVisited(self, visited_idxs, checkR, checkC):
    #     for vRow, vCol in visited_idxs:
    #         if vRow == checkR or vCol == checkC:
    #             return True
    #     return False

        

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # visited_idxs = []

        # Key : row, value : cols containing zeros
        make_row_cols_zero = {}

        # iterate over rows and check for 0's
        for i in range(len(matrix)):
            cols = self.getZeroIndexsInRow(matrix, i)
            make_row_cols_zero[i] = cols

        # Now set zeros after getting zeros positions
        for key, cols in make_row_cols_zero.items():
            for col in cols:
                self.setZerosInRowAndCol(matrix, r=key, c=col)

            # for col in cols:
            #     if (col != -1) and not self.isVisited(visited_idxs, i, col):
            #         self.setZerosInRowAndCol(matrix, r=i, c=col)
            #         visited_idxs.append((i, col)) # add (row, col)


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    for i  in range(len(TestCases)):
        given= np.array(TestCases[i])
        sol.setZeroes(TestCases[i])
        if(TestCases[i] != Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(np.array(Expected[i]))
            print("--> Got")
            print(np.array(TestCases[i]))
            print("--> Given")
            print(given)


