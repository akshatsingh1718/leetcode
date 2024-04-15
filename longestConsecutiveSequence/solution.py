from typing import List


class Solution:
    """
    TC: O(N logN) [sort] + O(N) [for loop] = O(N log N) + O(N)
    SC: O(1)

    Note:
    1. Using sort we are distorting the array

    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()  # O(n logn)

        max_ctr = 1
        prv = float("-inf")
        ctr = 1

        for num in nums:
            # if the prv + 1 == num it means sequence is going on and update the counter
            if (num - 1) == prv:
                prv = num # update the prv to current
                ctr += 1 # inc the counter

            elif num != prv: 
                # if the current is not eq to prv meaning the seq got broked
                # even if the prv and num is eq it means they last element and current is same and seq is paused but not breaked. so do not inc the counter
                # if the prv + 1 == num it means sequence is going on and update the counter
                # But here it does not follow anything sequential so we reset the counter and prv became the current to check for
                # the next seq
                ctr = 1
                prv = num

            max_ctr = max(ctr, max_ctr)
        return max_ctr


# TS1
# nums = [100, 4, 200, 1, 3, 2]
# output = 4

# TS2
nums = []
output = 0


# TS3
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
output = 9


print(Solution().longestConsecutive(nums))
