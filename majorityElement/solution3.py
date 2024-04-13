from typing import List

class Solution:
    '''
    
    Algo: (Moore Voting Algo)
    '''
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        candidate = 0

        for i in range(n):

            if count == 0:
                candidate = nums[i]

            if candidate == nums[i]: count += 1
            else: count -= 1

            if count > (n // 2): return candidate

        return candidate


nums = [3,2,3]
Output =  3
print(Solution().majorityElement(nums))