from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # pos: res
        cache = dict()
        max_score = float("-inf")
        def find_score(i: int, j: int):
            nonlocal cache, n, m, grid, max_score
            if i >= n or j >= m:
                return 0

            res = float("-inf")

            if cache.get((i, j)) is not None:
                res = cache[(i, j)]

            else:
                # go right
                for t_i in range(i + 1, n):
                    res = max(find_score(t_i, j), grid[t_i][j] - grid[i][j], res)

                # go bottom
                for t_j in range(j + 1, m):
                    res = max(find_score(i, t_j), grid[i][t_j] - grid[i][j], res)

                cache[(i, j)] = res

            max_score = max(max_score, res)
            return res
        
        res =  find_score(0, 0)
        print(cache)

        return res

grid = [[9, 5, 7, 3], 
        [8, 9, 6, 1], 
        [6, 7, 14, 3], 
        [2, 5, 3, 1]]
output = 9

# TS1
# grid = [[4,3,2],[3,2,1]]
# output= -1

print(Solution().maxScore(grid))
