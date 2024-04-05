from typing import List

class Solution:

    def reverseInplace(self, nums: List[int]):
        n = len(nums)
        if n == 2:
            nums[0], nums[1] = nums[1], nums[0]
        else:
            mid = n//2
            for i in range(0, mid):
                nums[i], nums[n-1-i] = nums[n-1-i], nums[i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx = -1 # assume our nums are aleady at its largest  eg. [5, 4, 3, 2, 1]
        n = len(nums)

        # 1. find breakpoint
        # ERROR I DID: we need to iterate till 0 which will be -1 not 0 as range 2nd arg is till num-1
        for i in range(n-2, -1, -1) : # from 2nd last to 0th
            if nums[i] < nums[i+1]: # increasing order breaks from last; breakpoint found !
                idx = i
                break
        
        # already at the largest permutation
        if idx == -1:
            nums[::] = nums[::-1]
            return

        # 2. Swap with the smallest from the last till idx - 1 
        for i in range(n-1, idx, -1):
            if nums[i] > nums[idx]: # find the smallest
                nums[i], nums[idx] = nums[idx], nums[i]
                break
            
        # reverse from idx to last
        # nums= nums[: idx + 1] + nums[idx+1:][:: -1]
        # Error I DID: same as indexing error
        nums[idx+1:]= nums[idx+1:][::-1]

def main():
    s = Solution()
    n = [1, 3, 2]
    s.nextPermutation(nums= n)
    print(n)

if __name__ == "__main__":
    main()