class Solution:
    '''
    No the solution that was expected.

    Algo:
    1. Iterate over array.
    2. Remove consecutive n numbers to find out the min of the array
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        curr_min = num[k:n]

        for i in range(n):
            sub = num[0:i] + num[i+k:n]
            if sub < curr_min:
                curr_min = sub

            sub = num[0:n-k-i] + num[n - i:]
            if sub < curr_min:
                curr_min = sub



        while len(sub) > 0:
            if sub[0] == "0":
                sub = sub[1:]

        return curr_min if len(curr_min) > 0 else "0"
    


num = "1432219"
k = 3
output= "1219"

print(Solution().removeKdigits(num= num, k=k))