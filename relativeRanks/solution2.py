from typing import List


class Solution:
    """
    TC: O(n) + O(n) + O(max(score)) ~ O(max(score))
    SC: O(max(score)) ~ O(max(score))
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # find the max
        M = max(score)  # TC: O(n)
        n = len(score)

        score_to_indexes = [0] * (M + 1)  # SC: O(max(score))

        for i in range(n):  # TC: O(n)
            # setting the i + 1 because later on we will neglect all elements
            # which are 0 value and index==0 will be also neglected
            score_to_indexes[score[i]] = i + 1

        place = 1
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [None] * n

        for i in range(M, -1, -1):  # TC: O(max(score))
            if score_to_indexes[i] != 0:
                if place <= 3:
                    result[score_to_indexes[i] - 1] = medals[place - 1]
                else:
                    result[score_to_indexes[i] - 1] = str(place)

                place += 1

        return result


# TS1
score = [5, 4, 3, 2, 1]
output = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

# TS2
score = [10, 3, 8, 9, 4]
output = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

print(Solution().findRelativeRanks(score))
