# https://programmercarl.com/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.html

import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

    def numSquares2(self, n: int) -> int:
        # dpi 代表 容量为 i 的背包 能够装 完全平方数 的最小数量
        dp = [float('inf') for i in range(n + 1)]

        # 2 递推公式
        # dp[i] = min(dp[i], dp[i - j * j] + 1)

        # 3 初始化
        dp[0] = 0

        # 4 遍历顺序
        for i in range(1, n + 1):
            for j in range(int(math.pow(i, 0.5)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


a = Solution()
print(a.numSquares(4))
