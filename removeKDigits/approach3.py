from functools import cache

class Solution:
    """
    TLE
    """
    def removeKdigits(self, num: str, k: int) -> str:

        def find_min(num_str:str, curr_min: str, no_to_remove: int, mem: dict):

            if no_to_remove == 0:
                return num_str
            
            for i, ele in enumerate(num_str):
                if i != 0:
                    if ele == num_str[i - 1]:
                        continue # if same as prv number

                if mem.get(num_str[:i]+num_str[i+1:]) is not None:
                    curr_min = mem[num_str[:i]+num_str[i+1:]]
                else:
                    curr_min = min(curr_min, find_min(num_str[:i]+num_str[i+1:], curr_min, no_to_remove -1, mem))
                    mem[num_str[:i]+num_str[i+1:]] = curr_min

            return curr_min
        
        return find_min(num, num[k:], k, {}).lstrip("0") or "0"

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