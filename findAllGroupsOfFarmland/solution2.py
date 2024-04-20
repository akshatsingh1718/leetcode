from typing import List

class Solution:
    '''
    TC: O(m x n)
    '''
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        coords = []
        visited = set() # using a list instead of set will throw a TLE

        # Iterate over each item and find the land starting
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (i, j) not in visited:
                    max_x, max_y = i, j
                    stack = [(i, j)]
                    while len(stack) > 0:
                        x, y = stack.pop()

                        # for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        for dx, dy in [(1, 0), (0, 1)]:

                            nx, ny = dx + x, dy + y

                            if (
                                (0 <= nx < n)
                                and (0 <= ny < m)
                                and (nx, ny) not in visited
                                and land[nx][ny] != 0
                            ):
                                visited.add((nx, ny))
                                stack.append((nx, ny))

                                max_x = max(max_x, nx)
                                max_y = max(max_y, ny)

                    coords.append([i, j, max_x, max_y])

        return coords

# TS1
land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
output = [[0, 0, 0, 0], [1, 1, 2, 2]]

# TS2
# land = [[1, 1], [1, 1]]
# output = [[0, 0, 1, 1]]

# TS3
# land = [[0]]
# output= []

print(Solution().findFarmland(land))
