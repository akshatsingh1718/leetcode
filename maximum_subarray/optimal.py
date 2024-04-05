from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)

        Solution:
        Kadane's solution

        1. Iterate over items and start with zero running mean and max_value of -inf
        2. Add the current iterating item to running_mean and if its gt max_value then update max_value.
        3. If the running_mean is lt 0 meaning negative value then set it again to zero. Why this? because if our running_mean goes negative it is indicating its not worth to carry the negative values further as even if we have a very big number earlier in the array but some values cancels it and does not give any value to futhrer numbers. Even if the next numbers coming are not bigger than the prv number which has been canceled by the negatives we still have that number as max_val stores the max sum of subarry as subarray can be a single num as well.
        """

        max_val = float("-inf")
        running_sum = 0  # dont let this go negative

        for i in range(len(nums)):

            running_sum += nums[i]

            if running_sum > max_val:
                max_val = running_sum
            if running_sum < 0:
                running_sum = 0

        # return max(0, max_val) # if there are no max subarry then return 0
        return max_val

    def findMaxSubarray(self, nums: List[int]) -> List[int]:

        max_val = float("-inf")
        curr_sum = 0

        start = -1
        ans_start, ans_end = -1, -1

        for i in range(len(nums)):

            # if curr_sum is 0 meaning we may start a subarray
            if curr_sum == 0:
                start = i

            curr_sum += nums[i]

            if curr_sum > max_val:
                max_val = curr_sum

                ans_start = start
                ans_end = i

            curr_sum = max(0, curr_sum)

        return max_val, nums[ans_start : ans_end + 1]


i = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
o = [4, -1, 2, 1]
max_val, ans = Solution().findMaxSubarray(i)

print(f"{max_val = }")
print(f"{ans = }")
