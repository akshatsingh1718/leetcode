from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums3 = []
        left = 0
        right = 0

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                nums3.append(nums1[left])
                left += 1
            else:
                nums3.append(nums2[right])
                right += 1

        while left < m:
            nums3.append(nums1[left])
            left += 1

        while right < n:
            nums3.append(nums2[right])
            right += 1

        return nums3


# low = 2; high = 2
# mid = 2 + (2-2) // 2 = 2
# if 3 > 2 -> high = 2 - 1 = 1
# low = 2; high = 1
# return (low= 2)

## Que1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
output= [1,2,2,3,5,6]

## Que2
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

## Que3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

res = Solution().merge(nums1, m, nums2, n)

print(res)
