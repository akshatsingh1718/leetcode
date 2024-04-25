class Solution:
    """
    TC: O(n * n)
    SC: O(n)
    """

    def longestIdealString(self, s: str, k: int) -> int:

        arr = [0 for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):

            max_val = 0
            for j, _ in enumerate(s[i + 1 :], start=i + 1):
                if abs(ord(s[j]) - ord(s[i])) <= k:
                    max_val = max(max_val, arr[j])

            arr[i] += max_val + 1

        return max(arr)

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
output = 5

print(Solution().longestIdealString(s, k))
