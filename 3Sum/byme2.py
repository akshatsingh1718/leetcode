from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ """

        n = len(nums)
        arr = []

        bucket = {}  # key = -(arr[i] + arr[j]) : val = (i, j)

        for i in range(n - 2):
            for j in range(i + 1, n):
                idxs = bucket.get(nums[j])

                if idxs is None:
                    bucket[-nums[i] - nums[j]] = (i, j)
                else:
                    if j in idxs:
                        continue
                    _i, _j = idxs

                    triplet = sorted([nums[_i], nums[_j], nums[j]])

                    if triplet not in arr:
                        if triplet == [-2, 1, 1]:
                            print(f"{i=} | {j=} | {_i=} | {_j=}")
                            print(f"")

                        arr.append(triplet)
        return arr


def main():
    # nums = [-1, 0, 1, 2, -1, -4]
    # output = [[-1, -1, 2], [-1, 0, 1]]

    # nums = [1,2,-2,-1]
    # output= []

    nums = [3, 0, -2, -1, 1, 2]
    output = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]

    s = Solution()

    res = s.threeSum(nums)

    print(res)


if __name__ == "__main__":
    main()
