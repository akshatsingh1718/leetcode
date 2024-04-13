from typing import List


class Solution:
    '''
    TC: O(n) [for loop] + O(n) [pop till monotonous is preserved] ~ O(2n)
    SC: O(n) [stack]
    
    '''

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # to pop all the elements when the heights is sorted array
        stack = [] # monotonous stack
        max_rect = 0

        # Iterate over all the elements
        for i, ele in enumerate(heights):

            # check if the current element is less than the top of the stack
            # if yes it means we are breaking the monotonous increaing nature of the
            # stack and got a lower value than the top of the stack and should remove the top
            # elements of the stack since they can no longer make a rectangle furthur this point
            while len(stack) > 0 and heights[stack[-1]] > ele:
                # pop the top index
                top_idx = stack.pop()
                # get the value of corresponding height
                top_val = heights[top_idx]

                # if the stack is empty meaning all the elements are popped because of the stoppage
                # by the current element by having a small value from all the left elements of it meaning
                # it can make rect till the first element which is 0 idx
                # AND
                # if the stack is not empty then the top element + 1 will be starting index since the
                # top element is the one which is smaller than the top_idx element

                left_small = (stack[-1] + 1) if len(stack) > 0 else 0

                # right small will be i as i is the place where the monotonous nature breaks
                right_small = i

                # find the max b/w max_react and the volumne of the top_val
                max_rect = max(max_rect, (right_small - left_small) * top_val)

            # if the monotonous nature is preserved then simply add it to the stack
            stack.append(i)

        return max_rect


# TS1
# heights = [2, 1, 5, 6, 2, 3]
# output = 10

# TS2
# heights = [3, 2, 10, 11, 5, 10, 6, 3]
# output = 25

# TS3
heights = [1]
output = 1

# TS4
heights = [1, 1]
output = 2

# TS5
heights = [2, 0, 2, 1, 1]
output = 3

print(Solution().largestRectangleArea(heights))
