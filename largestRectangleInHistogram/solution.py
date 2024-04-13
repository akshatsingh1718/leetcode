from typing import List


class Solution:
    """
    TC: O(n^2) [find left and right min for each n elements]
    SC: O(1)

    Algo:
    1. Find the left and right min boundary of the current element.
    2. Find the max via the formula for largest react with current element's height.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        def find_left_min_indx(idx: int):
            nonlocal heights

            left_small = 0

            for i in range(idx - 1, -1, -1):
                if heights[i] < heights[idx]:
                    left_small = i + 1
                    break

            return left_small

        def find_right_min_indx(idx: int):
            nonlocal heights

            right_small = len(heights) - 1

            for i in range(idx + 1, len(heights)):
                if heights[i] < heights[idx]:
                    right_small = i - 1
                    break

            return right_small

        curr_max = 0
        for i, ele in enumerate(heights):
            curr_max = max(
                curr_max, (find_right_min_indx(i) - find_left_min_indx(i) + 1) * ele
            )
        return curr_max

        # return max([ (find_right_min_indx(i) - find_left_min_indx(i) + 1) * ele  for i, ele in enumerate(heights)])


heights = [2, 1, 5, 6, 2, 3]
output = 10
print(Solution().largestRectangleArea(heights))
