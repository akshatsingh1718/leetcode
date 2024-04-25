# Reference: https://www.youtube.com/watch?v=3AlOK4t-Q3I

class Solution:
    '''
    TC: O(n * 26) [n i's will store the indexes and their previous element will be 26 at max]
    SC: O(n * 26)

    Algo (recursion):
    This will throw Memory error
    '''
    def longestIdealString(self, s: str, k: int) -> int:

        cache = dict()

        def dfs(i: int, prv: str):
            nonlocal cache, s

            if i == len(s):
                return 0

            if (i, prv) in cache:
                return cache[(i, prv)]

            res = dfs(i + 1, prv) # skip s[i]

            if prv == "" or abs(ord(s[i]) - ord(prv)) <= k:
                # adding one since we are including the current character with prv character
                res = max(res, 1 + dfs(i + 1, s[i]))  # include s[i]

            cache[(i, prv)] = res
            return res
        
        return dfs(0, "")


# TS1
s = "acfgbd"
k = 2
output = 4

# TS2
s = "abcd"
k = 3
output = 4

# TS3
s = "fabzcd"
k = 2

# TS4
s = "eduktdb"
k = 15

print(Solution().longestIdealString(s, k))
