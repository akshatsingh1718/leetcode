from typing import List


class Solution:
    """
    Time Limit Exceeded
    249 / 293 testcases passed
    Last Executed Input
    Use Testcase
    nums =
    [-472,-466,-463,-445,-443,-429,-428,-427,-383,-372,-345,-344,-318,-314,-302,-299,-285,-283,-267,-236,-235,-232,-230,-225,-207,-205,-185,-184,-155,-151,-144,-128,-127,-124,-110,-110,-101,-95,-93,-63,-43,-25,-25,2,4,19,20,28,31,31,40,75,79,92,113,114,119,157,157,161,161,181,191,198,209,215,228,229,235,237,243,254,254,260,274,274,292,303,304,316,320,324,336,368,378,383,389,402,406,446,462,496]
    target =
    2044

    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Brute force approach
        """
        n = len(nums)
        arr = []

        for i in range(n - 3):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        print(f"{l =}")
                        summ = nums[i] + nums[j]
                        summ += nums[k] + nums[l]
                        temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                        print(temp)
                        if summ == target and temp not in arr:
                            arr.append(sorted([nums[i], nums[j], nums[k], nums[l]]))

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


    nums = [0,0,0,0]
    target = 0
    output = [[0,0,0,0]]


    s = Solution()

    res = s.fourSum(nums, target)

    print(f"{res =}")

    assert arrCompare(res, output), "Not Matching"

    print("Passed !")


if __name__ == "__main__":
    main()
