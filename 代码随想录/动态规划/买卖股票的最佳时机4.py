# https://programmercarl.com/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.html#%E6%80%9D%E8%B7%AF
# 题解

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 动态规划
        # dp[i][0] 无操作
        # dp[i][1] 第一次买入后的最高现金
        # dp[i][2] 第一次卖出的最高现金
        # dp[i][3] 第二次买入的最高现金
        # dp[i][4] 第二次卖出的最高现金
        # dp[i][2 * k + 1] 第 k + 1 次买入的最高现金
        # dp[i][2 * k + 2] 第 k + 1 次卖出的最高现金
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(len(prices))]

        # 2 递推公式
        # # dp[1] = max(dp[1], 0 - prices[i])
        # dp[i][1] = - prices[i] 保证了永远是第一次买入，因此后续迭代的过程中保证了最多两次买入和卖出
        # 保持前一天状态时，列索引保持一致       2 * j + 1      2 * j + 2
        # 买入卖出时，索引向前一次             2 * j        2 * j + 1
        i = 0
        for j in range(k):
            dp[i][2 * j + 1] = max(dp[i - 1][2 * j + 1], dp[i - 1][2 * j] - prices[i])
            dp[i][2 * j + 2] = max(dp[i - 1][2 * j + 2], dp[i - 1][2 * j + 1] + prices[i])

        # 3 初始化，所有的买入初始化为 -prices[0]
        for i in range(2 * k + 1):
            if i % 2 == 1:
                dp[0][i] = -prices[0]

        # 4 遍历方式
        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][2 * j + 1] = max(dp[i - 1][2 * j + 1], dp[i - 1][2 * j] - prices[i])
                dp[i][2 * j + 2] = max(dp[i - 1][2 * j + 2], dp[i - 1][2 * j + 1] + prices[i])
        return dp[-1][2 * k]
