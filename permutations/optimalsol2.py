from sample import *
from typing import List


"""
Started On: 27 Aug 23
Ended On: 27 Aug 23
"""
class Solution:
    """
    """
    def recursion(self, nums: List[int], ds: List[int], map: List[bool], res: List[List[int]]):
        # base case : if len of datastructure has reached the len of map meaning used all the items
        if len(ds) == len(map):
            res.append(ds)
            return 
        
        for i in range(len(map)):
            if not map[i]: # if position is not occupied

                ds.append(nums[i]) # add the item to the ds
                map[i] = True # mark the item idx to used
                self.recursion(nums, ds[:], map, res) # recurse for new items
                map[i] = False # unmark the item idx to not used
                ds.pop() # remove the item added to the ds


    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        map = [False] * len(nums)
        self.recursion(nums, [], map, arr) 
        return arr


if __name__ == "__main__":
    sol = Solution()
    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        res = sol.permute(TestCases[i])
        print(res)
        print(Expected[i])
        if not checkSol(res, Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(res)
            print("--> Given")
            print(TestCases[i])
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }/{len(TestCases)}")
    print(f"{testcases_failed = }/{len(TestCases)}")
