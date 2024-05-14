from typing import List


class Solution:
    """
    GOT TLE

    Time & Space complexity:
    ========================
    TC (sorting case): O(n) * (O(n) + O(n log n))
    TC (heap case): O(n) * (O(n) + O(n log k))

    """

    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:

        res = float("inf")
        n = len(quality)

        # Create worker ratio (wage / quality)
        worker_ratio = []
        for i in range(n):
            worker_ratio.append((wage[i] / quality[i], quality[i]))

        # sort the worker ratio
        worker_ratio.sort(key=lambda x: x[0])

        # Make the managers
        for manager in range(k-1, n):  # TC: O(n)

            #   quality_1       wage_1
            #   ---------   =   --------- => wage_2 = quality_2 * (wage_1 / quality_1) = quality_2 * manager_ratio
            #   quality 2       wage_2

            # Where manager_ratio =     wage_1
            #                       -----------------
            #                           quality_1

            manager_ratio = worker_ratio[manager][0]
            wage_to_use = [wage[manager]]

            # get the wages for each worker
            for i in range(manager):  # TC: O(n)

                # get the ith wage
                ith_wage = quality[i] * manager_ratio
                wage_to_use.append(ith_wage)

            # do not include if the workers are lesser than k min required workers
            if len(wage_to_use) < k:
                continue

            # sort the wages to get the minimum wages first
            wage_to_use.sort()  # TC: O(n logn)

            res = min(res, sum(wage_to_use[:k]))

        return res


# TS1
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
output = 105.00000

# TS2
quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3
output = 30.66667

print(Solution().mincostToHireWorkers(quality, wage, k))
