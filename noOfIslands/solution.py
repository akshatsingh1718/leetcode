from typing import List

class Solution1:
    '''
    This quesiton assumes only to count the islands which are connected via diagonal
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        start_i, start_j = -1, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    start_i = i
                    start_j = j
                    break
            if start_j != -1:
                break

        if start_i == -1:
            return 0

        max_c = 0
        def dfs(i:int, j:int, count:int):
            nonlocal grid, n, m, max_c
            if not (0 <= i < n) or not (0 <= j < m) or grid[i][j] == "0":
                return 0
            
            if grid[i][j] == -1:
                return 0
            
            max_c = max(max_c, count)
            
            grid[i][j] = -1
            
            # for non diagonal
            dfs(i + 1, j, count)
            dfs(i - 1, j, count)
            dfs(i, j + 1, count)
            dfs(i, j - 1, count)

            # for diagonal
            dfs(i - 1, j - 1, count + 1)
            dfs(i - 1, j + 1, count + 1)
            dfs(i + 1, j - 1, count + 1)
            dfs(i + 1, j + 1, count + 1)

            return count

        
        dfs(i=start_i, j=start_j, count= 1)
        return max_c


class Solution():

    '''
    TC: O(n x m) [to iterate over all the water and land] + O(n + m) [to see the neighbours in worst case when its all "1"s]
    SC: O(1) or O(n x m) [if using visited array for n and m]
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            nonlocal grid, n, m

            # if border or water encounters then simply return none
            if not (0 <= i < n) or not (0 <= j < m) or grid[i][j] == "0":
                return None
            
            # if already visited
            # if grid[i][j] == -1:
            #     return None

            # change the visited state
            # grid[i][j] = -1
            grid[i][j] = "0"


            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


# TS1    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
output= 3

# TS2
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
output= 1

# TS3
grid = [["1","0","1","1","0","1","1"]]
output = 3

print(Solution().numIslands(grid))