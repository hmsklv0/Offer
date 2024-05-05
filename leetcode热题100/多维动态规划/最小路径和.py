from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # print(dp)
        return dp[m - 1][n - 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # dp[i][j]代表第i行第j列的最小路径和
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 2 递推公式
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # 3 初始化, 初始化要小心
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 4 遍历方式

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


a = Solution()
grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(a.minPathSum(grid1))
