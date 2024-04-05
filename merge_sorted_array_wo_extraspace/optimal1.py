from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        
        TC: O(min(m, n)) + O(n log n) + O(n log n)
        SC: O(1)

        Algo: 2 pointer approach + basic sorting
        """

        # create 2 poitners for left and right array
        left = m - 1
        right = 0

        # copy the large elements to left array and small elements to right array
        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break

        # sort the arrays individually
        nums1.sort()
        nums2.sort()

        return nums1, nums2




# low = 2; high = 2
# mid = 2 + (2-2) // 2 = 2
# if 3 > 2 -> high = 2 - 1 = 1
# low = 2; high = 1
# return (low= 2)

## Que1
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# output= [1,2,2,3,5,6]

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


## Que4
nums1 = [1, 8, 8]
m = 3
nums2 = [2, 3, 4, 5]
n = 4
output= [1, 2, 3, 4, 5, 8, 8]

res = Solution().merge(nums1, m, nums2, n)

print(res)