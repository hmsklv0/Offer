class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        cost = float('+inf')

        for i in range(len(prices)):
            # 找到状态转移方程
            cost = min(cost, prices[i])
            profit = max(profit, prices[i] - cost)

        return profit
