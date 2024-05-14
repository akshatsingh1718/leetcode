from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        # idx: res
        cache = dict()

        def find_energy(idx: int):
            nonlocal k, n, energy, cache
            res = 0
            while idx < n:
                res += energy[idx]
                idx += k

            return res

        res = float("-inf")
        for i in range(n):
            res = max(res, find_energy(i))
            cache[i] = res

        return res


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        # idx: res
        cache = dict()

        def find_energy(idx: int, res: int):
            nonlocal k, n, energy, cache
            if idx >= n:
                return 0

            if cache.get(idx) is not None:
                res += cache[idx]
            else:
                res += energy[idx] + find_energy(idx + k, res)
                cache[idx] = res

            return res

        res = float("-inf")
        for i in range(n):
            res = max(res, find_energy(i, 0))

        return res


energy = [-2, -3, -1]
k = 2
expected = -1

# TS2
energy = [5,2,-10,-5,1]
k = 3
expected = 3

print(Solution().maximumEnergy(energy, k))
