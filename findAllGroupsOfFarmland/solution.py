from typing import List


class Solution:
    """
    TC: O( m x n)
    SC: O(4 x (mxn)//2) [4 coords and worst case when land is like a chess board]
    """
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        coords = []

        def dfs(i: int, j: int, coord: tuple):
            nonlocal land, m, n

            # if the land is already seen or just forest return the coords we get
            if not (0 <= i < n) or not (0 <= j < m) or land[i][j] == 0:
                return coord

            # if the land is farmland (not visited) then mark the land as visited
            land[i][j] = 0

            # find the max of current coord (i, j) and the max till we have found which is coord 
            coord = max(coord, (i, j))

            # find the land in all 4 directions and find out the farthest to the down right land
            coord = max(dfs(i + 1, j, coord), coord)
            coord = max(dfs(i, j + 1, coord), coord)
            # no need to check for up and left as the farm is square and we have already find
            # the starting point so no need to go up and left
            # coord = max(dfs(i, j - 1, coord), coord)
            # coord = max(dfs(i - 1, j, coord), coord)

            return coord

        # Iterate over each item and find the land starting
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    # find the land ending coords
                    coord = dfs(i, j, coord=(i, j))
                    # (i, j) will be the starting of the land
                    coords.append([i, j, coord[0], coord[1]])

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
