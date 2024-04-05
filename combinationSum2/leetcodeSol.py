from typing import List


class Solution:
    """
    Runtime
    Details
    77ms
    Beats 51.91%of users with Python3
    Memory
    Details
    16.33MB
    Beats 69.66%of users with Python3

    https://leetcode.com/problems/combination-sum-ii/solutions/16878/combination-sum-i-ii-and-iii-java-solution-see-the-similarities-yourself/
    """

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
        elif target < 0:
            return

        for i in range(index, len(candidates)):
            # we dont want duplicate 
            if i != index and candidates[i] == candidates[i - 1]:
                continue

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
