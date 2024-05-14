from typing import List


class Solution:
    """
    Time and space complexity:
    ==========================
    n = no of rows
    m = no of columns

    TC: O(m * n) [for loop] + O(m*n) [recursion for each cell] ~ O((m*n) ^ 2) [quadratic time]
    SC: O(m * n) [recursion stack space]
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def get_gold(i: int, j: int):
            nonlocal m, n, grid, visited

            # add the current gold value to gold collected
            temp_gold_collected = grid[i][j]
            # mark the current place as visited
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                new_i = dx + i
                new_j = dy + j
                if (
                    0 <= new_i < n
                    and 0 <= new_j < m
                    and grid[new_i][new_j] != 0
                    and (new_i, new_j) not in visited
                ):

                    gold_collected = get_gold(new_i, new_j)
                    temp_gold_collected = max(
                        grid[i][j] + gold_collected, temp_gold_collected
                    )

            # unmark the current place as non visited for
            # other cells to explore the current i, j place
            visited.remove((i, j))

            return temp_gold_collected

        # initially assume max gold is 0
        max_gold_collected = 0
        # iterate over all the row and col
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    # Create an empty set for each new starting of gold collection
                    visited = set()

                    # collect the gold for current i, j
                    gold_collected = get_gold(i, j)
                    max_gold_collected = max(max_gold_collected, gold_collected)

        return max_gold_collected


class Solution: # more concise and optimized
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
            nonlocal m, n, grid, visited

            if not (
                0 <= i < n and 0 <= j < m and grid[i][j] != 0 and (i, j) not in visited
            ):
                return 0

            # add the current gold value to gold collected
            temp_gold_collected = grid[i][j]
            # mark the current place as visited
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                gold_collected = get_gold(dx + i, dy + j)
                temp_gold_collected = max(
                    grid[i][j] + gold_collected, temp_gold_collected
                )

            # unmark the current place as non visited for
            # other cells to explore the current i, j place
            visited.remove((i, j))

            return temp_gold_collected

        # initially assume max gold is 0
        max_gold_collected = 0
        # iterate over all the row and col
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    # Create an empty set for each new starting of gold collection
                    visited = set()

                    # collect the gold for current i, j
                    gold_collected = get_gold(i, j)
                    max_gold_collected = max(max_gold_collected, gold_collected)

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
