"""
If the no of left parenthesis are less than no of right parenthesis it means the sequence is invalid and we can never recover from that state even if we are more left parenthesis ahead.
"""

from typing import List

class Solution:
    '''
    TC: O(3^N) [Three possiblities at each N position in worst case where all the elements are * which can take <Empty-Space>, <Open-Parenthesis>, <Close-Parenthesis>]
    
    SC:

    Algo: (DP + Recursion)
    1.  
    '''


    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        # old cache: Error was all the -1 were referring to the same memory location hence changing one element eg.- cache[i][j] will change all the cache[i][0->n]
        # cache = [[-1] * n ] * n
        # new cache 
        cache = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(i: int, bal: int) -> bool:
            nonlocal cache, s

            if i >= len(s):
                return bal == 0

            if bal < 0:
                return False

            if cache[i][bal] != -1:
                return cache[i][bal]

            is_good = False
            if s[i] == "(":
                is_good |= solve(i + 1, bal + 1)
            elif s[i] == ")":
                is_good |= solve(i + 1, bal - 1)
            else:
                is_good |= solve(i + 1, bal + 1)  # assume (
                is_good |= solve(i + 1, bal - 1)  # assume )
                is_good |= solve(i + 1, bal)  # assume blank

            cache[i][bal] = is_good
            return is_good

        return solve(0, 0)

# (2, 0)
# ( = 0 
# ) = 1
# _ = 2
s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
output = True
res = Solution().checkValidString(s)
print(res)
