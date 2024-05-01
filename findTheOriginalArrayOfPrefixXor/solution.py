from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        prev_num = 0

        for num in pref:
            res.append(prev_num ^ num)
            prev_num = num

        return res


pref = [5, 2, 0, 3, 1]
output = [5, 7, 2, 3, 2]

print(Solution().findArray(pref))
