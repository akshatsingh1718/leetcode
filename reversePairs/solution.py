from typing import List

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


class Solution:

    def merge(cls, arr: List[int], low: int, mid: int, high: int) -> int:
        i = low
        j = mid
        res = []
        while i < mid and j <= high:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1

        while i < mid:
            res.append(arr[i])
            i += 1

        while j <= high:
            res.append(arr[j])
            j += 1

        for i in range(low, high + 1):
            arr[i] = res[i - low]  # low is offset

    def count_pairs(cls, arr: List[int], low: int, mid: int, high: int) -> int:

        i = low
        j = mid
        count = 0
        for i in range(low, mid):
            while j <= high and arr[i] > arr[j] * 2:
                j += 1
            count += j - mid
        return count
    
    def merge_sort(cls, arr: List[int], low: int, high: int) -> int:
        count = 0
        if low < high:

            mid = (high + low) // 2

            # This means add the count for left array (this will also eventually call count_pairs fn)
            count += cls.merge_sort(arr, low, mid)
            # add the count for right array 
            count += cls.merge_sort(arr, mid + 1, high)
            # count the pairs of the current merged array of left + right
            count += cls.count_pairs(arr, low, mid + 1, high)
            cls.merge(arr, low, mid + 1, high)

        return count

    def reversePairs(cls, nums: List[int]) -> int:
        n = len(nums)
        return cls.merge_sort(nums, 0, n - 1)


# TS1
# arr = [1, 3, 2, 3, 1]
# output = 2

# TS2
arr= [2,4,3,5,1]
output = 3

# TS3
# arr = [1, 2, 3, 4, 5]
# output = 0

n = len(arr)
print(Solution().reversePairs(arr))
