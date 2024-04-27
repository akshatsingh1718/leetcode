from typing import List


class Solution:
    """
    TC: O(n^3)
    SC: O(2n) ~ O(n) [for storing dp and next_dp]

    Algo:
    1. Move from top to bottom and store the previous cumilative min sum along the way
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        dp = grid[0]
        next_dp = [0 for _ in range(m)]

        # Iterate over all the rows
        for i in range(1, n):

            for j in range(m):
                min_val = float("inf")

                # find the min from the prv dp
                for val_idx, val in enumerate(dp):
                    if val_idx != j:  # prv col should not be same as the present col
                        min_val = min(val, min_val)

                # set the next dp value by adding the current chosen col value + prv min value
                next_dp[j] = min_val + grid[i][j]

            # make the prv_dp current dp and assign the dp as next row
            dp = next_dp[:]

        return min(dp)


# TS1
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = 13

# TS2
grid = [[7]]
output = 7

# TS3
grid = [
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
    [2, 2, 1, 2, 2],
]
output = 7

print(Solution().minFallingPathSum(grid))
