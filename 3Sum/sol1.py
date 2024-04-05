from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Limit Exceeded

        - Some compilter will not give TLE  
        """

        n = len(nums)
        arr = []  # store all triplets

        for i in range(n):
            bucket = set()  # key = -(arr[i] + arr[j]) : val = (i, j)
            for j in range(i + 1, n):

                # find the third element we needed
                arrK = -(nums[i] + nums[j])

                # check if third element we needed is in or bucket or not
                if arrK in bucket:

                    # create triplet with the 3rd element
                    triplet = sorted([nums[i], nums[j], arrK])
                    
                    # check if triplet already in our unique arr or not
                    if triplet not in arr:
                        arr.append(triplet)
                else:
                    # if 3rd element not present in bucket then add into the bucket 
                    bucket.add(nums[j])
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
