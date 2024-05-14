from typing import List


class Solution:
    """
    Time and space complexity:
    ==========================
    n = no of rows
    m = no of columns
    v = no of cells having gold

    TC: O(m * n) [for loop] + O(4 ^ v) [recursion for each cell] ~ O(m*n*4^v) [quadratic time]
    SC: O(4^v) [recursion stack space]
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def get_gold(i: int, j: int):
            nonlocal m, n, grid
            if (not (0 <= i < n)) or (not (0 <= j < m)) or grid[i][j] == 0:
                return 0

            # store the current value
            curr_val = grid[i][j]
            temp_gold_collected = grid[i][j]
            # set the current value as 0 to indicate we already visited the place
            grid[i][j] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                temp_gold_collected = max(
                    curr_val + get_gold(i=dx + i, j=dy + j), temp_gold_collected
                )

            # set back the current value changes
            grid[i][j] = curr_val
            return temp_gold_collected

        # initially assume max gold is 0
        max_gold_collected = 0
        # iterate over all the row and col
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    max_gold_collected = max(max_gold_collected, get_gold(i, j))

        return max_gold_collected


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
output = 24

grid = [
    [1, 0, 7, 0, 0, 0],
    [2, 0, 6, 0, 1, 0],
    [3, 5, 6, 7, 4, 2],
    [4, 3, 1, 0, 2, 0],
    [3, 0, 5, 0, 20, 0],
]
output = 60
print(Solution().getMaximumGold(grid))
