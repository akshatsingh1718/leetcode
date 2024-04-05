from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        
        TC: O(n) + O(n) ~ O(2n)
        SC: O(1)

        Algo: Using insertion sort
        """

        for i in range(0, n):
            j = m + i 
            key = nums2[i]

            nums1[j] = key

            # reduce the j index to check for left elements
            j -= 1
            
            while key <= nums1[j] and j >= 0:
                # shift the jth number to right as it is bigger than our key
                nums1[j + 1] = nums1[j]
                j -= 1

            j += 1
            nums1[j] = key

        return nums1


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
nums1 = [0]
m = 0
nums2 = [1]
n = 1

res = Solution().merge(nums1, m, nums2, n)

print(res)