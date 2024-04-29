from typing import List


class Solution:
    '''
    TC: O(n + 32) [for loop + for loop over 32 bits] ~ O(n)
    SC: O(1)

    Algo:

    1. find the xor of the array.
    2. since the constraints tell us that nums range will be <= 10**6 so we can say that we will be dealing
        in the range of ints of 32 bits at most.
    3. Iterate over all the 32 bits of the the k and xor.
    4. Left shifiting the 1 from 0 to 32 will give the bit=1 at each of the positon of 32 bit and leaving 0
        for rest of the positions.
        Eg. Take example of 4 bit
            1 = 0001
            1 << 0 = 0001 # 0th bit
            1 << 1 = 0010 # 1st bit
            1 << 2 = 0100 # 2nd bit
            1 << 3 = 1000 # 4th bit

    5. Now we will AND "&" these with the k and xor. But Why ? We need to check which bits of k and xor are
        not matching and that will cost an operation. But how do we check for the specific bit since we cant slice the bit easily like string. eg bit[0] is not a valid operation so we will use & operation with left shifted of integer 1. At step 4 we say we are getting 1 at each position of bit and rest are zeros. So &'ing with those shifted values will give the same bit at the postion of 1 and 0 elsewhere since 0 & <Any Number = 0 and 1 & <Any num> = <Any num> and this way we will grab the ith bit of xor and k and check if they match or not.



    '''
    def minOperations(self, nums: List[int], k: int) -> int:

        # get the xor of array
        xor = 0
        for num in nums:
            xor ^= num

        # find out if each bit of k is matching with the xor
        # we know the constraints of nums are <= 10**6 which means
        # less than 32 bit integer limit

        operations_needed = 0
        for i in range(0, 32):  # iterate from 0 -> 31
            if (k & (1 << i)) != (xor & (1 << i)):
                operations_needed += 1

        return operations_needed


nums = [2, 1, 3, 4]
k = 1
output = 2

print(Solution().minOperations(nums, k))
