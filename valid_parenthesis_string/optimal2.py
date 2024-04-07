"""
Resources: 

Leetcode Sol: https://gist.github.com/SuryaPratapK/7d82ab4579a93ed9067eb5702e964650
Youtube: https://www.youtube.com/watch?v=KuE_Cn3xhxI&t=16s
"""

from typing import List

class Solution:
    '''
    TC: O(n) [close all the close brackets] + O(n) [close all the open brackets] ~ O(n)
    SC: O(n) [Open Brackets + Star elements]
    
    Algo: (STACK)
    1. Create 2 Stacks for open bracket and star.
    2. Add index of open bracket and star in their respective stacks. For open if closed found then pop index from open stack.
    3. Now, after adding both the {open, star} bracket close the remaning open bracket in open stack by iterating from left to right and checking for higher index in star stack as closing a bracket with index i can only be closed by star of index greater than i.
    '''


    def checkValidString(self, s: str) -> bool:
        n = len(s)

        open_stack =  []
        star_stack = []

        # Close all the close bracket
        for i, ele in enumerate(s):
            if ele == "(":
                open_stack.append(i)
            elif ele == ")":
                # No need to check for `open_stack[-1] < i` as i will always be greater than element idx added before it
                # if len(open_stack) > 0 and open_stack[-1] < i:
                if len(open_stack) > 0:
                    open_stack.pop() # remove the last opening bracket stack element
                elif len(star_stack) > 0:
                    star_stack.pop() # remove the last star stack element as it acts as opening bracket
                else:
                    # if both the stacks are empty meaning bracket cannot be closed
                    return False
            else:
                # Case of *
                star_stack.append(i) 

        # Close all the open bracket
        while len(open_stack) != 0:
            if len(star_stack) == 0:
                return False
            elif star_stack[-1] > open_stack[-1]:
                star_stack.pop()
                open_stack.pop()
            else:
                return False
            
        return True

# (2, 0)
# ( = 0 
# ) = 1
# _ = 2
s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
output = True
res = Solution().checkValidString(s)
print(res)
