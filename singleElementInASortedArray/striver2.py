from typing import List


class Solution:
    '''
    Runtime
    Details
    144ms
    Beats 96.60%of users with Python3
    Memory
    Details
    25.95MB
    Beats 69.80%of users with Python3
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid ^ 1] == nums[mid]:
                low = mid + 1
            else:
                high = mid

        return nums[low]


def main():
    s = Solution()

    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    output = 2

    res = s.singleNonDuplicate(nums)

    if res != output:
        print("Error")

    else:
        print("Success")


if __name__ == "__main__":
    main()
