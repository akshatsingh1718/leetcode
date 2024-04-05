from typing import List

class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Algo:
        1. Sort the array
        2. Find out the corresponding same item
        '''

        nums.sort() # inplace operation

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
             
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Algo:
        1. Since the numers are from 1-n, create a freq array and which has already a 1 in its position its the item we are looking for.
        '''
        n = len(nums)

        freq = [0] * (n)
        for i in range(n):
            if freq[nums[i]] == 0:
                freq[nums[i]] += 1
            else:
                return nums[i]


nums = [1,3,4,2,1]
Output= 2

res = Solution2().findDuplicate(nums)

print(res)



