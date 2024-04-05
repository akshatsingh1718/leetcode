from typing import List


class Solution:
    """
    Runtime
    Details
    76ms
    Beats 17.76%of users with Python3
    Memory
    Details
    16.36MB
    Beats 76.81%of users with Python3

    Approach:
    1. start recursive call from 0 to n for candidates and append the item to arr.
    2. check if sum(arr) == target and sorted(arr) is not in result then append to res.
    3. start a new recursive call by adding elements from i to n. i will be the index of last element added
        to the arr as arr can have as many arr[i] as possible to make the target sum. 
    """

    def checkSum(
        self,
        candidates: List[int],
        target: int,
        index: int,
        arr: List[int],
        result: List[List[int]],
    ):
        target_sum = sum(arr)
        if target_sum > target:
            return None

        elif target_sum == target and arr not in result:
            result.append(arr)
            return None

        n = len(candidates)

        for i in range(index, n):
            arr.append(candidates[i])
            self.checkSum(candidates, target, i, sorted(arr[:]), result)
            arr.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        self.checkSum(candidates, target, 0, [], result)

        # for i in range(n):
        #     self.checkSum(candidates, target, i, [candidates[i]], result)

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
