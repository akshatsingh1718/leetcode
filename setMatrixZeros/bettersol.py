'''
Initialize a row and col vector with zeros and turn the row[n] or col[m] 
to 1 if  corresponding matrix[n][m] is 0.
'''
from sample import TestCases, Expected
from typing import List
import numpy as np

class Solution():
    '''
    Runtime
    119ms
    Beats 74.60%of users with Python3

    Memory
    17.31MB
    Beats 18.15%of users with Python3
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # rows, cols
        n, m = len(matrix), len(matrix[0])

        # initialize row and col vector
        row, col = [0] * n, [0] * m

        # iterate over matrix and fill row and col vector
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == 0):
                    # mark corresponding vectors to 1
                    row[i] = 1
                    col[j] = 1


        # re-iterate over matrix and make the 1's value from row and col idx in matrix to 0
        for i in range(n):
            for j in range(m):
                if row[i] == 1 or col[j] ==1:
                    matrix[i][j] = 0



if __name__ == "__main__":
    sol = Solution()

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

    