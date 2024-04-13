from typing import List

# reference: https://leetcode.com/problems/majority-element-ii/solutions/5012760/video-how-we-think-about-a-solution-boyer-moore-majority-vote-algorithm/

class Solution:
    """
    TC: O(2n) [2 for loops]
    SC: O(2) [for res]


    Algo: (Boyer-Moore Majority Vote Algorithm)
    1. At max only two numbers can be on majority for n // 3
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3

        count1 = count2 = candidate1 = candidate2 = 0

        for num in nums:
            # if num is same element as 1 then inc count1
            if num == candidate1:
                count1 += 1
            # if num is same element as 2 then inc count2
            elif num == candidate2:
                count2 += 1
            # if num is different than both can1 & can2 then allot it a new slot as count1 is empty
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            # if num is different than both can1 & can2 then allot it a new slot as count2 is empty & count1 is occupied
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            # if both the counts slots are not empty then decrement counts of both
            else:
                count1 -= 1
                count2 -= 1

        # verify counts if we get the majority or not using both can1 and can2
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        # simply check if both the counts 1 and 2 passes the threshold
        res = []

        if count1 > threshold:
            res.append(candidate1)

        if count2 > threshold:
            res.append(candidate2)

        return res


# TS1
nums = [3,2,3]
output= [3]

# TS2
# nums = [1, 2]
# output = [1, 2]
print(Solution().majorityElement(nums))
