from typing import List


class Solution:
    """
    TC: O(n^2)
    SC: O(2)

    Algo:
    1. Move from top to bottom and store the previous two cumilative min sum along the way
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        def get_min_two(row):

            two_smallest = []
            for idx, val in enumerate(row):

                if len(two_smallest) < 2:
                    two_smallest.append((val, idx))
                elif two_smallest[1][0] > val:
                    two_smallest.pop()
                    two_smallest.append((val, idx))
                two_smallest.sort()  # always sort ony two elements

            return two_smallest

        n, m = len(grid), len(grid[0])
        cum_row = grid[0][:]
        dp = get_min_two(grid[0])

        # now iterate over all the rows
        for i in range(1, n):
            # create cum row
            cum_row = [
                (
                    (dp[0][0] + grid[i][j])
                    if j != dp[0][1]
                    else (dp[1][0] + grid[i][j])
                )
                for j in range(m)
            ]

            # create new two
            dp = get_min_two(cum_row)

        return dp[0][0]


# TS1
# grid = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
# output = 13

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

# TS1
# grid = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
# output = 13

print(Solution().minFallingPathSum(grid))
