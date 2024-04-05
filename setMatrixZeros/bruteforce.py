"""
Started on 21 Aug 23
"""
from typing import List
import numpy as np
from sample import TestCases, Expected

PLACEHOLDER = -999

class Solution_1:
    '''
    -> Sol by me from tutorial

    Runtime
    120 ms

    Memory
    17.3 MB
    '''
    def setZerosInRowAndCol(self, m, r, c):
        # set 0 in row
        for k in range(len(m[r])):
            if m[r][k] != PLACEHOLDER: # do not replace PLACEHOLDER with 0 
                m[r][k] = 0

        # set 0 in col
        for k in range(len(m)):
            if m[k][c] != PLACEHOLDER:
                m[k][c] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # iterate over every idx's and mark each 0 as PLACEHOLDER
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = PLACEHOLDER

        # iterate over every idx's and mark each 0 as PLACEHOLDER
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == PLACEHOLDER:
                    matrix[i][j] = 0  # set the PLACEHOLDER index to zero
                    self.setZerosInRowAndCol(matrix, i, j)


class Solution_2:
    '''
    Runtime
    118ms
    Beats 79.69%of users with Python3

    Memory
    17.29MB
    Beats 56.08%of users with Python3
    '''
    def markRow(self, m, r):
        # set 0 in row
        for k in range(len(m[r])):
            if m[r][k] != 0: 
                m[r][k] = PLACEHOLDER

    def markCol(self, m, c):
        # set 0 in row
        for k in range(len(m)):
            if m[k][c] != 0: 
                m[k][c] = PLACEHOLDER


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # iterate over every idx's and mark each 0 as PLACEHOLDER
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.markCol(matrix, j)
                    self.markRow(matrix, i)

        # iterate over every idx's and mark each 0 as PLACEHOLDER
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == PLACEHOLDER:
                    matrix[i][j] = 0  # set the PLACEHOLDER index to zero





if __name__ == "__main__":
    sol = Solution_2()

    # iterate over rows
    for i in range(len(TestCases)):
        given = np.array(TestCases[i])
        sol.setZeroes(TestCases[i])
        if TestCases[i] != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(np.array(Expected[i]))
            print("--> Got")
            print(np.array(TestCases[i]))
            print("--> Given")
            print(given)
