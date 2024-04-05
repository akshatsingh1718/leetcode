from typing import *


class Solution:
    '''
    
    Runtime
    Details
    77ms
    Beats 80.81%of users with Python3
    Memory
    Details
    16.71MB
    Beats 89.32%of users with Python3
    '''
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Time complexity: O(n) 
            As we are iterating over whole array only once

        Space Complexity: O(1) [max_prod] + O(1) [curr_max] + O(1) [curr_min] ~ O(1)
            Since we are using constant space

        Q. Why are we storing min with max as well ?
        A. If the current element is a negative value and our min (which is the min element till the nth element 
            we are currently on) is a very large negative value then our current prod will be a very larget positive
            value as negative * negative = positive.
        '''
        n = len(nums)

        # initially max_prod, curr_max and curr_min will store the first element of the list
        max_prod = nums[0]

        curr_max, curr_min = nums[0], nums[0]

        # start from the second item in the list
        for n in nums[1:]:

            # create a group of current_element, current_element * curr_max, current_element * curr_min
            vals = (n, n * curr_max, n * curr_min)

            # curr_max : the current max of sub array till the nth item 
            curr_max = max(vals)

            # curr_min : the current min of sub array till the nth item 
            curr_min = min(vals)

            # max_prod: the max prod we get while iterating
            max_prod = max(max_prod, curr_max)

        return max_prod


def main():
    s = Solution()

    # nums = [2,3,-2,4]
    # output= 6

    # nums = [-2, 0, -1]
    # output = 0

    nums = [-4, -3]
    output = 12

    res = s.maxProduct(nums)

    print(res)

    # assert output == res, "Not Matching"


main()
