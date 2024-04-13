from typing import List

class Solution:
    '''
    TC: O(n) [for loop]
    SC: O(n) [freq dict]
    '''
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = dict()

        for i, ele in enumerate(nums):

            freq[ele] = 1 if freq.get(ele) is None else (freq[ele] + 1)
            if freq[ele] == (n // 2) + (n % 2):
                return ele
            




nums = [3,2,3]
Output =  3
print(Solution().majorityElement(nums))