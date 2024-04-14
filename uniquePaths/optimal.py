class Solution:
    """
    TC: O(n-1) or O(m-1)
    SC: O(1)

    """

    def uniquePaths(self, m: int, n: int) -> int:

        N = m + n - 2
        R = m - 1  # or n - 1 (if we go right first as n is horizontal array length)

        result = 1
        for i in range(1, R + 1):
            result *= (N - R + i) / i

        return round(result)

 
# TS1
m = 3
n = 7
output = 28

# TS2
# m = 2
# n = 3
# output= 3

# TS3
m = 10
n = 10
output = 48620
print(Solution().uniquePaths(m, n))
