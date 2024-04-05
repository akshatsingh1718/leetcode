from sample import *

'''
Started On: 27 Aug 23
Ended On: 27 Aug 23
'''
class Solution:
    '''GFG
    Test Cases Passed: 
    113 /113
    Total Points Scored: 
    4 /4
    Your Total Score: 
    24
    Total Time Taken: 
    0.56
    Your Accuracy: 
    100%
    Attempts No.: 
    1
    '''
    def getPowerSetSum(self, idx, sum, arr, sumSubset):
        if idx == len(arr):
            sumSubset.append(sum)
            return None
        
        self.getPowerSetSum(idx + 1, sum + arr[idx], arr, sumSubset)
        self.getPowerSetSum(idx + 1, sum, arr, sumSubset)

    def subsetSums(self, arr, N):
        sumSubset = []
        self.getPowerSetSum(0, 0, arr, sumSubset)
        sumSubset.sort()
        return sumSubset
		
if __name__ == "__main__":
    # lets print the combinations
    arr = [5, 2, 1]
    sol = Solution()
    res = sol.subsetSums(arr, len(arr))

    for i  in range(len(TestCases)):
        res = sol.subsetSums(TestCases[i], len(TestCases[i]))
        if(res != Expected[i]):
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(TestCases[i])
            print("--> Given")
            print(TestCases[i])


