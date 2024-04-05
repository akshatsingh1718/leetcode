from typing import List
import numpy as np


class Solution:
    """
    https://leetcode.com/problems/minimum-path-sum/description/
    """

    def reachToBottom(self, x, y, grid):
        '''
        Starting from bottom right -> top left
        '''

        # if reached to the top left the return the value
        if x == 0 and y == 0:
            return grid[0][0]
        
        # if pos is going out of the grid
        if x < 0 or y < 0:
            return float("inf")

        


    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = self.reachToBottom2(n- 1, m - 1, grid)

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
