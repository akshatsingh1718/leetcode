from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()

        n = len(s)
        l = 0
        r = 0
        max_length = 0
        curr_length = 0

        while l <= r < n:

            # remove duplicate till r
            while s[l] in visited and l < n and l <= r:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])


    

s = "abcabcbb"
output = 3

# TS2
# s = "pwwkew"
# output= 3

# TS3
# s = "bbbbb"
# output= 1

# TS4
# s = "b"
# output= 1

# TS5
# s = "cdd"
# output = 2

# TS6
# s = "dvdf"
# output= 3

# TS7
# s = "abba"
# output= 2


print(Solution().lengthOfLongestSubstring(s))