from typing import List


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