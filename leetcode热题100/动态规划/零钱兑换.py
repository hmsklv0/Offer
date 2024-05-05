# https://programmercarl.com/0322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# 代码随想录题解

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

    def coinChange2(self, coins: List[int], amount: int) -> int:

        # 1 dpi 代表容量为 i 的背包所需要的最少硬币数量
        dp = [float('inf') for _ in range(amount + 1)]

        # 2 递推公式
        # dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        # 3 初始化
        dp[0] = 0

        # 4 遍历顺序
        for i in range(1, amount + 1):
            # 相当于直接在当前背包尝试所有的物品，得到背包的最小硬币数
            # 因此更大容量的背包遍历所有类型的硬币后，就能得到最小硬币数
            # 如 3 的背包， 1、2的硬币
            # dp1轮 dp 0 1
            # dp2轮 dp 0 1 1
            # dp3轮 dp 0 1 1 2
            for j in range(len(coins)):
                if i - coins[j] < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

    def coinChange3(self, coins: List[int], amount: int) -> int:
        # 1 dpi 代表容量为 i 的背包所需要的最少硬币数量
        dp = [float('inf') for _ in range(amount + 1)]

        # 2 递推公式
        # dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        # 3 初始化
        dp[0] = 0

        # 4 遍历顺序
        # 外层遍历物品，内层遍历背包
        for j in range(len(coins)):
            # 相当于先用一种物品，填满所有的背包，再尝试第二种物品，
            # 如 3 的背包， 1、2的硬币
            # 1轮 dp 1 2 3
            # 2轮 dp 1 1 2
            for i in range(coins[j], amount + 1):
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]


nums = [1, 2, 5]
a = Solution()
print(a.coinChange(nums, 11))
