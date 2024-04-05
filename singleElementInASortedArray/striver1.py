from typing import List

class Solution:
    ''''
    -> Using XOR Operator: n^n = 0 and n^m=1


    Runtime
    Details
    158ms
    Beats 50.74%of users with Python3
    Memory
    Details
    25.86MB
    Beats 93.87%of users with Python3
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = nums[0]
        for i in nums[1:]:
            print(f"{x}^{i} = {x^i}")
            x ^= i

        return x



def main():

    s = Solution()

    nums = [1,1,2,3,3,4,4,8,8]
    output=  2

    res = s.singleNonDuplicate(nums)

    if res != output:
        print("Error")

    else:
        print("Success")


if __name__ == "__main__":
    main()