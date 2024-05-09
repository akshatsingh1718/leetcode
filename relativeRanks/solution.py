"""
Problem: https://leetcode.com/problems/relative-ranks/submissions/1252455851/?envType=daily-question&envId=2024-05-08
"""

from typing import List


class Solution:
    """
    TC: O(n) [create indexes] + O(n logn) [sorting] + O(n) [for result] ~ O(n logn)
    SC: O(n) [storing indexes] + O(n) [storing ranks] ~ O(n)
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        # Store the indexes of initial values
        indexes = {x[1]: x[0] for x in enumerate(score)}

        # sort array in descending order to get the
        # ranks. The largest score will have the lowest rank
        scores_ranks = sorted(score, reverse=True)

        # store result
        result = ["" for _ in range(n)]

        # Get the rank and their scores
        for rank, sc in enumerate(scores_ranks):
            # get the index of the score
            idx = indexes[sc]

            # check for Gold, silver and bronze medal
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            # else assign the rank value
            else:
                result[idx] = str(rank + 1)

        return result


class Solution:
    """
    TC: O(n) [create indexes] + O(n logn) [sorting] + O(n) [for result] ~ O(n logn)
    SC: O(n) [storing indexes]
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexes = {x[1]: x[0] for x in enumerate(score)}

        score.sort(reverse=True)
        n = len(score)
        result = ["" for _ in range(n)]

        for rank in range(n):
            sc = score[rank]
            idx = indexes[sc]

            result[idx] = (
                ["Gold Medal", "Silver Medal", "Bronze Medal"][rank]
                if rank <= 2
                else str(rank + 1)
            )

        return result


# TS1
score = [5, 4, 3, 2, 1]
output = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

# TS2
score = [10, 3, 8, 9, 4]
output = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

print(Solution().findRelativeRanks(score))
