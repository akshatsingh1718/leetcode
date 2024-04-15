from typing import List


class Solution:
    '''
    TC: O(N) [adding to set] + O(N) [for loop] + O(N) [finding the next of the sequence] = O(3N)
    SC: O(N) [set]

    Algo:
    1. Add all the elements to the set.
    2. Iterate over items in nums and check if (item - 1) element is present in set or not. If present it means there is another element which is starting the sequence and we continue with the next iteration. If the (item-1) is not present in the set it means that current item can be a starting point of some sequence and we check for (item + 1, item+2, ... item + n) in set till we cannot find the element in the set where our sequence will also break. This loop till n elements will give the count as n since we can find the sequence maintaining till nth element.
    3.update the maximun if new max found using counter.
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        seq_ctr = 0
        max_ctr = 0
        for n in nums:
            if (n - 1) in nums_set:
                continue

            j = n + 1
            seq_ctr = 1 # num can make its own independent consecutive pair

            while j in nums_set:
                seq_ctr += 1
                j += 1

            max_ctr = max(seq_ctr, max_ctr)

        return max_ctr


# TS1
nums = [100, 4, 200, 1, 3, 2]
output = 4

nums = []
output = 0

print(Solution().longestConsecutive(nums))
