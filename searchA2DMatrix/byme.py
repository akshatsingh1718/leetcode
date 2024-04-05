"""
Started On: 24 Aug 23
End On: 24 Aug 23

"""
from typing import List
from sample import *
import numpy as np


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        low_m, low_n = 0, 0
        high_m, high_n = m, n

        # Note: Why using or and not and here ?
        #
        while low_m <= high_m and low_n <= high_n:
            mid_m = low_m + (high_m - low_m) // 2
            mid_n = low_n + (high_n - low_n) // 2
            # print(
            #     f"{low_m=} ; {low_n=}; {high_m=}; {high_n=}; {m= }; {n= }; {mid_m=}; {mid_n=}"
            # )
            print(f"({low_m},{low_n}) ->  ({high_m}, {high_n}) | {mid_m=}; {mid_n=}")

            if matrix[mid_m][mid_n] == target:
                return True

            # if the target is gt mid value then ignore left half
            elif matrix[mid_m][mid_n] < target:
                # [1,   3,  5,  7],
                # [10,  11, 16, 20],
                # [23,  30, 34, 50]],
                # target= 7)

                print(
                    f"--> Target={target} is gt than matrix[{mid_m}][{mid_n}] = {matrix[mid_m][mid_n]} "
                )
                if mid_n == n:
                    low_n = 0
                    low_m = mid_m + 1
                else:
                    low_n = mid_n + 1
                    low_m = mid_m

            # if the target is lt mid value then ignore right half
            else:
                # ([
                # [1, 3, 5, 7],
                # [10, 11, 16, 20],
                # [23, 30, 34, 60]],
                # target= 13),
                print(
                    f"--> Target={target} is lt than matrix[{mid_m}][{mid_n}] = {matrix[mid_m][mid_n]} "
                )

                if mid_n > 0:
                    high_m = mid_m
                    high_n = mid_n - 1
                else:  # eq 0
                    high_n = n
                    high_m -= 1

        print(f"{low_m=} ; {low_n=}; {high_m=}; {high_n=}; {n= }; {m= }")

        return False


if __name__ == "__main__":
    sol = Solution()

    # iterate over rows
    testcases_passed = 0
    testcases_failed = 0
    # iterate over rows
    for i in range(len(TestCases)):
        print("=" * 50)
        given = TestCases[i]
        res = sol.searchMatrix(TestCases[i][0], TestCases[i][1])
        if res != Expected[i]:
            print(f"!!!!! Not Passed Testcase -> {i + 1}")
            print("--> Expected")
            print(Expected[i])
            print("--> Got")
            print(res)
            print("--> Given")
            print(given)
            testcases_failed += 1
        else:
            print(f"Passes TC = {i+1}")
            testcases_passed += 1

    print(f"{testcases_passed = }")
    print(f"{testcases_failed = }")


# [[1, 3, 5, 7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 60]]
# Target = 3

# m = 3, n = 4

# high_m = m - 1 = 3 - 1 = 2
# high_n = n - 1 = 4 - 1 = 3
# low_m = 0
# low_n = 0


# mid_m = low_m + (high_m - low_m) // 2 => 0 + (2 - 0) // 2 => 1
# mid_n = low_n + (high_n - low_n) // 2 => 0 + (3 - 0) // 2 => 1

# check matrix[mid_m, mid_n] => matrix[1, 1] => 11
# 11 is gt than 3 (target) ignore right half

# New
# high_m = mid_m - 1 = 1 - 1 = 0
# high_n = mid_n - 1 = 1 - 1 = 0

# mid_m = low_m + (high_m - low_m) // 2 => 0 + (1 - 0) // 2 => 0
# mid_n = low_n + (high_n - low_n) // 2 => 0 + (1 - 0) // 2 => 0

# check matrix[mid_m, mid_n] => matrix[0, 0] => 1
# 1 is lt than 3 (target) ignore left half
