from typing import List


class Solution:
    """
    TC: O(n) [find precomputed min, max values] + (n) [check for water stored] ~ O(n)
    SC: O(n)

    Algo: 

    1. Iterate over all the elements of the list
    2. check current element's max right and max left.
    3. If the current element is greater than either right or left max then its water cannot be stored.
    4. If both the max left and right is higher than current element than it means water can be stored for
        current element.  
    """

    def trap(self, height: List[int]) -> int:

        def find_max_on(i):
            nonlocal height

            left_max = max(height[:i]) if i > 0 else 0
            right_max = max(height[i + 1 :]) if i < (len(height) - 1) else 0
            return left_max, right_max

        # store the precomputed values
        min_max_arr = [find_max_on(i) for i in range(len(height)) ]

        result = 0
        for i, ele in enumerate(height):

            left_max, right_max = min_max_arr[i]

            if ele > left_max or ele > right_max:
                continue

            deciding_height = min(left_max, right_max)
            result += (deciding_height - ele)

        return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = 6
print(Solution().trap(height))
