from typing import List


class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def findMaxK(self, nums: List[int]) -> int:
        curr_max = -1 # store -1 as initial current max value
        visited = dict() # for visited elements

        # Iterate over all the elements
        for num in nums:
            # if we have already seen contrasted value of num in visited then it
            # is definitely forming a pair of (-val, +val).
            # Also check that absolute value (+val) of num is greater than current max
            if visited.get(-num, None) is not None and abs(num) > curr_max:
                # Store the value in curr max
                curr_max = abs(num)

            # add the num into our visited elements
            visited[num] = True

        # return the current max
        return curr_max


nums = [-1, 2, -3, 3]
Output = 3

# nums = [-1, 10, 6, 7, -7, 1]
# output = 7

nums = [-10,8,6,7,-2,-3]
output= -1

print(Solution().findMaxK(nums))
