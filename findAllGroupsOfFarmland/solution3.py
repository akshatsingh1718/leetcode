from typing import List


class Solution:
    """
    TC: O(n x m x ( (m+n) // 2) ) [to verify i and j for each coor in coords]
    SC: (m+n) // 2 [coords length]
    """

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        coords = []
        # Iterate over each item and find the land starting
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and (
                    len(coords) == 0
                    or not any(
                        [((c[0] <= i <= c[2]) and (c[1] <= j <= c[3])) for c in coords]
                    )
                ):

                    temp_j = j + 1
                    while temp_j < m and land[i][temp_j] == 1:
                        temp_j += 1

                    temp_i = i + 1
                    while temp_i < n and land[temp_i][j] == 1:
                        temp_i += 1

                    width_j = temp_j - 1 - j
                    width_i = temp_i - 1 - i

                    coords.append([i, j, i + width_i, j + width_j])

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

# TS4
# land = [[0, 1],
#         [1, 0]]
# output = [[0, 1, 0, 1], [1, 0, 1, 0]]

# TS5
land = [[1, 1], [0, 0]]
# output= [[0,0,0,1]]


print(Solution().findFarmland(land))
