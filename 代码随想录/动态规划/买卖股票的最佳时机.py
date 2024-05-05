# https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html#%E6%80%9D%E8%B7%AF
# 题解 贪心 + 动态规划
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 核心思想为:维护今天之前的最小股票价格,然后记录当天卖出的收益,然后逐个遍历
        # 但是最后的结果一定是 某天的高价减去之前的最低买入价格,因此满足
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        # 1
        # dp[i][0] 代表持有股票时的最多现金(此题条件下为最少的负债)
        # dp[i][1] 代表当天不持有股票所能拥有的最多现金
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        # 2 递推公式
        # 此种方法适合手上只持有一只股票
        # dp[i][0] 此题条件下为最少的负债, 看哪天持有股票时的负债最小
        # dp[i][1] 当天不持有股票能获得的钱 要么是昨天不持有股票能获得钱,要么是今天卖出股票,加上昨天持有股票能有的钱
        # dp[i][0] = max(dp[i-1][0], -prices[i])
        # dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        # 3 初始化
        # dp[0][0] 第一天买入股票,亏prices[0]
        # 第一天的 dp[0][1] 当天不持有股票所能拥有的最多现金为 0, 因为当天买股票,当天卖就为0,什么都不买也为0
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        # 4 遍历方式
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
        return dp[-1][1]
