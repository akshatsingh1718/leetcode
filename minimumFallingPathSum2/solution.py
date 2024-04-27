from typing import List


class Solution:
    '''
    TLE
    '''
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        minimum_path = float("inf")
        n = len(grid)
        m = len(grid[0])

        def find_min_path(i: int, prv_j: int, curr_sum: int, arr) -> int:
            nonlocal m, n, grid, minimum_path

            if i == n:
                print(arr)
                return curr_sum

            for j in range(m):
                if j != prv_j:
                    res = find_min_path(
                        i + 1,
                        prv_j=j,
                        curr_sum=curr_sum + grid[i][j],
                        arr=arr + [grid[i][j]],
                    )
                    minimum_path = min(minimum_path, res)

            return minimum_path

        return find_min_path(0, -1, 0, [])

# TS1
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = 13

# TS2
# grid = [[7]]
# output = 7

# TS3
grid = [[2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2],
        [2,2,1,2,2]]
output = 7

print(Solution().minFallingPathSum(grid))
