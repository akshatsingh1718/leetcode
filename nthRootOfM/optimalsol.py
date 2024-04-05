from typing import Optional
from sample import *

"""
Start Date: 29 Aug 23
End Date:29 Aug 23
"""


def NthRoot(n: int, m: int) -> int:
    # n is the no of times we need to mul a number to get m

    ## Loop over possible combs
    for num in range(1, m // 2):
        res = 1

        # mul that no by n times
        for _ in range(n):
            res *= num
            if res > m:
                return -1
        if res == m:
            return num

    return -1


if __name__ == "__main__":
    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    for i in range(len(TestCases)):
        res = NthRoot(*TestCases[i])
        if res != Expected[i]:
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

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")
