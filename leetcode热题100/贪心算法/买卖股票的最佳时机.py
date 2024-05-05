from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        lower = float('inf')
        for i in range(n):
            lower = min(lower, prices[i])
            res = max(prices[i] - lower, res)

        return res

    def maxProfit2(self, prices: List[int]) -> int:
        # 核心思想为:维护今天之前的最小股票价格,然后记录当天卖出的收益,然后逐个遍历
        # 但是最后的结果一定是 某天的高价减去之前的最低买入价格,因此满足
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
