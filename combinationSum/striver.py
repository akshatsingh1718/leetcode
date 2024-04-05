from typing import List


class Solution:
    def checkSum(
        self,
        candidates: List[int],
        index: int,
        target: int,
        arr: List[int],
        res: List[List[int]],
    ):
        if index == len(candidates):
            if target == 0 and arr not in res:
                res.append(arr)
            return

        if candidates[index] <= target:
            self.checkSum(
                candidates,
                index,
                target - candidates[index],
                sorted(arr + [candidates[index]]),
                res,
            )

        # if sum was gt than the target check for next index if its lesser
        self.checkSum(
            candidates,  # arr
            index + 1,
            target,
            arr,  # ds
            res,  # ans
        )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.checkSum(
            candidates,
            index=0,
            target=target,
            arr=[],
            res=result,
        )
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
