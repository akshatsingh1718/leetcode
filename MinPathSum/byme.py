from typing import List
import numpy as np


class Solution:
    """
    https://leetcode.com/problems/minimum-path-sum/description/
    """

    def reachToBottom(self, x, y, grid, visited):
        """
        My Thought process

        visited will contain the min path from the its elements to the bottom
        if already visited the node then no need to recurse more and check for
        its min of right and down path
        """
        # print(f"Visiting {x, y}")
        n, m = len(grid), len(grid[0])

        if x == n - 1 and y == m - 1:
            visited[x][y] = grid[x][y]
            return grid[x][y]

        down_x, down_y = x + 1, y
        right_x, right_y = x, y + 1
        right_sum, down_sum = float("inf"), float("inf")

        if 0 <= down_x < n and 0 <= down_y < m:
            if visited[down_x][down_y] == -1:
                down_sum = self.reachToBottom(down_x, down_y, grid, visited)
                visited[down_x][down_y] = down_sum
            else:
                down_sum = visited[down_x][down_y]

        if 0 <= right_x < n and 0 <= right_y < m:
            if visited[right_x][right_y] == -1:
                right_sum = self.reachToBottom(right_x, right_y, grid, visited)
                visited[right_x][right_y] = right_sum
            else:
                right_sum = visited[right_x][right_y]

        return min(right_sum + grid[x][y], down_sum + grid[x][y])

    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        visited = [[-1] * m for _ in range(n)]

        res = self.reachToBottom(0, 0, grid, visited)

        return res


def main():
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # output = 7

    grid = [[1, 2, 3], [4, 5, 6]]
    output = 12

    s = Solution()
    res = s.minPathSum(grid)
    print(f"{res = }")
    print(f"{output = }")


main()
