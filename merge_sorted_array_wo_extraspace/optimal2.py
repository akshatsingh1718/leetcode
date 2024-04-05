from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """

        TC: O(min(m, n)) + O(n log n) + O(n log n)
        SC: O(1)

        Algo: Gap method from Shell sort
        """

        def swap_if_gtr(a1, idx1, a2, idx2):
            if a1[idx1] > a2[idx2]:
                a1[idx1], a2[idx2] = a2[idx2], a1[idx1]

        gap = m + n
        gap = (gap // 2) + (gap % 2)

        while gap > 0:

            ptr1 = 0
            ptr2 = ptr1 + gap
            while ptr2 < n + m:

                if (
                    ptr1 < m and ptr2 >= m
                ):  # ptr1 is on the left array and ptr2 is on the right array
                    swap_if_gtr(nums1, ptr1, nums2, ptr2 - m)
                elif ptr1 >= m:
                    swap_if_gtr(nums2, ptr1 - m, nums2, ptr2 - m)
                else:
                    swap_if_gtr(nums1, ptr1, nums1, ptr2)

                ptr1 += 1
                ptr2 += 1

            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)

        return nums1, nums2


# low = 2; high = 2
# mid = 2 + (2-2) // 2 = 2
# if 3 > 2 -> high = 2 - 1 = 1
# low = 2; high = 1
# return (low= 2)

## Que1
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# output = [1, 2, 2, 3, 5, 6]

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
