from typing import Optional
from sample import *

"""
Start Date: 29 Aug 23
End Date:
"""


def getExp(num: int, pow: int, limit: int):
    res = 1
    for _ in range(num):
        res *= num
        # if res exceeds limit then return 2
        if res > limit:
            return 2
    # if we got the exp then  return 1
    if res == limit:
        return 1
    # if we didnt get the exp then return 0
    return 0


def NthRoot(n: int, m: int) -> int:
    low, high = 0, m

    while low <= high:
        mid = low + (high - low) // 2

        # find exp of the mid to n
        res = getExp(num=mid, pow=n, limit=m)
        if res == 1:
            return mid

        elif res == 0:
            low = mid + 1
        else:
            high = mid - 1

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
