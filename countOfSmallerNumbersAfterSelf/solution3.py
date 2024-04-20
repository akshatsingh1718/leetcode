from typing import List


class Solution:
    '''
    TC: O(n log n)
    SC: O(n)

    
    Algo: (Mostly same as reverse pairs) (Merge Sort)
    1. Create a count to store the counts of each indexes.
    2. Create a index to store the value and initial index location of the value since sorting may change the location of each element.
    3. Start the merge sort and sorting will be in decreasing manner.
    4. When merging the left and right array check if index[i] > index[j] then increment the count for i the element to the len(arr[j -> high]) since from j'th index we have all the element only decreasing so our count will include all those elements and then simply increment the i to check for next element from left array.

    '''
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge(low, mid, high, count: List[int], index: List[int]):
            i = low
            j = mid
            temp = []

            while i < mid and j <= high:
                if index[i][0] <= index[j][0]:
                    # if element at i is gt element at j
                    temp.append(index[j])  # add small element
                    j += 1  # lets check for next j if its smaller or not ?
                else:
                    count[index[i][1]] += (high - j + 1)
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

        def merge_sort(low, high, count: List[int], index: List[int]):
            if low < high:
                mid = (low + high) // 2

                merge_sort(low, mid, count, index)
                merge_sort(mid + 1, high, count, index)

                # NOTE: Its imp to use (mid+1) below because one array if from (low -> mid) and (mid+1 -> high)
                merge(low, mid + 1, high, count, index)

        n = len(nums)
        count = [0 for _ in range(n)]
        # index = [[ele, i, i] for i, ele in enumerate(nums)]
        index = [[ele, i] for i, ele in enumerate(nums)]

        merge_sort(0, n - 1, count, index)

        return count


nums = [5, 2, 6, 1]
output = [2, 1, 1, 0]

# nums = [2, 0, 1]
# output = [2, 0, 0]

# nums = [0,2,1]
# output= [0,1,0]

nums = [
    26,
    78,
    27,
    100,
    33,
    67,
    90,
    23,
    66,
    5,
    38,
    7,
    35,
    23,
    52,
    22,
    83,
    51,
    98,
    69,
    81,
    32,
    78,
    28,
    94,
    13,
    2,
    97,
    3,
    76,
    99,
    51,
    9,
    21,
    84,
    66,
    65,
    36,
    100,
    41,
]
output = [
    10,
    27,
    10,
    35,
    12,
    22,
    28,
    8,
    19,
    2,
    12,
    2,
    9,
    6,
    12,
    5,
    17,
    9,
    19,
    12,
    14,
    6,
    12,
    5,
    12,
    3,
    0,
    10,
    0,
    7,
    8,
    4,
    0,
    0,
    4,
    3,
    2,
    0,
    1,
    0,
]


res = Solution().countSmaller(nums)
print(res == output)
