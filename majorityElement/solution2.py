from typing import List

class Solution:
    '''
    TC: (n logn)
    SC: O(1)
    '''
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]



nums = [3,2,3]
Output =  3
print(Solution().majorityElement(nums))