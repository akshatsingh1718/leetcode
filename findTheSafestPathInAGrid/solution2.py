'''
Problem: https://leetcode.com/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2024-05-15
Solution: https://www.youtube.com/watch?v=8I0Z_eajcvs
'''

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # if first and last has thief then return 0 safeness
        if n > 0 and (grid[0][0] == 1 or grid[n - 1][m - 1] == 1):
            return 0

        isvalid_path = lambda x, y: 0 <= x < n and 0 <= y < m

        # find all the ones
        thieves_dist = [
            (i, j, 0) for i in range(n) for j in range(m) if grid[i][j] == 1
        ]

        # new matrix to store the safeness
        safeness = [[-1 for _ in range(m)] for _ in range(n)]

        for thief in thieves_dist:
            safeness[thief[0]][thief[1]] = 0

        # START THE MULTI BFS TRAVERSAL
        # add the safeness for each place
        while len(thieves_dist) > 0:
            new_dist = []
            for thief in thieves_dist:

                # move in all 4 directions
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = dx + thief[0], dy + thief[1]
                    # if the new i, j is valid and safeness is not yet decided
                    if isvalid_path(new_i, new_j) and safeness[new_i][new_j] == -1:
                        # add the new place where its safeness needs to be set
                        new_dist.append((new_i, new_j, thief[2] + 1))
                        safeness[new_i][new_j] = thief[2] + 1

            thieves_dist = new_dist

        # START THE BINARY SEARCH FOR SAFENESS
        low = 0
        high = n
        max_sf = 0

        def check(min_safeness: int):
            nonlocal safeness, isvalid_path
            # move from top left to bottom right

            path = [(0, 0)]
            visited = set((0, 0))
            while len(path) > 0:
                pt = path.pop()

                if pt[0] == n - 1 and pt[1] == m - 1:
                    return True

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = dx + pt[0], dy + pt[1]

                    # cell is valid and not visited yet
                    if isvalid_path(new_i, new_j) and (new_i, new_j) not in visited:

                        # safeness is not what we needed so skip
                        if safeness[new_i][new_j] < min_safeness:
                            continue
                        # safeness is what we needed and append to the path
                        # and mark as visit
                        path.append((new_i, new_j))
                        visited.add((new_i, new_j))

            return False

        while low <= high:
            min_safeness = low + (high - low) // 2

            if check(min_safeness):
                max_sf = max(min_safeness, max_sf)
                low = min_safeness + 1
            else:
                high = min_safeness - 1

        return max_sf


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # if first and last has thief then return 0 safeness
        if n > 0 and (grid[0][0] == 1 or grid[n - 1][m - 1] == 1):
            return 0

        isvalid_path = lambda x, y: 0 <= x < n and 0 <= y < m

        # find all the ones
        thieves_dist = [
            (i, j, 0) for i in range(n) for j in range(m) if grid[i][j] == 1
        ]

        # new matrix to store the safeness
        safeness = [[-1 for _ in range(m)] for _ in range(n)]

        for thief in thieves_dist:
            safeness[thief[0]][thief[1]] = 0

        # START THE MULTI BFS TRAVERSAL
        # add the safeness for each place
        while len(thieves_dist) > 0:
            new_dist = []
            for thief in thieves_dist:

                # move in all 4 directions
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = dx + thief[0], dy + thief[1]
                    # if the new i, j is valid and safeness is not yet decided
                    if isvalid_path(new_i, new_j) and safeness[new_i][new_j] == -1:
                        # add the new place where its safeness needs to be set
                        new_dist.append((new_i, new_j, thief[2] + 1))
                        safeness[new_i][new_j] = thief[2] + 1

            thieves_dist = new_dist

        # START THE BINARY SEARCH FOR SAFENESS
        low = 0
        high = n
        max_sf = 0

        def check(min_safeness: int):
            nonlocal safeness, isvalid_path
            # move from top left to bottom right

            path = [(0, 0)]
            visited = {(0, 0)}

            if safeness[0][0] < min_safeness:
                return False

            while len(path) > 0:
                pt = path.pop()

                if pt[0] == n - 1 and pt[1] == m - 1:
                    return True

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = dx + pt[0], dy + pt[1]

                    # cell is valid and not visited yet
                    if isvalid_path(new_i, new_j) and (new_i, new_j) not in visited:

                        # safeness is not what we needed so skip
                        if safeness[new_i][new_j] < min_safeness:
                            continue
                        # safeness is what we needed and append to the path
                        # and mark as visit
                        path.append((new_i, new_j))
                        visited.add((new_i, new_j))

            return False

        while low <= high:
            min_safeness = low + (high - low) // 2

            if check(min_safeness):
                max_sf = max(min_safeness, max_sf)
                low = min_safeness + 1
            else:
                high = min_safeness - 1

        return max_sf


# grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
# output = 2

# TS 2
# grid = [[0, 0, 1], [0, 1, 1], [0, 0, 0]]
# output = 1

# TS3
# grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
# output = 0


# TS4
# grid = [[0,1,1],
#         [1,1,1],
#         [1,1,0]]
# output =0


# TS 5
# grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
# output = 1


# TS 6
grid = [[0, 1, 1], [0, 1, 1], [1, 1, 0]]
output = 0


# TS 7
# grid = [[0, 1, 1],
#         [0, 0, 0],
#         [0, 0, 0]]
# output = 1


# TS 8
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
]
output = 5

# TS 9
grid = [[0, 1, 1], [0, 0, 0], [0, 0, 0]]
output = 1

print(Solution().maximumSafenessFactor(grid))
