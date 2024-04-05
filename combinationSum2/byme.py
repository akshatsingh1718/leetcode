from typing import List


class Solution:
    '''
    TLE
    '''
    def checkSum(
        self,
        candidates: List[int],
        index: int,
        target: int,
        currSum: int,
        arr: List[int],
        ans: List[List[int]],
    ):
        if currSum == target and arr not in ans:
            ans.append(arr)
            return

        for i in range(index, len(candidates)):
            if currSum + candidates[i] <= target:
                self.checkSum(
                    candidates,
                    i + 1,
                    target,
                    currSum + candidates[i],
                    sorted(arr + [candidates[i]]),
                    ans,
                )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # candidates.sort()

        self.checkSum(candidates, index=0, target=target, currSum=0, arr=[], ans=ans)
        return ans


def main():
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    res = s.combinationSum2(candidates, target)

    print(res)


if __name__ == "__main__":
    main()
