from typing import List

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


class Solution():
    def merge(cls, arr: List[int], low: int, mid: int, high: int) -> int:
        """
        Algo:

        1. start a while loop over section of arr[low : mid] (left section) and arr[mid:high] (right section).
        2. The left and right sections are alredy sorted and we want to merge both the sections into a new array which will be sorted as well.
        4. We want to check the elements which are in left section and are greater than right section elements.
        5. If the element at i'th position in left is greater than any j'th element in the right then it's evident that all the elements from arr[i: len(left)] will be gt than the j'th element as the array is sorted and starting from i'th elements all the elements further will be gt as well. So increase the counter by no of elements from i'th pos till end and we saved our iterations as well for the rest of the elements for j'th element.
        """
        i = low
        j = mid
        res = []
        count = 0
        while i < mid and j <= high:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                count += mid - i
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

        return count

    def merge_sort(cls, arr: List[int], low: int, high: int):
        count = 0

        if low < high:

            mid = (high + low) // 2

            count = cls.merge_sort(arr, low, mid)
            count += cls.merge_sort(arr, mid + 1, high)
            count += cls.merge(arr, low, mid + 1, high)

        return count

    def getInversions(cls, arr, n) -> int:
        return cls.merge_sort(arr, 0, n - 1)


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
print(Solution().getInversions(arr, n))
