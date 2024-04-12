from typing import List


class Solution:
    '''
    TC: O(n)
    SC: O(1)

    Alog: (Two Pointer Approach)
    '''
    def trap(self, height: List[int]) -> int:
        
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        result = 0

        while left <= right:
            # if value of left height is less than right's height then it means 
            # right could carry water of left index
            if height[left] <= height[right]:

                # if the current left is a new left max meaning it can be only use as a barrier
                # to store water ahead and not above it since its the tallest yet
                if height[left] >= left_max:
                    left_max = height[left]
                # The current left is less than the left_max meaning we have a taller height stage on left
                # so the water store will be the tallest height of the platform minus (-) the current height
                # of the platform 
                else:
                    result += (left_max - height[left])

                left += 1
            
            # if the right height if smaller than the left height and now
            # its left's turn to be used a left barrier to store the water 
            # in b/w current right and left  
            else: 

                # if the current right is the tallest from all the heights in its right
                # then this will act as a barrier to store the water on left since
                # the water above it cannot be stored a no height in right is taller to store the water 
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # store water !
                    result += (right_max - height[right])

                right -= 1

        return result
        


height = [0,1,0,2,1,0,1,3,2,1,2,1]
output= 6
print(Solution().trap(height))