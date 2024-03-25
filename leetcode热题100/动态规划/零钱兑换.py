from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums_len = len(coins)

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for j in range(1, amount + 1):
            for i in range(nums_len):
                if j - coins[i] < 0:
                    continue
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


nums = [1, 2, 5]
a = Solution()
print(a.coinChange(nums, 11))
