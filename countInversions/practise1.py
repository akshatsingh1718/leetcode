from typing import List

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


class Solution:
    """
    TC: O(n logn)
    SC: O(n)
    """

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> int:
        # merge the array and count the unsorted nums offset

        # arr1: [low -> mid - 1]
        # arr2: [mid -> high]

        res = []
        i = low
        j = mid
        count = 0
        while i < mid and j <= high:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:  # arr[i] > arr[j]
                count += mid - i
                res.append(arr[j])
                j += 1

        # add the rest of the items
        while i < mid:
            res.append(arr[i])
            i += 1

        while j <= high:
            res.append(arr[j])
            j += 1

        # copy the res into original arr
        for i in range(low, high + 1):
            arr[i] = res[i - low]

        return count

    def merge_sort(self, arr: List[int], low: int, high: int) -> int:

        count = 0

        if low < high:
            mid = (low + high) // 2

            count = self.merge_sort(arr, low, mid)
            count += self.merge_sort(arr, mid + 1, high)
            count += self.merge(arr, low, mid + 1, high)
        return count

    def inversionCount(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)


# TS1
# arr = [3, 2, 1]
# output = 3

# TS2
# arr=[2, 5, 1, 3, 4]
# output = 4

# TS2
arr = [5, 3, 2, 4, 1]
output = 8

n = len(arr)
print(Solution().inversionCount(arr))
