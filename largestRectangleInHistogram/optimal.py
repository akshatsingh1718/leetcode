from typing import List

# Improved version of solution.py


class Solution:
    """
    TC: O(n) [find left small] + O(n) [find right small] + O(n) [find max] = O(3n)
    SC: O(n) [left_small] +  O(n) [right_small] = O(2n)

    Algo:


    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # find left smalls
        left_small = [0 for _ in range(n)]
        stack = []

        # if ele is gt than top stack[-1] then simply append it to stack
        # else pop all the elements till ele is sm stack elements to get the react shape as left as possible since
        #   we want to strech the current element height as left to as possible
        for i, ele in enumerate(heights):

            while len(stack) > 0 and ele <= heights[stack[-1]]:
                stack.pop()  # remove until ele is gt stack.top()

            if len(stack) == 0:
                left_small[i] = (0)
            else:
                left_small[i] = (stack[-1] + 1)

            stack.append(i)

        # find left smalls
        right_small = [0 for _ in range(n)]
        stack = [] # empty stack

        for i in range(n - 1, -1, -1):
            ele = heights[i]

            while len(stack) > 0 and ele <= heights[stack[-1]]:
                stack.pop()  # remove until right small is not found to current ele

            if len(stack) == 0:
                right_small[i]= (n - 1)
            else:
                right_small[i]= (stack[-1] - 1)

            stack.append(i)

        # find the max
        max_rect = 0
        for i, ele in enumerate(heights):
            max_rect = max(max_rect, (right_small[i] - left_small[i] + 1) * ele)
        return max_rect

class Solution2:
    """
    TC: O(n) [find left small] + O(n) [find right small + find max] = O(2n)
    SC: O(n) [left_small] +  O(n) [right_small] + O(n) [stack] = O(3n)

    Algo:

    While computing right small we can find the max_rect at i'th position
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # find left smalls
        left_small = [0 for _ in range(n)]
        stack = []

        # if ele is gt than top stack[-1] then simply append it to stack
        # else pop all the elements till ele is sm stack elements to get the react shape as left as possible since
        #   we want to strech the current element height as left to as possible
        for i, ele in enumerate(heights):

            while len(stack) > 0 and ele <= heights[stack[-1]]:
                stack.pop()  # remove until ele is gt stack.top()

            if len(stack) == 0:
                left_small[i] = (0) # cause stack is empty
            else:
                left_small[i] = (stack[-1] + 1)


            stack.append(i)

        # find left smalls
        right_small = [0 for _ in range(n)]
        stack = [] # empty stack

        # find the max
        max_rect = 0

        for i in range(n - 1, -1, -1):
            ele = heights[i]

            while len(stack) > 0 and ele <= heights[stack[-1]]:
                stack.pop()  # remove until right small is not found to current ele

            if len(stack) == 0:
                right_small[i]= (n - 1)
            else:
                right_small[i]= (stack[-1] - 1)

            stack.append(i)

            max_rect = max(max_rect, (right_small[i] - left_small[i] + 1) * ele)
        
        return max_rect

# TS1
# heights = [2, 1, 5, 6, 2, 3]
# output = 10

# TS2
heights = [3, 2, 10, 11, 5, 10, 6, 3]
output = 25

print(Solution2().largestRectangleArea(heights))
