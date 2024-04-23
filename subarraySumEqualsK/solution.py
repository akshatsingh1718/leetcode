from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        element_last_fount_at = dict()
        count = 0
        running_sum = 0

        for i, ele in enumerate(nums):
            running_sum += ele


            if element_last_fount_at.get(running_sum - k) is not None:
                element_last_fount_at[running_sum] = i
                count += 1

            # check at last for current running sum
            # if running_sum == k:
            #     element_last_fount_at[running_sum] = i
            #     count += 1
            # if the curr sum is not eq to k and 
            # we cannot find any value which can make
            # curr sum
            else:
                element_last_fount_at[running_sum] = i

        return count


# TS1
nums = [1, 1, 1]
k = 2
output = 2

# TS2
# nums = [1, 2, 3]
# k = 3
# output = 2

# TS3
# nums = [1, -1, 0]
# k = 0
# output = 3

# TS4
nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
output = 55

print(Solution().subarraySum(nums, k))
