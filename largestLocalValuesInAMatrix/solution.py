from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        res = [[0 for _ in range(n-2)] for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = max(grid[i][j: j + 3] + grid[i+1][j: j + 3] + grid[i+ 2][j: j + 3])
        return res