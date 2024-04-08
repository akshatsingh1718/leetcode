"""
Interview Bit: https://www.interviewbit.com/problems/repeat-and-missing-number-array/
"""

class Solution:
    '''
    TC: O(n) [for filling freq arr] + O(n) [for finding missing]
    SC: O(n) [for freq array]
    '''
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        freq = [0 for _ in range(len(A))]
        duplicate = None
        missing = None
        
        for _, ele in enumerate(A):
            count = freq[ele - 1]
            if count == 0:
                freq[ele - 1] += 1
            else:
                duplicate = ele
                
        for idx, ele in enumerate(freq):
            if ele == 0:
                missing = idx + 1
                
        return (duplicate, missing)
                
