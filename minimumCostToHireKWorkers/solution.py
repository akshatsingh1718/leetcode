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

        # Make the managers
        for manager in range(n):  # TC: O(n)

            #   quality_1       wage_1
            #   ---------   =   --------- => wage_2 = quality_2 * (wage_1 / quality_1) = quality_2 * manager_ratio
            #   quality 2       wage_2
            manager_ratio = wage[manager] / quality[manager]
            wage_to_use = [wage[manager]]

            # get the wages for each worker
            for i in range(n):  # TC: O(n)
                # ignore if the index is of manager itself
                if i == manager:
                    continue

                # get the ith wage
                ith_wage = quality[i] * manager_ratio
                # if ith wage is smaller then the minimum wage then do not select the worker
                if ith_wage >= wage[i]:
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
