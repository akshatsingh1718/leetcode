from typing import List


class Solution:
    '''
    This is not working
    - Here i was storing an array to hold the original indexes of the array
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge(arr, low, mid, high, count: List[int], index: List[int]):
            i = low
            j = mid
            temp = []
            temp_ctr= 0
            index_temp = []

            while i < mid and j <= high:

                if arr[i] > arr[j]:
                    for temp_i in range(i, mid):
                        count[index[temp_i]] += 1

                    # temp_ci = index[i]
                    # index[i] = j
                    # index[j] = temp_ci
                    index[low + temp_ctr] = j

                    temp.append(arr[j])
                    j += 1
                else:
                    index[low + temp_ctr] = i
                    temp.append(arr[i])
                    i += 1

                temp_ctr += 1

            
            while i < mid:
                index[low + temp_ctr] = i
                temp_ctr += 1

                temp.append(arr[i])
                i += 1

            while j <= high:
                index[low + temp_ctr] = j
                temp_ctr += 1

                temp.append(arr[j])
                j += 1

            # print("index", index)
            # replace the numbers on original array
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def merge_sort(arr, low, high, count: List[int], index: List[int]):
            if low < high:
                mid = (low + high) // 2

                merge_sort(arr, low, mid, count, index)
                merge_sort(arr, mid + 1, high, count, index)
                # NOTE: Its imp to use (mid+1) below because one array if from (low -> mid) and (mid+1 -> high)
                merge(arr, low, mid + 1, high, count, index)

        n = len(nums)
        count = [0 for _ in range(n)]
        index = [i for i in range(n)]

        merge_sort(nums, 0, n - 1, count, index)
        return count


# nums = [5, 2, 6, 1]
# output = [2, 1, 1, 0]

# nums = [2, 0, 1]
# output = [2, 0, 0]

# nums = [0,2,1]
# output= [0,1,0]

nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
output= [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]


res = Solution().countSmaller(nums)
print(res)

print(res == output)