from typing import Optional
from sample import *
'''
Start Date: 27 Aug 23
End Date: 27 Aug 23
'''

class Solution:
    '''GFG
    Test Cases Passed: 
    220 /220
    Total Points Scored: 
    2 /2
    Your Total Score: 
    20
    Total Time Taken: 
    0.8
    Your Accuracy: 
    100%
    Attempts No.: 
    1
    '''
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        stack = []
        # add the meetings (start, end, idx) to the stack
        for idx, (s, e) in enumerate(zip(start, end)):
            stack.append((s, e, idx))

        # sort the stack based on end time
        stack.sort(key= lambda x : x[1])

        # move through the stack and count the meeting 
        meetings = 0
        last_meeting_time =  -1
        for s, e, idx in stack:
            if s > last_meeting_time:
                meetings += 1
                last_meeting_time = e
        return meetings


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        Input = len(TestCases[i][1]), TestCases[i][0], TestCases[i][1]
        res = sol.maximumMeetings(*Input)
        if res != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(res)
            print("--> Given")
            print(Input)
            testcases_failed += 1
        else:
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
