# https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# 贪心算法题解

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

