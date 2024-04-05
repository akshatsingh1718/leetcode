from typing import List


class Solution:
    """
    Runtime
    Details
    60ms
    Beats 54.20%of users with Python3
    Memory
    Details
    16.34MB
    Beats 59.63%of users with Python3
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]  # copy of grid

        q = list()  # ( (x, y), time)


        # total non rotten count to check if all the apples has been rotten or not
        total_non_rotten = 0

        # iterate over whole grid and add starting point to the queue and make them visited
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))  # at time 0; starting point of rottening
                    visited[i][j] = 2 # copy the rotten to the visited matrix
                else:
                    visited[i][j] = 0 # if not visited make them 1

                if grid[i][j] == 1:  # count non rotten tomatoes
                    total_non_rotten += 1

        counter = 0 # counter for counting how many apples has been rotten
        total_time = 0 # count total time

        while len(q) > 0:
            (x, y), time = q.pop(0)

            print(f"=====> Popped: {x, y} ; time = {time}")

            total_time = max(total_time, time)


            # iterate over all 4 directions
            for delrow, delcol in zip([-1, 0, +1, 0], [0, +1, 0, -1]):
                row = x + delrow
                col = y + delcol

                # if the row and col are in the range of matrix, and
                # if row and col is not rotten and 
                # if row and col is an orange and not empty place
                if (
                    0 <= row < n
                    and 0 <= col < m
                    and visited[row][col] != 2
                    and grid[row][col] == 1
                ):
                    print(f"Q={row, col} => {delrow=} | {delcol=}")
                    q.append(((row, col), time + 1)) # append the neighbour to queue with increased time step
                    visited[row][col] = 2  # make rotten
                    counter += 1 # increaser the new rotten items counter

        if counter != total_non_rotten: # if we have not rotten all the oranges 
            return -1

        return total_time


def main():
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # output = -1

    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    output = 4

    # grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
    # output = 2

    s = Solution()

    res = s.orangesRotting(grid)
    print(res)

    assert output == res, "Not Matching"


main()
