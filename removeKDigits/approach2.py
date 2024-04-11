from functools import cache

class Solution:
    """
    TLE
    """
    def removeKdigits(self, num: str, k: int) -> str:

        @cache
        def find_min(num_str:str, curr_min: str, no_to_remove: int):
            if no_to_remove == 0:
                return min(num_str, curr_min)
            
            for i in range(len(num_str)):
                curr_min = min(curr_min, find_min(num_str[:i]+num_str[i+1:], curr_min, no_to_remove -1))

            return curr_min
        
        result = find_min(num, num[k:], k)
        return  str(int(result)) if len(result) > 0 else  "0"

# TS1
num = "1432219"
k = 3
output= "1219"

# TS2
# num = "10001"
# k = 4
# output = "0"

# TS3
# num = "10"
# k = 2
# output = "0"

# TS3
num = "10200"
k = 1
output = "200"

print(Solution().removeKdigits(num= num, k=k))