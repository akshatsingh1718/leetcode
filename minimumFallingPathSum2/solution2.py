from typing import List


class Solution:
    '''
    Throws TLE
    
    TC: O(n^3)
    SC: O(n^2)

    Algo:
    use dp for caching
    '''
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        dp = dict()

        def find_min_path(i: int, prv_j: int) -> int:
            nonlocal m, n, grid, dp

            if i == n:
                return 0

            if (i, prv_j) in dp:
                return dp[(i, prv_j)]

            res = float("inf")
            for j in range(m):
                if j != prv_j:
                    res = min(
                        grid[i][j]
                        + find_min_path(
                            i + 1,
                            prv_j=j,
                        ),
                        res,
                    )

            dp[(i, prv_j)] = res

            return res

        res = float("inf")
        for j in range(m):
            res = min(find_min_path(0, j), res)
        print(dp)
        return res


# TS1
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = 13

# TS2
# grid = [[7]]
# output = 7

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
