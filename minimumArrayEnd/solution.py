class Solution:
    '''
    TC: O(n)
    SC: O(1)
    
    GOT TLE

    '''
    def minEnd(self, n: int, x: int) -> int:
        # first element
        last_num = x

        for _ in range(1, n):
            last_num = x | (last_num + 1)

        return last_num
    
print(Solution().minEnd(n=3, x= 4))