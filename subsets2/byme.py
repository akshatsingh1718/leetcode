from typing import List


class Solution:
    """
    Runtime
    Details
    38ms
    Beats 86.12%of users with Python3
    Memory
    Details
    16.51MB
    Beats 50.42%of users with Python3
    """

    def findSubsets(
        self, index: int, nums: List[int], arr: List[int], result: List[List[int]]
    ):
        n = len(nums)
        if n == index:
            return None

        visited = []
        for i in range(index, n):
            if nums[i] not in visited:
                visited.append(nums[i])
                result.append(arr + [nums[i]])
                self.findSubsets(i + 1, nums, result[-1], result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        arr = []
        nums.sort()

        self.findSubsets(0, nums, arr, result)

        return result + [[]]


def main():
    s = Solution()

    nums = [1, 2, 2]
    outputs = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    res = s.subsetsWithDup(nums) 

    print(res)


if __name__ == "__main__":
    main()
