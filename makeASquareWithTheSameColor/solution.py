from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        n = len(grid)
        m = len(grid[0])

        for i in range(n - 1):
            for j in range(m - 1):
                score_of_W = 0

                if grid[i][j] == "W":
                    score_of_W += 1
                else:
                    score_of_W -= 1

                if grid[i + 1][j] == "W":
                    score_of_W += 1
                else:
                    score_of_W -= 1

                if grid[i][j + 1] == "W":
                    score_of_W += 1
                else:
                    score_of_W -= 1

                if grid[i + 1][j + 1] == "W":
                    score_of_W += 1
                else:
                    score_of_W -= 1

                if score_of_W != 0:
                    return True
        return False


# TS1
grid = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
output = True

# TS2
grid = [["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]
output = False

# TS3
grid = [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]
output = True


print(Solution().canMakeSquare(grid))
