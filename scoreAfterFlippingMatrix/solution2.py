"""
Problem: https://leetcode.com/problems/score-after-flipping-matrix/submissions/1256910416/?envType=daily-question&envId=2024-05-13
Solution: https://www.youtube.com/watch?v=sMH5Ustubc4
"""

from typing import List


class Solution:
    """
    ==========================
    Time and space complexity:
    ==========================
    n = no of rows
    m = no of columns

    TC: O(m * n) [for loop]

    SC: O(1)
    """

    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # score = (1 << (m - 1)) * n
        score = n << (m - 1)
        # score = n * 2**(m-1)

        # iterate over columns
        for col in range(1, m):

            no_of_ones = 0
            for row in range(n):
                # if the 1st bit is zero and the current bit is 0 then increase count of 1
                # if the 1st bit is 1 nd the current bit is 1 then inc count of 1
                if grid[row][col] == grid[row][0]:
                    no_of_ones += 1
            ## OR
            # for row in range(n):
            #     will_bit_flip = True if grid[row][0] == 0 else False
            #     bit_val = grid[row][col]
            #     if will_bit_flip:
            #         bit_val = 1 if bit_val == 0 else 0
            #     no_of_ones += bit_val

            no_of_zeros = n - no_of_ones
            new_no_of_ones = max(no_of_ones, no_of_zeros)

            # score += (1 << (m - 1 - col)) * new_no_of_ones
            score += new_no_of_ones << (m - 1 - col)
            # or we can write it as
            # since a << b -> a * 2**b
            # score += (2 ** (m - 1 - col)) * new_no_of_ones

        return score


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
output = 39

# TS2
# grid = [[0]]
# output = 1

print(Solution().matrixScore(grid))
