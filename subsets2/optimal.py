from typing import List


class Solution:
    """
    Runtime
    Details
    44ms
    Beats 55.87%of users with Python3
    Memory
    Details
    16.24MB
    Beats 99.65%of users with Python3

    TC : O(2^n) [recursion stack] x O(n) [assuming avg length of subsets is n/ copying the subset to ans ds] 
    SC : O(2^n) [to store all the subsets] x O(k) [ since adding a DS takes o(k) and not constant time]
    Aux SC: O(n) [max recursion stack]
    """

    def findSubsets(
        self, index: int, nums: List[int], arr: List[int], result: List[List[int]]
    ):
        n = len(nums)
        result.append(arr)

        # if n == index:
        #     return None
        # visited = []
        # for i in range(index, n):
        #     if nums[i] not in visited:
        #         visited.append(nums[i])
        #         result.append(arr + [nums[i]])
        #         self.findSubsets(i + 1, nums, result[-1], result)
        ## To simplify the above code without using visited array

        # array is already sorted then we can check the arr[i] != arr[i-1]
        # no need to handle base case as index will not go out of bounds

        for i in range(index, n):
            # if i is not the starting position
            if i != index and nums[i] == nums[i - 1]:
                continue

            # This be done at an average of O(n) assuming all nums are unique
            arr.append(nums[i]) # add new different number # takes o(n) to add a ds into a ds
            self.findSubsets(i + 1, nums, arr[:], result)
            arr.pop()

            # print(f"{i} Send => {arr} -> {arr + [nums[i]]}")
            
            # or more concise
            # self.findSubsets(i + 1, nums, arr + [nums[i]], result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        self.findSubsets(0, nums, arr=[], result=result)

        return result


def main():
    s = Solution()

    nums = [1, 2, 2]
    outputs = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    res = s.subsetsWithDup(nums)

    print(res)


if __name__ == "__main__":
    main()
