from typing import List


class Solution:

    def makeRotten(self, grid: List[List[int]], visited: list, counter: list):
        '''
        Runtime
        Details
        65ms 
        Beats 33.99%of users with Python3
        Memory
        Details
        16.45MB
        Beats 22.51%of users with Python3
        '''
        q = list()
        n, m = len(grid) - 1, len(grid[0]) - 1

        xy_temp_list = []
        for i in range(n + 1):
            for j in range(m + 1):
                if grid[i][j] == 2:
                    xy_temp_list.append((i, j))

        if len(xy_temp_list) > 0:
            q.append(xy_temp_list)

        while len(q) > 0:
            xy_list = q.pop(0)

            does_rotten = False

            xy_temp_list = []

            for x, y in xy_list:
                # top
                if grid[max(0, x - 1)][y] == 1 and (max(0, x - 1), y) not in visited:
                    visited.append((max(0, x - 1), y))
                    xy_temp_list.append((max(0, x - 1), y))
                    grid[max(0, x - 1)][y] = 2
                    does_rotten = True

                # bottom
                if grid[min(n, x + 1)][y] == 1 and (min(n, x + 1), y) not in visited:
                    visited.append((min(n, x + 1), y))
                    xy_temp_list.append((min(n, x + 1), y))
                    grid[min(n, x + 1)][y] = 2
                    does_rotten = True

                # left
                if grid[x][max(0, y - 1)] == 1 and (x, max(0, y - 1)) not in visited:
                    visited.append((x, max(0, y - 1)))
                    xy_temp_list.append((x, max(0, y - 1)))
                    grid[x][max(0, y - 1)] = 2
                    does_rotten = True

                # right
                if grid[x][min(m, y + 1)] == 1 and (x, min(m, y + 1)) not in visited:
                    visited.append((x, min(m, y + 1)))
                    xy_temp_list.append((x, min(m, y + 1)))
                    grid[x][min(m, y + 1)] = 2
                    does_rotten = True

            if len(xy_temp_list) > 0:
                q.append(xy_temp_list)

            if does_rotten:
                counter[0] += 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = []

        n, m = len(grid), len(grid[0])

        counter = [0]

        self.makeRotten(grid, visited, counter)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return counter[0]


def main():
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # output = -1

    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # output = 4

    grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
    output = 2

    s = Solution()

    res = s.orangesRotting(grid)
    print(res)

    assert output == res, "Not Matching"


main()
