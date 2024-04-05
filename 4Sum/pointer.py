from typing import List


class Solution:
    """
    Runtime
    Details
    732ms
    Beats 50.73%of users with Python3
    Memory
    Details
    16.43MB
    Beats 33.92%of users with Python3

    TC : O(n^2) [2 for loops] x O(n) [while loop of k - l] ~ O(n^3)
    SC : O(no of quads)
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        arr = []

        # sort the array to asc order
        nums.sort()

        for i in range(n):
            # if i is 0 then increment till its not same as prv element
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # if j is not the element right after i then increment till its not same as prv element
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                    # above i was doing j += 1 but dont do that let
                    # for loop increment the j, index error will be raised

                # set the k and j to their initial values
                k = j + 1
                l = n - 1
                # check k should not pass j's value
                while k < l:
                    quads_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    # print(f"{i=} | {j=} | {k=} | {l=} | {quads_sum=}")

                    # check if found target or not
                    if quads_sum == target:
                        arr.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # move to the element where they are not equal to their last value
                        while k < j and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif quads_sum < target:
                        k += 1

                    else:  # quads_sum > target
                        l -= 1

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
