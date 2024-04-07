class Solution:
    '''
    Done by me
    TC: O(n) [find unmatching parenthesis] + O(n)[remove unmatching parenthesis] + O(n) [find in stack for index] ~ O(n)
    SC: O(n) [stack] + O(n) [store result] ~ O(n)
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = list()

        # FIND THE UNMATCHING PARENTHESIS
        for i, ele in enumerate(s):
            if ele == "(":
                stack.append((ele, i))
                continue

            if ele == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((ele, i))

        # remove the indexes
        res_str = ""
        for i, ele in enumerate(s):
            for j in stack:
                if i == j[1]:
                    break
            else:
                res_str += ele

        return res_str
    
# testcase 1
# s = "lee(t(c)o)de)"
# output = "lee(t(c)o)de"

# testcase 2
# s = "a)b(c)d"
# output= "ab(c)d"

# testcase 3
# s = "))(("
# output= ""

# testcase 4
s = "a(b(c)d"
output= "ab(c)d"

res = Solution().minRemoveToMakeValid(s)
print(res)