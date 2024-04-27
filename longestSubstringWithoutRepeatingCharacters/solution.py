from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = dict()

        max_length = 0
        running_length = 0

        for idx, char in enumerate(s):

            if visited.get(char) is not None:
                max_length = max(max_length, running_length)
                running_length = running_length - visited[char]
            else:
                running_length += 1

            visited[char] = idx
            
        return max(running_length, max_length)
    

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