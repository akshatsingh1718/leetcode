from typing import List


class Solution:
    '''
    TC : O(n^2) [to find all the possible combinations] x O(k) [to add arr to ans DS; assuming avg len k for combinations]
    SC : O(k) [avg len of combination] x O(X) [total no of combinations]    
    '''
    def checkSum(
        self,
        candidates: List[int],
        index: int,
        target: int,
        arr: List[int],
        ans: List[List[int]],
    ):
        if target == 0:
            ans.append(arr)
            return

        for i in range(index, len(candidates)):
            # we dont want duplicate
            if i != index and candidates[i] == candidates[i - 1]:
                continue

            if target < candidates[i]:
                break  # since everything is sorted

            self.checkSum(
                candidates,
                i + 1,
                target - candidates[i],
                arr + [candidates[i]],
                ans,
            )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        self.checkSum(candidates, index=0, target=target, arr=[], ans=ans)
        return ans


def main():
    s = Solution()

    # TS 1
    # if we dont check in the loop if the i-1 == i then we can get duplicates
    # as starting with the 1 we can obtain [1, 2, 5] but if we dont check the condition i loop then
    # we will start another recursion starting with another 1 in the array.
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    res = s.combinationSum2(candidates, target)

    print(res)


if __name__ == "__main__":
    main()
