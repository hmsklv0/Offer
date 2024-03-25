from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res= 0
        lower = float('inf')
        for i in range(n):
            lower = min(lower, prices[i])
            res = max(prices[i] - lower, res)

        return res