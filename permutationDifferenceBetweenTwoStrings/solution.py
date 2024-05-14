class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_idx = {ch: id for id, ch in enumerate(s)}
        t_idx = {ch: id for id, ch in enumerate(t)}

        res = 0

        for ch in s:
            res += abs(s_idx[ch] - t_idx[ch])
        return res