from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Limit Exceeded

        - Some compilter will not give TLE
        """

        n = len(nums)
        arr = []  # store all triplets

        # sort array
        nums.sort()

        for i in range(n):
            # i should not be iterated previously
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                # if sum is lt 0 then increase the j pointer to inc the sum
                if sums < 0:
                    j += 1
                # if sum is gt 0 then decrease the k pointer to dec the sum
                elif sums > 0:
                    k -= 1
                # the sum is zero and append the triplet
                # no need to check if the triplet already exist in the arr
                # as every element i, j and k is unique at every stage
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    # add triplet to the array nd no need to sort as already sorted
                    arr.append(triplet)
                    # j and k cannot be same so change them
                    j += 1
                    k -= 1

                    # increase i and j till they are not equal to their last element
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return arr


def main():
    # nums = [-1, 0, 1, 2, -1, -4]
    # output = [[-1, -1, 2], [-1, 0, 1]]

    # nums = [1,2,-2,-1]
    # output= []

    # nums = [3, 0, -2, -1, 1, 2]
    # output = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]

    nums = [0, 0, 0]
    output = [[0, 0, 0]]

    s = Solution()

    res = s.threeSum(nums)

    print(res)


if __name__ == "__main__":
    main()
