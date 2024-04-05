from typing import List


class Solution:
    """
    Runtime
    Details
    1373ms
    Beats 14.86%of users with Python3
    Memory
    Details
    16.28MB
    Beats 87.03%of users with Python3

    TC : O(n^3) + O( log1 ) [if we are using ordered set else O(1) if using unordered set]

    SC : O(n) [for storing items in set] + O(no of quads)
    SC2 : When arr is set and not list then : O(no of quads)x2 [for storing quads in set unique and return as a list]
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        arr = []

        for i in range(n - 3):
            for j in range(i + 1, n):
                hashset = set()

                for k in range(j + 1, n):
                    numsL = target - (nums[i] + nums[j] + nums[k])
                    if numsL in hashset:
                        quads = sorted([nums[i], nums[j], nums[k], numsL])

                        if quads not in arr:
                            arr.append(quads)

                    hashset.add(nums[k])

        return arr


def arrCompare(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for a2 in arr2:
        if a2 not in arr1:
            return False
    return True


def main():
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    # output = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # nums = [2, 2, 2, 2, 2]
    # target = 8
    # output = [[2, 2, 2, 2]]

    # nums = [0, 0, 0, 0]
    # target = 0
    # output = [[0, 0, 0, 0]]

    # nums = [-3, -1, 0, 2, 4, 5]
    # target = 0
    # output = [[-3, -1, 0, 4]]

    s = Solution()

    res = s.fourSum(nums, target)

    print(f"{res =}")

    assert arrCompare(res, output), "Not Matching"

    print("Passed !")


if __name__ == "__main__":
    main()
