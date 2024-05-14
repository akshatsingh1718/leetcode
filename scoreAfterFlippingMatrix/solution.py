from typing import List


class Solution:
    """
    Time and space complexity:
    ==========================
    n = no of rows
    m = no of columns

    TC: O(n) [0th index bit flip] + O(m * n * m) [for loop on all elements + flip col] + O(m * n) [cal score]
      : O(n) + O(m^2 * n) + O(m * n)

    SC: O(1)
    """

    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # Helper functions to flip bits of rows and cols
        def flip_col(col_idx):
            nonlocal grid, m, n
            for c in range(n):
                grid[c][col_idx] = 1 if grid[c][col_idx] == 0 else 0

        def flip_row(row_idx):
            nonlocal grid, m, n
            for r in range(m):
                grid[row_idx][r] = 1 if grid[row_idx][r] == 0 else 0

        # if the 1st bit of each binary number is zeros then flip
        # the row since we need the 1 on the 0th index for making the
        # number largest as possible
        for i in range(n):
            if grid[i][0] == 0:
                flip_row(i)

        # Now iterate over all the columns from left to right
        # and check if the col has no of ones less than the half of
        # column size, if yes it means columns bits should be flipped and
        # we will get more ones than zeros.
        for col in range(m):
            # count no of ones in col
            count_of_ones = 0
            for row in range(n):
                count_of_ones += grid[row][col]

            # if count_of_ones < n / 2:
            if count_of_ones < n - count_of_ones: # count_of_ones < count_of_zeros
                flip_col(col)

        # calculate the score
        score = 0
        for i in range(n):
            binary_str = "".join(str(s) for s in grid[i])
            score += int(binary_str, 2)

        return score


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
output = 39

# TS2
# grid = [[0]]
# output = 1

print(Solution().matrixScore(grid))
