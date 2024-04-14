class Solution:
    """
    TC: O(nxm) [since we only visit one state at once]
    SC: O(nxm) [to store visited paths data]

    """

    def uniquePaths(self, m: int, n: int) -> int:

        def find_paths(i: int, j: int, visited) -> int:
            nonlocal m, n

            if i == m - 1 and j == n - 1:
                return 1  # found the end
            if i >= m or j >= n:
                return 0  # out of bounds
            if visited[i][j] != -1:
                return visited[i][j]  # already stored the path
            else:
                visited[i][j] = find_paths(i + 1, j, visited) + find_paths(
                    i, j + 1, visited
                )
                # return the sum of both right and down paths
                return visited[i][j]

        visited = [[-1 for _ in range(n)] for _ in range(m)]
        return find_paths(0, 0, visited)


m = 3
n = 7
output = 28
print(Solution().uniquePaths(m, n))
