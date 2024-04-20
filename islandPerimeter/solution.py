from typing import List


class Solution:
    '''
    TC Should be given to this

    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        stack = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            if len(stack) > 0:
                break

        perimeter = 0
        visited = []
        while len(stack) > 0:

            i, j = stack.pop(0)
            if (i, j) not in visited:
                visited.append((i, j))
            else:
                continue
            
            # top
            if i - 1 == -1 or (grid[i - 1][j] == 0):
                perimeter += 1
            else:
                stack.append((i - 1, j))

            # bottom
            if i + 1 == n or (grid[i + 1][j] == 0):
                perimeter += 1
            else:
                stack.append((i + 1, j))

            # right
            if j + 1 == m or (grid[i][j + 1] == 0):
                perimeter += 1
            else:
                stack.append((i, j + 1))

            # left
            if j - 1 == -1 or (grid[i][j - 1] == 0):
                perimeter += 1
            else:
                stack.append((i, j - 1))

        return perimeter


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        stack = []

        # find the first land
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            if len(stack) > 0:
                break

        perimeter = 0
        visited = []
        while len(stack) > 0:

            i, j = stack.pop(0)
            if (i, j) not in visited:
                visited.append((i, j))
            else:
                continue
            
            # top
            if i - 1 == -1 or (grid[i - 1][j] == 0):
                perimeter += 1
            # else:
                # stack.append((i - 1, j))

            # bottom
            if i + 1 == n or (grid[i + 1][j] == 0):
                perimeter += 1
            else:
                stack.append((i + 1, j))

            # right
            if j + 1 == m or (grid[i][j + 1] == 0):
                perimeter += 1
            else:
                stack.append((i, j + 1))

            # left
            if j - 1 == -1 or (grid[i][j - 1] == 0):
                perimeter += 1
            else:
                stack.append((i, j - 1))

        return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
output = 16
print(Solution().islandPerimeter(grid))
