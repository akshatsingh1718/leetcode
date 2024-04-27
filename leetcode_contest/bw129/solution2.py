from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        counts = 0
        n, m = len(grid), len(grid[0])

        below_total_ones = [0 for _ in range(m)]
        below_right_angle_made = [0 for _ in range(m)]

        for i in range(n - 1, -1, -1):
            total_ones_on_right_side = 0
            for j in range(m - 1, -1, -1):

                if grid[i][j] == 1:
                    # print(f"========={i, j}==============")
                    # print(f"{below_total_ones=}")
                    # print(f"{total_ones_on_right_side=}")
                    # print(f"{below_right_angle_made=}")



                    if total_ones_on_right_side > 0:
                        counts += (below_total_ones[j] + total_ones_on_right_side - 1)
                        below_right_angle_made[j] += 1

                    elif below_right_angle_made[j] > 0:
                        counts += below_right_angle_made[j]

                    if total_ones_on_right_side > 0 and 

                    total_ones_on_right_side += 1
                    below_total_ones[j] += 1
                    # print(f"{counts =}")

        return counts


# grid = [[0, 1, 0], [0, 1, 1], [0, 1, 0]]
# output = 2

# grid = [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
# output = 0


# grid = [[1, 0, 1], 
#         [1, 0, 0], 
#         [1, 0, 0]]
# output = 2

print(Solution().numberOfRightTriangles(grid))
