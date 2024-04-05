from typing import List


class Solution:
    """
    Runtime
    Details
    53ms
    Beats 86.07%of users with Python3
    Memory
    Details
    16.25MB
    Beats 94.13%of users with Python3

    Approach:
    1. start recursive call from 0 to n for candidates and append the item to arr.
    2. check if sum(arr) == target and sorted(arr) is not in result then append to res.
    3. start a new recursive call by adding elements from i to n. i will be the index of last element added
        to the arr as arr can have as many arr[i] as possible to make the target sum.

    Add onns on byme1.py:

    1. vigneshwar1185s1
        https://leetcode.com/problems/combination-sum/solutions/1777569/full-explanation-with-state-space-tree-recursion-and-backtracking-well-explained-c/comments/1405146
        One small optimization:
        We can add the backtrack in the for loop by checking if adding the candidate[i] will exceed the target value.
        If it exceeds we need not do recursion with that candidate[i]

        
    SC & TC :
        
        - TC : O(2^t) [since one position can have more than occurrence] + O(k) [adding ds into ds]
            In general, interviewer doesn't ask about the TC of the recursion problem but if he does we can tell him exponential.
            
        - SC : O(k . X) [k is the avg length and x is the no of combinations]
            We are not sure how many combinations can this recursive call can have to make up the target
    """

    def checkSum(
        self,
        candidates: List[int],
        target: int,
        index: int,
        arr: List[int],
        result: List[List[int]],
        currSum: int,
    ):
        if currSum == target and arr not in result:
            result.append(arr) # this will take o(n) time to add into a DS and not a constant time
            return None

        for i in range(index, len(candidates)):
            if (
                currSum + candidates[i] > target
            ):  # this will prevent a new recursive call
                continue

            self.checkSum(
                candidates,
                target,
                i,
                sorted(arr + [candidates[i]]),
                result,
                currSum + candidates[i],
            )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.checkSum(candidates, target, 0, [], result, 0)
        return result


def isSameList(res, output):
    if len(res) != len(output):
        return False

    for ri in res:
        if ri not in output:
            return False

    return True


def main():
    s = Solution()

    candidates = [2, 3, 2, 6, 7]
    target = 7
    output = [[2, 2, 3], [7]]

    # candidates = [2, 3, 5]
    # target = 8
    # output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # candidates = [2]
    # target = 1
    # output = []

    res = s.combinationSum(candidates, target)

    if not isSameList(res, output):
        print(res)
        print("Failed")
    else:
        print("Passed")


if __name__ == "__main__":
    main()
