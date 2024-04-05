'''
Coming from bettersol.py we need to remove the extra space of row[n] and col[m] which was taking ( O(n) + O(m) )

We will assume that our row[n] is matrix[0, :] and col[m] = matrix[:, 0],
But ! the problem is matrix[0][0] is common for both row and col. The sol to this can be an extra
variable to hold the value of col[0].

## The catch

We will iterate over the rows and cols except the first row and col of the matrix as they will
hold the value for if corresponding idx needs to be changed to 0 or not.

'''
from sample import TestCases, Expected
from typing import List
import numpy as np

class Solution():
    '''
    Runtime
    124ms
    Beats 63.84%of users with Python3

    Memory
    17.13MB
    Beats 83.83%of users with Python3
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # get dims
        n, m = len(matrix), len(matrix[0])

        # set col[0] = 1 (extra var)
        col_0 = 1

        # iterate over rows and cols
        for i in range(n):
            for j in range(m):

                # mark zeros 
                if matrix[i][j] == 0:

                    # mark matrix row and col idx to 0
                    matrix[i][0] = 0 # row 

                    # col special case when j == 0 then use extra var we defined
                    if j==0:
                        col_0 = 0
                    else:
                        matrix[0][j] = 0

        # Now, iterate over the idx which are not used as row and col
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Till now each element in the matrix is done except the first row and col
        # let's iterate over row and col, But which one to iterate over first ?

        # The first row of the matrix is dependent on the row[0] and the their value themselves 
        # and the first col of the matrix is dependent on the col_0 and their value themselves
        # so if we try to solve the row vector first then the row[0] might change to 0 and could 
        # potentially change the values of the col[0] of the matrix so we should sol col vector first


        # if the matrix[0][0] is 0 the matrix[0, :] will be zero no matter what their values is because
        # they also depend on the matrix[0][0]. 
        isZeroForMatrixRow0 =  matrix[0][0] == 0

        # iterate over col first to solve
        # Starting from 1st idx because matrix[0] belongs to row vector and not col in our case
        if isZeroForMatrixRow0:
            for j in range(1, m):
                matrix[0][j] = 0


        isZeroForMatrixCol0 =  col_0 == 0
        if isZeroForMatrixCol0:
            for i in range(n):
                matrix[i][0] = 0


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

    