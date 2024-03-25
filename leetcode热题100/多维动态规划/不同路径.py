from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        all_step = m + n - 2
        res = 0

        dp = [[0 for i in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                left, up = 0, 0

                if 1 <= i <= m - 1:
                    up = dp[i - 1][j]
                if 1 <= j <= n - 1:
                    left = dp[i][j - 1]
                dp[i][j] = left + up

        # print(dp)
        return dp[m - 1][n - 1]


a = Solution()
a.uniquePaths(3, 7)
