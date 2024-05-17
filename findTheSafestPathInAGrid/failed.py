from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        if n > 0 and (grid[0][0] == 1 or grid[n - 1][m - 1] == 1):
            return 0
        isvalid_path = lambda x, y: 0 <= x < n and 0 <= y < m


        manhattan_distance = [[0 for _ in range(m)] for _ in range(n)]
        # safety_distance = [[0 for _ in range(m)] for _ in range(n)]

        # find all the ones
        ones = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ones.append((i, j))

        find_manhattan = lambda pt1, pt2: abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

        for i in range(n):
            for j in range(m):

                safety_val = 0 if len(ones) == 0 else float("inf")
                for one in ones:
                    safety_val = min(safety_val, find_manhattan((i, j), one))

                # safety_distance[i][j] = n - 1 - safety_val
                # manhattan_distance[i][j] = safety_val if safety_val > 0 else 1
                manhattan_distance[i][j] = safety_val


        i, j = 0, 0

        safeness = float("inf")

        while i != n and j != m:
            safeness = min(manhattan_distance[i][j], safeness)
            print(f"{i, j}", "dt=", manhattan_distance[i][j], f"{safeness=}")

            # check for down
            down_i = i + 1
            down_j = j

            # check for right
            right_i = i
            right_j = j + 1

            # if both the paths are valid then get the path which will
            # be the max manhattan distance
            if isvalid_path(down_i, down_j) and isvalid_path(right_i, right_j):
                # choose down if down distance is gt
                if (
                    manhattan_distance[down_i][down_j]
                    > manhattan_distance[right_i][right_j]
                ):
                    i = down_i
                    j = down_j
                else:
                    i = right_i
                    j = right_j

            elif isvalid_path(down_i, down_j):
                i = down_i
                j = down_j
            else:
                i = right_i
                j = right_j

        for row in manhattan_distance:
            print(row)

        return safeness


grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
output = 2

# TS 2
grid = [[0, 0, 1], 
        [0, 1, 1], 
        [0, 0, 0]]
output = 1

# TS3
# grid = [[1,0,0],
#         [0,0,0],
#         [0,0,1]]
# output = 0


# TS4
# grid = [[0,1,1],
#         [1,1,1],
#         [1,1,0]]
# output =0



print(Solution().maximumSafenessFactor(grid))
