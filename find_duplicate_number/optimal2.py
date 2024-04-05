from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Algo: Tortoise and Hare Problem | Floyd's cycle detection
        '''

        def slow_inc(a, idx):
            return a[idx]
        
        def fast_inc(a, idx):
            next_idx = a[idx]
            return a[next_idx]

        slow= slow_inc(nums, nums[0])
        fast = fast_inc(nums, nums[0])

        while slow != fast:
 
            slow = slow_inc(nums, slow)
            fast = fast_inc(nums, fast)

        # Start new pointer from starting
        slow2 = nums[0]
        while slow != slow2:
            slow = slow_inc(nums, slow)
            slow2 = slow_inc(nums, slow2)

        return slow


nums = [2,5,9,6,9,3,8,9,7,1]
Output= 9


res = Solution().findDuplicate(nums)

print(res)



