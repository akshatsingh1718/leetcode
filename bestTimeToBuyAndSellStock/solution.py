from typing import List


class Solution:
    """
    TLE
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        n = len(prices)

        for i in range(n):

            for j in range(i + 1, n):

                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max(max_profit, 0)


class Solution2:
    """
    TC: O(n)
    SC: O(1) + O(1) ~ O(1) Constant space

    Algo:
    1. Assume the profit to be 0 initially as buying and selling the stock at the same day gives a profit of 0.
    2. Assume the minimum stock price as the 1st day price of the stock.
    3. The stock can be only sell and buy only one time.
    4. We need to carry the minimum from left to right and negate it from the coming prices of the stock. This way we can have the maximum profit and minimum price on the left of the current day.
    5. Now just find the cost of selling the stock on the ith day and check whether we need to store it as the maximum profit or not.
    6. Also capture the minimum of the current day stock prices and the previous smallest number of the prices of the stock. 

    
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        n = len(prices)

        for i in range(1, n):

            # find the cost to sell the stock at i'th day
            cost = prices[i] - mini

            # find the new profit
            profit = max(profit, cost)

            # update the new min
            mini = min(prices[i], mini)

        return profit

prices = [7,1,5,3,6,4]
o = 5

# prices = [7, 6, 4, 3, 1]
# o = 0
res = Solution2().maxProfit(prices)

print(res)
