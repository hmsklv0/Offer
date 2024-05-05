# https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# 题解 贪心算法 + 动态规划
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法，在允许多次买入和多次卖出的情况下，积累每天的最大获利，就可以等于 最终的最大获利
        # 最大获利 必定是由每天的获利累加起来
        # 1 2 3 4 5 1 2 3 4 5 2 3 4 5
        # 在计算过程中，每个阶段的获利汇总成最终的最大获利
        # 而每个小阶段的获利 可以由每天的小获利组成
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res

    def maxProfit2(self, prices: List[int]) -> int:
        # 1
        # dp[i][0] 代表持有股票时的最多现金
        # dp[i][1] 代表当天不持有股票所能拥有的最多现金
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        # 2 递推公式
        # 此种方法适合手上只持有一只股票
        # dp[i][0] 持有股票时的最多现金, 要么来自昨天也持有股票，今天不变动，要么昨天没有持有股票，今天买入股票，和1最大的区别在于，1 没有买入就没有卖出，因此买入股票是 0 - 股票价格，一开始没有任何资金
        # 而现在因为允许买卖多次，因此现在买入股票时的 最多现金，需要用昨天的不持股所获得的最大现金 dp[i-1][1] - 股票价格 prices[i]
        # dp[i][1] 当天不持有股票能获得的钱 要么是昨天不持有股票能获得钱,要么是今天卖出股票 + 昨天持有股票能有的钱
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] -prices[i])
        # dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        # 3 初始化
        # dp[0][0] 第一天买入股票,亏prices[0]
        # 第一天的 dp[0][1] 当天不持有股票所能拥有的最多现金为 0, 因为当天买股票,当天卖就为0,什么都不买也为0
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        # 4 遍历方式
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]
