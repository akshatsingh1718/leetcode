from typing import List


class Solution:
    '''
    TC: O(log n) [divide to subarray] + O(n) [for merge sorting] + O(n) [for count_smaller] ~ O(2n logn)
    SC: O(n) [for value, index storing in index var]
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge(low, mid, high, index: List[int]):
            i = low
            j = mid
            temp = []

            while i < mid and j <= high:
                if index[i][0] > index[j][0]:
                    # if element at i is gt element at j
                    temp.append(index[j])  # add small element
                    j += 1
                else:
                    temp.append(index[i])  # add small element
                    i += 1

            while i < mid:
                temp.append(index[i])
                i += 1

            while j <= high:
                temp.append(index[j])
                j += 1

            # replace the numbers on original array
            for i in range(low, high + 1):
                index[i] = temp[i - low]

        def count_smaller(low, mid, high, index, count):
            i = low
            j = mid
            for i in range(low, mid):

                while j <= high and index[i][0] > index[j][0]:
                    j += 1
                count[index[i][1]] += j - mid

        def merge_sort(low, high, count: List[int], index: List[int]):
            if low < high:
                mid = (low + high) // 2

                merge_sort(low, mid, count, index)
                merge_sort(mid + 1, high, count, index)

                # count inversions
                count_smaller(low, mid + 1, high, index, count)

                # NOTE: Its imp to use (mid+1) below because one array if from (low -> mid) and (mid+1 -> high)
                merge(low, mid + 1, high, index)


        n = len(nums)
        count = [0 for _ in range(n)]
        # (val, static idx, dynamic index for sort)
        index = [[ele, i] for i, ele in enumerate(nums)]

        merge_sort(0, n - 1, count, index)

        return count

nums = [5, 2, 6, 1]
output = [2, 1, 1, 0]

# nums = [2, 0, 1]
# output = [2, 0, 0]

# nums = [0,2,1]
# output= [0,1,0]

# nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
# output= [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]


res = Solution().countSmaller(nums)
print(res == output)
