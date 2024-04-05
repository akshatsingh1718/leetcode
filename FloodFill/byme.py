from typing import *

"""
https://leetcode.com/problems/flood-fill/

Runtime
Details
70ms
Beats 90.09%of users with Python3
Memory
Details
16.54MB
Beats 43.37%of users with Python3
"""


class Solution:
    def bfs(self, image, sr, sc, color, truthy_value):
        q = list()
        q.append((sr, sc))
        visited = list()
        visited.append((sr, sc))

        n, m = len(image) - 1, len(image[0]) - 1

        while len(q) > 0:
            x, y = q.pop(0)

            # middle top
            if (
                image[max(0, x - 1)][y] == truthy_value
                and (max(0, x - 1), y) not in visited
            ):
                image[max(0, x - 1)][y] = color
                visited.append((max(0, x - 1), y))
                q.append((max(0, x - 1), y))

            # middle bottom
            if (
                image[min(n, x + 1)][y] == truthy_value
                and (min(n, x + 1), y) not in visited
            ):
                image[min(n, x + 1)][y] = color
                visited.append((min(n, x + 1), y))
                q.append((min(n, x + 1), y))

            # middle left
            if (
                image[x][max(0, y - 1)] == truthy_value
                and (x, max(0, y - 1)) not in visited
            ):
                image[x][max(0, y - 1)] = color
                visited.append((x, max(0, y - 1)))
                q.append((x, max(0, y - 1)))

            # middle right
            if (
                image[x][min(m, y + 1)] == truthy_value
                and (x, min(m, y + 1)) not in visited
            ):
                image[x][min(m, y + 1)] = color
                visited.append((x, min(m, y + 1)))
                q.append((x, min(m, y + 1)))

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        self.bfs(image, sr, sc, color, image[sr][sc])
        image[sr][sc] = color

        return image


def main():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2

    s = Solution()
    res = s.floodFill(image, sr, sc, color)
    print(res)


main()
