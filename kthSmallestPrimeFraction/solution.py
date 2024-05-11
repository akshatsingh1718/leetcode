from typing import List


class Solution:
    """
    TC: O(n^2) [fractions] + O(n logn) [sorting]
    SC: O(n^2) [fractions]

    Algo:
    1. Find all the fractions from i: 0->n ; j: i+1->n
    2. sort the fractions.
    3. return the numbers from which fractions was calculated.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)

        fractions = [
            [arr[i] / arr[j], [arr[i], arr[j]]]
            for i in range(n)
            for j in range(i + 1, n)
        ]

        fractions.sort(key=lambda x: x[0])
        return fractions[k - 1][1]


arr = [1, 2, 3, 5]
k = 3
output = [2, 5]

print(Solution().kthSmallestPrimeFraction(arr, k))
