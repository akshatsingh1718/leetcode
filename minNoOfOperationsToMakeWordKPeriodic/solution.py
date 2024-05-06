'''
Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/
'''

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        counts = dict()

        n = len(word)
        max_counts = 0
        for i in range(0, n, k):
            sub_str = word[i : i + k]
            counts[sub_str] = counts.get(sub_str, 0) + 1
            max_counts = max(max_counts, counts[sub_str])

        return (n // k) - max_counts
