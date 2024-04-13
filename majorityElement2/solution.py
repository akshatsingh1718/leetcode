from typing import List

class Solution:

    '''
    TC: O(n)
    SC: O(n) + O(2)
    '''
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3

        freq = dict()
        res = set()

        for num in nums:
            freq[num] = (freq[num] + 1) if freq.get(num) else 1
            if freq[num] > threshold:
                res.add(num)

        return list(res)

nums = [3,2,3]
output= [3]
print(Solution().majorityElement(nums))