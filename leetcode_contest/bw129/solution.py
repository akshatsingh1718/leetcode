from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        

        n, m = len(grid), len(grid[0])

        def check_grid(i, j):
            nonlocal grid

            for i in range(2):
                
                for j in range(2):
                    


        for i in range(n):
            for j in range(m):
                grid_val = grid[i][j]
                if grid[i][j] == "B":
                    grid[i][j] = "W"
                    check_grid()


grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
print(Solution().canMakeSquare(grid))