from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        def dfs(r, c):
            # Base case where we return for water and going out of grid 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            # if already visited then return 0
            if grid[r][c] == -1:
                return 0
            
            # mark visited
            grid[r][c] = -1

            # Now recurse more if our current element is carrying value as 1
            return (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))

        is_started = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)
                    is_started = True
                    break
            if is_started:
                break
                    


        return perimeter
    

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
output = 16
print(Solution().islandPerimeter(grid))
