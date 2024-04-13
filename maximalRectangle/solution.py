from typing import List


class Solution:
    '''
    TC: O(m * 2n) [m * find_max_hist_rect] + O(m*n) [2 for loops] = (m*2n) + (m*n) = m(2n + n ) = O(m * 3n)
    SC: O(n) [stack] + O(n) [arr] ~ O(2n)
    '''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        def find_max_hist_rect(arr: List[int]):  # refer: largestRectangleInHistogram
            arr.append(-1)
            stack = []
            max_rect = 0

            for i, ele in enumerate(arr):

                while (
                    len(stack) > 0 and arr[stack[-1]] > ele
                ):  # monotonous nature breaks !
                    top_idx = stack.pop()
                    top_val = arr[top_idx]

                    left_small = (stack[-1] + 1) if len(stack) > 0 else 0
                    right_small = i

                    max_rect = max(max_rect, (right_small - left_small) * top_val)

                stack.append(i)

            return max_rect

        arr = [0 for _ in range(n)]
        max_rect = 0
        for i in range(m):

            # create hist for each level
            for j in range(n):
                if matrix[i][j] == "0":
                    arr[j] = 0 # Zero act as a break for horizontal ones
                else:
                    arr[j] += int(matrix[i][j])

            max_rect = max(max_rect, find_max_hist_rect(arr))

        return max_rect


matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]
output= 6
print(Solution().maximalRectangle(matrix))